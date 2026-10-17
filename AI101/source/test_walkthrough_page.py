"""Browser checks for the Code tab (needs: pip install playwright; a Chromium browser).
Run from the AI101 folder: python source/test_walkthrough_page.py [screenshot_dir]
Opens the page from disk; no network is used."""
import sys, json
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
URL = (ROOT / 'AI_101_for_Mechanical_Engineers.html').as_uri()
SHOTS = Path(sys.argv[1]) if len(sys.argv) > 1 else None
errors = []

def tabs(page):
    return page.eval_on_selector_all('nav.tabs a', 'els=>els.map(e=>e.textContent.trim())')

def go(page, h):
    page.evaluate("h=>{location.hash=h}", h)
    page.wait_for_timeout(150)

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome') if Path('/opt/pw-browsers/chromium-1194/chrome-linux/chrome').exists() else p.chromium.launch()
    ctx = b.new_context(viewport={'width': 1200, 'height': 900})
    page = ctx.new_page()
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
    page.goto(URL); page.wait_for_timeout(300)

    # Modules that have a walkthrough (Modules 1 and 13 have none, see the PR notes)
    WITH = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16]
    WITHOUT = [1, 13]
    assert sorted(WITH + WITHOUT) == list(range(1, 17))
    walk = page.evaluate('WALK')
    assert sorted(int(k[1:]) for k in walk) == WITH, sorted(walk)

    # 1. every module: tab bar is Lessons, [Code only where a walkthrough exists], Review, Quiz
    for n in range(1, 17):
        go(page, f'#/m/{n}/1')
        t = tabs(page)
        assert t[-2:] == ['Review', 'Quiz'], (n, t)
        assert ('Code' in t) == (n in WITH), (n, t)
        if n in WITH: assert t[-3] == 'Code' and len(t) == 6, (n, t)
        else: assert len(t) == 5, (n, t)

    # 2. Next button: Lesson 3 -> Code (with walkthrough) / Review (without)
    def nxt(h):
        go(page, h); return page.get_by_role('link', name='Next →').get_attribute('href')
    for n in range(1, 17):
        assert nxt(f'#/m/{n}/3') == (f'#/m/{n}/code' if n in WITH else f'#/m/{n}/review'), n
    assert nxt('#/m/2/2') == '#/m/2/3'

    # 3. progress is untouched by visiting Code tabs
    def snap():
        d = json.loads(page.evaluate("()=>JSON.stringify(Object.fromEntries(Object.entries(localStorage)))"))
        st = json.loads(d['ai101-me-progress-v1']); st.pop('view', None)   # 'view' = last page visited, updated by every navigation
        return json.dumps(st, sort_keys=True)
    go(page, '#/m/2/3'); before = snap()
    for n in WITH:
        go(page, f'#/m/{n}/code'); page.wait_for_timeout(120)
        page.get_by_role('button', name='Copy code').first.click()
    go(page, '#/m/16/code')
    page.get_by_role('link', name='Next →').click(); page.wait_for_timeout(150)
    assert page.evaluate('location.hash') == '#/m/16/review'
    assert snap() == before, 'saved progress changed (other than the last-visited page)'

    # 4. Code page content, every module with a walkthrough
    for n in WITH:
        w = walk[f'm{n:02d}']
        go(page, f'#/m/{n}/code'); page.wait_for_timeout(150)
        txt = page.inner_text('main')
        for s in ['Code walkthrough', 'Optional and not graded', 'Python does not run on this page', 'Objective', 'Before you start', 'Step 1.', 'Expected output', 'Try it', 'Limits of this example', 'Open in Google Colab', 'synthetic']:
            assert s.lower() in txt.lower(), (n, s)
        k = len(w['steps'])
        assert page.locator('main pre').count() == k + k + 1 + 1, (n, page.locator('main pre').count())
        colab = page.get_by_role('link', name='Open in Google Colab').get_attribute('href')
        assert colab == f'https://colab.research.google.com/github/mazhar17/courses/blob/main/AI101/AI_101_notebooks/walkthrough_m{n:02d}.ipynb', (n, colab)
        assert page.get_by_role('link', name='Download notebook').get_attribute('href') == f'AI_101_notebooks/walkthrough_m{n:02d}.ipynb'
        assert (ROOT / 'AI_101_notebooks' / f'walkthrough_m{n:02d}.ipynb').exists()
        assert page.locator('nav.tabs a.active').inner_text().strip() == 'Code'
        assert page.locator('main button:has-text("Mark as complete")').count() == 0
        assert '`' not in txt, (n, 'literal backtick shown')
    go(page, '#/m/2/code')
    page.locator('main pre').first.focus()
    assert page.evaluate('document.activeElement.tagName') == 'PRE'

    # 5. modules without a walkthrough
    for n in WITHOUT:
        go(page, f'#/m/{n}/code')
        assert 'no code walkthrough for this module yet' in page.inner_text('main'), n

    # 6. layout: no horizontal page scroll, light and dark, desktop and 375 px, every walkthrough
    for theme in ('light', 'dark'):
        for w_, hgt, tag in ((1200, 900, 'desktop'), (375, 800, 'mobile')):
            page.set_viewport_size({'width': w_, 'height': hgt})
            page.emulate_media(color_scheme=theme)
            for n in WITH:
                go(page, f'#/m/{n}/code'); page.wait_for_timeout(120)
                over = page.evaluate('document.documentElement.scrollWidth-document.documentElement.clientWidth')
                assert over <= 1, (n, theme, tag, 'page scrolls horizontally', over)
                if SHOTS and n in (2, 12, 15, 16):
                    SHOTS.mkdir(exist_ok=True)
                    page.screenshot(path=str(SHOTS / f'code_m{n:02d}_{tag}_{theme}.png'), full_page=(tag == 'mobile'))
    b.close()

assert not errors, errors
print('PASS browser checks: tabs for 16 modules, navigation, progress untouched, content, layout light/dark, desktop/mobile')
