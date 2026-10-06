from pathlib import Path
import json
from ai101_content import MODULES
from ai101_notebooks import LABS,ENV
CHECKLIST='''# AI 101 mini-project submission checklist

- State the decision, users, inputs available at prediction time, target and operating domain.
- Identify synthetic versus measured data and record units, provenance and missingness.
- Justify the evaluation boundary (independent designs, time, machine or event).
- Fit preprocessing inside training; use validation for choices; lock the final test.
- Compare a simple baseline on the same examples and information.
- Report metrics with units/class counts and interpret consequences.
- Check one known numerical case and at least one relevant physical relationship or limit.
- Explain verification versus real-system validation; avoid unsupported hardware claims.
- Record environment, seed, code and transformations; restart and run top to bottom.
- Disclose permitted AI assistance and retain your own reasoning.
- Submit a runnable notebook with outputs and a short report. Browser completion is separate.

Rubric: problem/data 20%; baseline/split/preprocessing 25%; evaluation/interpretation 25%; physical checks/limitations 20%; reproducibility/disclosure 10%.
'''
text='# AI 101 for Mechanical Engineers\n\nVersion 1.0. Authored foundational course; synthetic teaching examples. Practical notebook work is assessed separately from browser knowledge checks.\n'
for m in MODULES:
 text+='\n## Module '+str(m['num'])+': '+m['title']+'\n\nLearning outcomes:\n'+''.join('- '+o+'\n' for o in m['outcomes'])
 for l in m['lessons']:text+='\n### '+l['title']+'\n\n'+l['text']+'\n\nPause and explain: '+l['check']+'\n'
 text+='\n### Terms\n\n'+''.join('**'+t['term']+'**: '+t['definition']+' Example: '+t['example']+'\n\n' for t in m['terms'])
text+='\n'+CHECKLIST
data=dict(modules=MODULES,labs=LABS,environment=ENV,checklist=CHECKLIST,courseText=text)
payload=json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
app=Path('ai101_app.js').read_text(encoding='utf-8')
shell=Path('ai101_shell.html').read_text(encoding='utf-8')
Path('AI_101_for_Mechanical_Engineers.html').write_text(shell.replace('/*DATA*/','const DATA='+payload+';').replace('/*APP*/',app),encoding='utf-8')
Path('AI_101_course_text.md').write_text(text,encoding='utf-8')
Path('AI_101_requirements.txt').write_text(ENV,encoding='utf-8')
Path('AI_101_submission_checklist.md').write_text(CHECKLIST,encoding='utf-8')
out=Path('AI_101_notebooks');out.mkdir(exist_ok=True)
for l in LABS:
 for variant in ['starter','reference']:(out/(l['id']+'_'+variant+'.ipynb')).write_text(json.dumps(l[variant],ensure_ascii=False,indent=1),encoding='utf-8')
Path('ai101_data.json').write_text(json.dumps(data,ensure_ascii=False),encoding='utf-8')
print('Built',len(MODULES),'modules,',sum(len(m['lessons']) for m in MODULES),'lessons,',sum(len(m['questions']) for m in MODULES),'questions,',sum(len(m['terms']) for m in MODULES),'terms and',len(LABS)*2,'notebooks.')
