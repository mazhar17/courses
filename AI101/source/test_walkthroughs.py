"""Execute each walkthrough's code and compare stdout exactly with the expected output
shown on the course page. Run from the AI101 folder: python source/test_walkthroughs.py
(imports from source/ are resolved relative to this file)."""
import contextlib, io, json, platform, sys
from pathlib import Path

SRC = Path(__file__).resolve().parent
sys.path.insert(0, str(SRC))
from ai101_walkthroughs import WALKTHROUGHS, notebook_for, public_data  # noqa: E402

print('Python', platform.python_version())
checked = 0


def run(codes, ns=None):
    ns = {} if ns is None else ns
    outs = []
    for c in codes:
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            exec(compile(c, '<walkthrough>', 'exec'), ns)
        outs.append(buf.getvalue().rstrip('\n'))
    return outs


for mid, w in WALKTHROUGHS.items():
    outs = run([s['code'] for s in w['steps']])
    for s, got in zip(w['steps'], outs):
        assert got == s['expected_output'], (mid, s['heading'], got, s['expected_output'])
        checked += 1
    # 'Try it' change must apply exactly once and give the stated output
    old, new = w['try_it']['change']
    last = w['steps'][-1]['code']
    assert last.count(old) == 1, 'try-it anchor must occur once'
    got = run([last.replace(old, new)])[0]
    assert got == w['try_it']['expected_output'], (mid, got)
    checked += 1
    # a clean, top-to-bottom run of the whole notebook gives the same outputs
    n = notebook_for(mid)
    codes = [''.join(c['source']) for c in n['cells'] if c['cell_type'] == 'code']
    assert run(codes) == [s['expected_output'] for s in w['steps']]
    assert all(c['outputs'] == [] and c['execution_count'] is None for c in n['cells'] if c['cell_type'] == 'code')
    # the file on disk matches the generator
    path = SRC.parent / 'AI_101_notebooks' / w['notebook']
    assert path.exists(), 'notebook file missing: ' + str(path)
    assert json.loads(path.read_text(encoding='utf-8')) == json.loads(json.dumps(n, ensure_ascii=False))
    # no network, no non-stdlib imports in walkthrough code
    for s in w['steps']:
        assert 'import ' not in s['code'] and 'open(' not in s['code'], 'unexpected import or file access'
    assert set(public_data()[mid]) >= {'colab', 'download', 'steps', 'try_it'}

# Module 2 arithmetic, independent of the code strings above
assert 100 * 1000 * 0.02 == 2000 and 2000 / 0.8 == 2500 and 2800 - 2500 == 300
for dp, q, y, eta, r in [(100, .02, 2800, .8, 300), (80, .015, 1650, .8, 150), (120, .025, 3950, .8, 200),
                         (100, .02, 2800, .75, 133.3), (80, .015, 1650, .75, 50.0), (120, .025, 3950, .75, -50.0)]:
    assert round(y - dp * 1000 * q / eta, 1) == r, (dp, q, y, eta, r)
print(f'PASS {checked} outputs matched; {len(WALKTHROUGHS)} walkthrough(s)')
