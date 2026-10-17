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

    # 1. every module: tab bar is Lessons, [Code only for module 2], Review, Quiz
    for n in range(1, 17):
        go(page, f'#/m/{n}/1')
        t = tabs(page)
        assert t[-2:] == ['Review', 'Quiz'], (n, t)
        assert ('Code' in t) == (n == 2), (n, t)
        if n == 2: assert t[-3] == 'Code' and len(t) == 6, t
        else: assert len(t) == 5, (n, t)

    # 2. Next button: Lesson 3 -> Code (module 2) / Review (others)
    def nxt(h):
        go(page, h); return page.get_by_role('link', name='Next →').get_attribute('href')
    assert nxt('#/m/2/3') == '#/m/2/code'
    assert nxt('#/m/1/3') == '#/m/1/review'
    assert nxt('#/m/16/3') == '#/m/16/review'
    assert nxt('#/m/2/2') == '#/m/2/3'

    # 3. progress is untouched by visiting the Code tab
    def snap():
        d = json.loads(page.evaluate("()=>JSON.stringify(Object.fromEntries(Object.entries(localStorage)))"))
        st = json.loads(d['ai101-me-progress-v1']); st.pop('view', None)   # 'view' = last page visited, updated by every navigation
        return json.dumps(st, sort_keys=True)
    go(page, '#/m/2/3'); before = snap()
    go(page, '#/m/2/code'); page.wait_for_timeout(200)
    page.get_by_role('button', name='Copy code').first.click()
    page.get_by_role('link', name='Next →').click(); page.wait_for_timeout(150)
    assert page.evaluate('location.hash') == '#/m/2/review'
    assert snap() == before, 'saved progress changed (other than the last-visited page)'

    # 4. Code page content
    go(page, '#/m/2/code'); page.wait_for_timeout(200)
    txt = page.inner_text('main')
    for s in ['Code walkthrough', 'Optional and not graded', 'Python does not run on this page', 'Objective', 'Before you start', 'Step 1.', 'Step 5.', 'Expected output', 'Try it', 'Limits of this example', 'Open in Google Colab', 'synthetic']:
        assert s.lower() in txt.lower(), s
    assert page.locator('main pre').count() == 5 + 5 + 1 + 1, page.locator('main pre').count()
    colab = page.get_by_role('link', name='Open in Google Colab').get_attribute('href')
    assert colab == 'https://colab.research.google.com/github/mazhar17/courses/blob/main/AI101/AI_101_notebooks/walkthrough_m02.ipynb'
    assert page.get_by_role('link', name='Download notebook').get_attribute('href') == 'AI_101_notebooks/walkthrough_m02.ipynb'
    assert page.locator('nav.tabs a.active').inner_text().strip() == 'Code'
    assert page.locator('main button:has-text("Mark as complete")').count() == 0
    # keyboard: a code block can take focus
    page.locator('main pre').first.focus()
    assert page.evaluate('document.activeElement.tagName') == 'PRE'

    # 5. module without a walkthrough
    go(page, '#/m/5/code')
    assert 'no code walkthrough for this module yet' in page.inner_text('main')

    # 6. layout: no horizontal page scroll at phone width; light and dark
    for theme in ('light', 'dark'):
        for w, hgt, tag in ((1200, 900, 'desktop'), (375, 800, 'mobile')):
            page.set_viewport_size({'width': w, 'height': hgt})
            page.emulate_media(color_scheme=theme)
            go(page, '#/m/2/code'); page.wait_for_timeout(250)
            over = page.evaluate('document.documentElement.scrollWidth-document.documentElement.clientWidth')
            assert over <= 1, (theme, tag, 'page scrolls horizontally', over)
            if SHOTS:
                SHOTS.mkdir(exist_ok=True)
                page.screenshot(path=str(SHOTS / f'code_m02_{tag}_{theme}.png'), full_page=(tag == 'mobile'))
    b.close()

assert not errors, errors
print('PASS browser checks: tabs for 16 modules, navigation, progress untouched, content, layout light/dark, desktop/mobile')
