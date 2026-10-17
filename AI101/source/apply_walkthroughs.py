"""Add the optional 'Code' tab to the published course page and write the notebooks.

Why a patcher: the published AI101/AI_101_for_Mechanical_Engineers.html has been edited
since source/ was last used to build it (lesson media, rewritten lessons and quizzes), so
re-running build_ai101.py would overwrite those edits. This script changes the published
page in a small, exact way instead. Every anchor must match exactly once or nothing is
written. Running it twice is refused.

Usage (from the AI101 folder):  python source/apply_walkthroughs.py
"""
import json, sys
from pathlib import Path

SRC = Path(__file__).resolve().parent
ROOT = SRC.parent
sys.path.insert(0, str(SRC))
from ai101_walkthroughs import WALKTHROUGHS, notebook_for, public_data  # noqa: E402

MARK = '/*AI101-CODE-WALKTHROUGH*/'
PAGE = ROOT / 'AI_101_for_Mechanical_Engineers.html'

CSS = MARK + '''
.walk-note{border-left:4px solid var(--brand);background:var(--brand-soft);padding:10px 16px;border-radius:0 8px 8px 0;margin:16px 0}
.walk pre{margin:10px 0;padding:14px 16px;border:1px solid var(--line);border-radius:8px;background:var(--bg);color:var(--ink);font:14px/1.55 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;overflow-x:auto;max-width:100%;white-space:pre;tab-size:4}
.walk pre.out{border-left:4px solid var(--ok);background:var(--ok-bg)}
.walk .label{font-size:13px;font-weight:700;color:var(--soft);margin:14px 0 0}
.walk code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.92em}
.walk .step{border-top:1px solid var(--line);padding-top:8px;margin-top:22px}
'''

JS_TEMPLATE = MARK + '''
const WALK=__DATA__;
function codeBlock(host,codeText,cls,label){
  if(label)host.append(E('p',{class:'label',text:label}));
  host.append(E('pre',{class:cls||'',tabindex:'0','aria-label':label||'Code'},E('code',{text:codeText})));
}
function inlineCode(host,tag,text){
  let el=E(tag);
  text.split('`').forEach((part,i)=>{el.append(i%2?E('code',{text:part}):document.createTextNode(part));});
  host.append(el);
}
function codePage(h,m){
  let w=WALK[m.id];
  if(!w){h.append(E('h2',{text:'Code walkthrough'}),E('p',{text:'There is no code walkthrough for this module yet. Code walkthroughs are optional; they never affect your quiz scores.'}),E('div',{class:'actions'},link('Go to Review',`#/m/${m.num}/review`,'btn primary')));return;}
  let s=E('section',{class:'walk','aria-label':'Code walkthrough'});
  s.append(E('p',{class:'eyebrow',text:'Code walkthrough · optional'}),E('h2',{text:w.title}));
  s.append(E('p',{class:'walk-note'},E('strong',{text:'Optional and not graded. '}),'This page shows code and its expected output. Python does not run on this page. To run the code yourself, use the Google Colab or notebook links at the end. Your quiz scores and progress do not depend on this page.'));
  s.append(E('h3',{text:'Objective'}),E('p',{text:w.objective}),E('p',{class:'small',text:'Supports: '+w.supports}));
  s.append(E('h3',{text:'Before you start'}));
  let ul=E('ul');w.prereqs.forEach(x=>inlineCode(ul,'li',x));s.append(ul);
  s.append(E('p',{text:'Python ideas used on this page:'}));
  let ul2=E('ul');w.python_ideas.forEach(x=>inlineCode(ul2,'li',x));s.append(ul2);
  s.append(E('h3',{text:'The example'}));
  w.example.forEach(x=>inlineCode(s,'p',x));
  codeBlock(s,w.data_table,'out','Synthetic teaching data (invented, not measured)');
  w.steps.forEach(st=>{
    let d=E('div',{class:'step'});
    d.append(E('h3',{text:st.heading}));inlineCode(d,'p',st.explain);
    codeBlock(d,st.code,'','Code');
    d.append(B('Copy code',()=>{try{navigator.clipboard.writeText(st.code).then(()=>message('Code copied.'),()=>message('Copy was blocked by the browser. Select the code and copy it manually.'));}catch(e){message('Copy is not available here. Select the code and copy it manually.');}},'btn'));
    codeBlock(d,st.expected_output,'out','Expected output');
    inlineCode(d,'p',st.output_explain);
    s.append(d);
  });
  let t=E('div',{class:'step'});
  t.append(E('h3',{text:'Try it (optional)'}));
  inlineCode(t,'p',w.try_it.instruction);
  codeBlock(t,w.try_it.expected_output,'out','Expected output after the change');
  inlineCode(t,'p',w.try_it.expected_observation);
  s.append(t);
  s.append(E('h3',{text:'Limits of this example'}));
  let ul3=E('ul');w.limits.forEach(x=>inlineCode(ul3,'li',x));s.append(ul3);
  if(w.related)s.append(E('p',{class:'small',text:w.related}));
  s.append(E('h3',{text:'Run it yourself'}));
  s.append(E('p',{},E('a',{class:'btn primary',href:w.colab,target:'_blank',rel:'noopener',text:'Open in Google Colab'}),' ',E('a',{class:'btn',href:w.download,download:'',text:'Download notebook (.ipynb)'})));
  s.append(E('p',{class:'small',text:'Colab opens the notebook from the course repository and asks you to sign in with a Google account before it runs code. You need no installation. You can also download the notebook and open it in Jupyter. The expected outputs above were produced by running this same code.'}));
  h.append(s);
  h.append(E('div',{class:'actions'},link('Next →',`#/m/${m.num}/review`,'btn primary'),link('← Back to Lesson 3',`#/m/${m.num}/3`,'btn')));
}
'''

# (old, new) pairs; each `old` must occur exactly once in the page
EDITS = [
 ('</style>', CSS + '</style>'),
 ("function route(hash){", '__JS__' + "function route(hash){"),
 ("(?:\\/(\\d|quiz|cards|review))?$/", "(?:\\/(\\d|quiz|cards|review|code))?$/"),
 ("['1','2','3','quiz','cards','review'].includes(sub)", "['1','2','3','quiz','cards','review','code'].includes(sub)"),
 ("tabs.append(link('Review',", "if(WALK[m.id])tabs.append(link('Code',`#/m/${m.num}/code`,r.sub==='code'?'active':''));tabs.append(link('Review',"),
 ("if(['review','cards'].includes(r.sub)){moduleReview(h,m);return;}", "if(r.sub==='code'){codePage(h,m);return;}if(['review','cards'].includes(r.sub)){moduleReview(h,m);return;}"),
 (":`#/m/${m.num}/review`;h.append(E('div',{class:'actions'},link('Next →',next", ":(WALK[m.id]?`#/m/${m.num}/code`:`#/m/${m.num}/review`);h.append(E('div',{class:'actions'},link('Next →',next"),
]


def main():
    page = PAGE.read_text(encoding='utf-8')
    if MARK in page:
        sys.exit('Already applied (marker found). Restore the page from git before re-applying.')
    data = json.dumps(public_data(), ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
    js = JS_TEMPLATE.replace('__DATA__', data)
    for old, new in EDITS:
        n = page.count(old)
        if n != 1:
            sys.exit(f'Anchor found {n} times (need exactly 1): {old[:70]!r}. Nothing written.')
    for old, new in EDITS:
        page = page.replace(old, new.replace('__JS__', js))
    nbdir = ROOT / 'AI_101_notebooks'
    nbdir.mkdir(exist_ok=True)
    for mid, w in WALKTHROUGHS.items():
        (nbdir / w['notebook']).write_text(json.dumps(notebook_for(mid), ensure_ascii=False, indent=1), encoding='utf-8')
    PAGE.write_text(page, encoding='utf-8')
    print('Applied: Code tab for', ', '.join(sorted(WALKTHROUGHS)), '| notebooks written:', len(WALKTHROUGHS))


if __name__ == '__main__':
    main()
