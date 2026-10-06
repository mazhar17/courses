import json,sys,contextlib,io,platform
from pathlib import Path
import numpy as np
from html.parser import HTMLParser
print('Python',platform.python_version(),'NumPy',np.__version__)
files=sorted(Path('AI_101_notebooks').glob('*.ipynb'));count=0;executed=[]
for path in files:
 n=json.loads(path.read_text(encoding='utf-8'));assert n['nbformat']==4 and n['nbformat_minor']==5
 ids=[]
 for i,c in enumerate(n['cells']):
  assert c['cell_type'] in ['code','markdown'] and isinstance(c['metadata'],dict)
  assert isinstance(c['source'],list) and all(isinstance(s,str) for s in c['source'])
  ids.append(c['id'])
  if c['cell_type']=='code':
   assert c['outputs']==[] and c['execution_count'] is None
   compile(''.join(c['source']),str(path)+':'+str(i+1),'exec');count+=1
 assert len(ids)==len(set(ids))
 if 'reference' in path.name:
  ns={};capture=io.StringIO()
  with contextlib.redirect_stdout(capture):
   for i,c in enumerate(n['cells']):
    if c['cell_type']=='code':exec(compile(''.join(c['source']),str(path)+':'+str(i+1),'exec'),ns)
  print('PASS reference execution',path.name);print(capture.getvalue())
  path.with_suffix('.execution.txt').write_text(capture.getvalue(),encoding='utf-8');executed.append(path.name)
 else:
  ns={};stopped=False
  with contextlib.redirect_stdout(io.StringIO()):
   for c in n['cells']:
    if c['cell_type']=='code':
     try:exec(''.join(c['source']),ns)
     except NotImplementedError:stopped=True;break
  assert stopped
class Inspector(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.tags=[]
 def handle_starttag(self,t,a):
  self.tags.append(t)
  for k,v in a:
   if k=='id':self.ids.append(v)
p=Inspector();p.feed(Path('AI_101_for_Mechanical_Engineers.html').read_text(encoding='utf-8'))
assert len(p.ids)==len(set(p.ids));assert all(t in p.tags for t in ['html','head','body','main','script','style'])
print('PASS HTML parser ingestion and unique shell IDs')
print('PASS',len(files),'notebook structures;',count,'code cells compiled;',len(executed),'references executed; 4 starters stopped at intended TODOs.')
try:import nbformat
except ImportError:print('UNVERIFIED formal nbformat package validation: unavailable; structural checks above passed.')
else:
 for path in files:nbformat.validate(json.loads(path.read_text(encoding='utf-8')))
 print('PASS formal nbformat validation')
