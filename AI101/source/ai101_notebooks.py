import json
def nb(title,cells):
 return dict(nbformat=4,nbformat_minor=5,metadata=dict(kernelspec=dict(display_name='Python 3',language='python',name='python3'),language_info=dict(name='python'),title=title),cells=[dict(cell_type=t,id=f'ai101-{i:03}',metadata={},source=s.splitlines(True),**(dict(execution_count=None,outputs=[]) if t=='code' else {})) for i,(t,s) in enumerate(cells)])
def md(s):return ('markdown',s)
def code(s):return ('code',s)
HEADER='''All examples are explicitly synthetic teaching examples, not validated machinery data.
Run from a clean kernel, top to bottom. Python 3.10+ and NumPy 1.26+ are the declared target environment. See the course validation file for actual tested versions. No internet or AI API is used by these notebooks after installing dependencies.
Use the starter before consulting the reference. Record permitted AI assistance and explain your own choices.
'''
LABS=[]
def lab(id,title,purpose,base,exercises,closing):
 starter=[md('# '+title+' — starter\n\n'+purpose+'\n\n'+HEADER)]+base[:]
 ref=[md('# '+title+' — reference\n\n'+purpose+'\n\n'+HEADER)]+base[:]
 for heading,hint,stub,solution in exercises:
  starter += [md('## '+heading+'\n\n'+hint),code(stub)]
  ref += [md('## '+heading+'\n\n'+hint),code(solution)]
 starter += [md(closing)];ref += [md(closing)]
 LABS.append(dict(id=id,title=title,purpose=purpose,starter=nb(title+' starter',starter),reference=nb(title+' reference',ref)))

lab('lab01','Read and inspect engineering data','Identify rows, input columns, target values, missingness and units. Create an audit trail without treating every unusual reading as a fault.',[
code('''import csv, io, sys
import numpy as np
print('Python', sys.version.split()[0], 'NumPy', np.__version__)
CSV = """run,flow_m3s,pressure_rise_Pa,power_kW
1,0.010,100000,1.42
2,0.015,110000,2.30
3,0.020,120000,3.34
4,,125000,3.70
5,0.025,130000,4.53
6,0.030,-1000,5.20
7,0.028,135000,5.26
8,0.024,115000,3.84
9,0.018,105000,2.67
10,0.022,118000,3.64
"""
rows = list(csv.DictReader(io.StringIO(CSV)))
units = {'flow_m3s': 'm^3/s', 'pressure_rise_Pa': 'Pa', 'power_kW': 'kW'}
print('Synthetic operating tests:', len(rows), 'units:', units)
''')],[
('1. Build arrays','X has shape (10,2), with flow and pressure rise. y has shape (10,). Convert an empty field to np.nan; retain run numbers. Hint: float(value) if value else np.nan.',
'''def arrays(rows):
    # Return X (n,2), y (n,), ids (n,). Preserve missing values.
    raise NotImplementedError('Build numeric arrays from the CSV rows')
X, y, ids = arrays(rows)
print(X.shape, y.shape, ids)
''',
'''def arrays(rows):
    value = lambda r,k: float(r[k]) if r[k] else np.nan
    X = np.array([[value(r,'flow_m3s'), value(r,'pressure_rise_Pa')] for r in rows])
    y = np.array([value(r,'power_kW') for r in rows])
    return X, y, np.array([int(r['run']) for r in rows])
X, y, ids = arrays(rows)
assert X.shape == (10,2) and y.shape == (10,)
print(X.shape, y.shape, ids)
'''),
('2. Audit rows','Create a boolean valid mask of shape (10,). Here declare flow>0, pressure rise>0 and finite inputs/target. Print flagged IDs and reasons; this is a teaching screening rule, not a universal operating specification.',
'''def valid_rows(X,y):
    raise NotImplementedError('Check finite values and stated bounds')
valid = valid_rows(X,y)
print('Flagged IDs:', ids[~valid])
''',
'''def valid_rows(X,y):
    return np.isfinite(X).all(axis=1) & np.isfinite(y) & (X[:,0]>0) & (X[:,1]>0)
valid = valid_rows(X,y)
print('Flagged IDs:', ids[~valid])
for i in np.flatnonzero(~valid):
    reasons=[]
    if not np.isfinite(X[i]).all(): reasons.append('missing input')
    if np.isfinite(X[i,1]) and X[i,1]<=0: reasons.append('pressure rise violates declared screening rule')
    print(ids[i], '; '.join(reasons))
assert ids[~valid].tolist() == [4,6]
'''),
('3. A physics feature','For screened rows compute hydraulic power ΔpQ/1000 in kW, shape (n_valid,). Compare electrical measurements; do not interpret this as a fitted or validated efficiency model.',
'''def hydraulic_kw(X):
    raise NotImplementedError('Multiply pressure rise by flow and convert W to kW')
hydraulic = hydraulic_kw(X[valid])
print('hydraulic kW:', hydraulic)
''',
'''def hydraulic_kw(X): return X[:,0]*X[:,1]/1000
hydraulic = hydraulic_kw(X[valid])
print('hydraulic kW:', np.round(hydraulic,3))
print('measured electrical kW:', y[valid])
print('ratio hydraulic/electrical:', np.round(hydraulic/y[valid],3))
assert np.isclose(hydraulic[0],1.0)
''')],
'''## Report
State X/y shapes, units, flag reasons and two limitations. Explain why filling missing flow with a whole-dataset mean before an evaluation split would be questionable. Do not claim this synthetic CSV validates a real pump.
''')

lab('lab02','Fit and evaluate a pump-power model','Compare simple regression and a physical feature on independent synthetic operating designs. Use validation for selection and reserve a locked test.',[
code('''import sys
import numpy as np
print('Python', sys.version.split()[0], 'NumPy', np.__version__)
rng=np.random.default_rng(42)
n=150
flow=rng.uniform(0.006,0.035,n)
dp=rng.uniform(80000,200000,n)
X=np.column_stack([flow,dp])
y=flow*dp/0.72/1000 + rng.normal(0,0.12,n)
order=rng.permutation(n)
tr,va,te=order[:90],order[90:120],order[120:]
print('Independent synthetic designs. train/validation/test:',len(tr),len(va),len(te))
print('X units: m^3/s and Pa. y unit: kW.')
''')],[
('1. Fit a repeatable transform and model','Define fit_linear(A,b), returning training mean, safe training standard deviation and coefficients. A shape (n,d), b shape (n,). Build an intercept column and use np.linalg.lstsq. Define predict(model,A) returning (n,).',
'''def fit_linear(A,b):
    raise NotImplementedError('Fit training scaling and least-squares coefficients')
def predict(model,A):
    raise NotImplementedError('Apply stored transform; do not refit on new inputs')
''',
'''def fit_linear(A,b):
    mean=A.mean(axis=0); sd=A.std(axis=0)
    sd=np.where(sd>0,sd,1.0)
    Z=np.column_stack([np.ones(len(A)),(A-mean)/sd])
    coef=np.linalg.lstsq(Z,b,rcond=None)[0]
    return mean,sd,coef
def predict(model,A):
    mean,sd,coef=model
    return np.column_stack([np.ones(len(A)),(A-mean)/sd])@coef
'''),
('2. Compare on validation','Fit two candidates: raw X and physical feature H=flow*dp/1000 with shape (150,1). Compare validation MAE with a constant training-mean baseline. Select without using te.',
'''def choose_candidate(X,y,tr,va):
    raise NotImplementedError('Compare candidates on validation and return name/model/feature arrays')
chosen,model,A=choose_candidate(X,y,tr,va)
''',
'''def choose_candidate(X,y,tr,va):
    features={'raw':X,'hydraulic':(X[:,0]*X[:,1]/1000).reshape(-1,1)}
    results={}
    for name,A in features.items():
        m=fit_linear(A[tr],y[tr]); mae=np.mean(np.abs(y[va]-predict(m,A[va])))
        results[name]=(mae,m,A)
        print(name,'validation MAE kW:',round(mae,4))
    print('training-mean baseline validation MAE kW:',round(np.mean(np.abs(y[va]-y[tr].mean())),4))
    chosen=min(results,key=lambda k:results[k][0])
    _,model,A=results[chosen]
    print('Selected using validation:',chosen)
    return chosen,model,A
chosen,model,A=choose_candidate(X,y,tr,va)
'''),
('3. Locked test and metrics','Refit the selected specification on tr+va, then evaluate te once. Return MAE, RMSE and R². Handle SST=0 explicitly. Baselines use tr+va only. Residual means observation minus prediction.',
'''def metrics(y,p):
    raise NotImplementedError('Implement MAE, RMSE and R-squared with a constant-target rule')
dev=np.concatenate([tr,va])
locked=fit_linear(A[dev],y[dev])
p=predict(locked,A[te])
print(metrics(y[te],p))
''',
'''def metrics(y,p):
    r=y-p; sst=np.sum((y-y.mean())**2)
    return dict(MAE=float(np.abs(r).mean()), RMSE=float(np.sqrt((r*r).mean())),
                R2=float(1-np.sum(r*r)/sst) if sst>0 else None)
dev=np.concatenate([tr,va]); locked=fit_linear(A[dev],y[dev]); p=predict(locked,A[te])
print('Locked model test metrics:',metrics(y[te],p))
print('Training-mean baseline:',metrics(y[te],np.full(len(te),y[dev].mean())))
physics=X[te,0]*X[te,1]/0.72/1000
print('Known synthetic physics baseline:',metrics(y[te],physics))
assert np.isclose(metrics(np.array([1.,-2.,3.]),np.zeros(3))['MAE'],2.0)
assert metrics(np.ones(3),np.ones(3))['R2'] is None
print('Independent physical check: 100000 Pa * 0.02 m^3/s / 0.8 =',100000*0.02/0.8,'W')
''')],
'''## Report
Describe independent synthetic designs, split sizes, chosen features, validation choice, test metrics and baseline. Explain why this random split is not the default for forecasting or transfer across machines. State limitations; do not infer validated pump performance.
''')

lab('lab03','Evaluate a fault detector','Select a decision threshold on validation scores, then report a fixed test result and an always-healthy baseline. Scores are synthetic illustrative outputs, not a trained or calibrated detector.',[
code('''import sys
import numpy as np
print('Python',sys.version.split()[0],'NumPy',np.__version__)
val_scores=np.array([.10,.20,.35,.40,.55,.62,.70,.82,.90,.30,.65,.45])
val_labels=np.array([0,0,0,1,0,1,1,1,1,0,0,1])
test_scores=np.array([.05,.15,.28,.42,.48,.58,.68,.78,.92,.25,.72,.52])
test_labels=np.array([0,0,0,1,0,1,1,1,1,0,0,1])
print('Positive class = fault. Threshold rule: score >= threshold.')
''')],[
('1. Count outcomes','Return integer TP,FP,FN,TN for labels and predictions of shape (n,). Add precision and recall with None when the relevant denominator is zero.',
'''def counts(y,p):
    raise NotImplementedError('Count TP,FP,FN,TN')
def report(y,p):
    raise NotImplementedError('Compute metrics; state denominator rules')
''',
'''def counts(y,p):
    return dict(TP=int(np.sum((y==1)&(p==1))), FP=int(np.sum((y==0)&(p==1))),
                FN=int(np.sum((y==1)&(p==0))), TN=int(np.sum((y==0)&(p==0))))
def report(y,p):
    c=counts(y,p); tp,fp,fn,tn=(c[k] for k in ['TP','FP','FN','TN'])
    return dict(c,precision=tp/(tp+fp) if tp+fp else None,
                recall=tp/(tp+fn) if tp+fn else None,accuracy=(tp+tn)/len(y))
'''),
('2. Select a threshold','Teaching cost: missed fault costs 5 units, false alarm costs 1. Evaluate thresholds .3,.4,.5,.6,.7 on validation only. Tie rule: choose the lowest threshold. This cost is illustrative, not an approved machinery policy.',
'''def choose(scores,y):
    raise NotImplementedError('Minimize 5*FN+FP on validation; deterministic tie handling')
threshold=choose(val_scores,val_labels)
''',
'''def choose(scores,y):
    candidates=[]
    for t in [.3,.4,.5,.6,.7]:
        c=counts(y,(scores>=t).astype(int)); cost=5*c['FN']+c['FP']
        candidates.append((cost,t)); print('validation threshold',t,'cost',cost,c)
    return min(candidates)[1]
threshold=choose(val_scores,val_labels)
print('Selected threshold',threshold)
'''),
('3. Locked test and baseline','Report test outcomes using the selected threshold. Compare always-healthy predictions. Separately calculate accuracy and recall for 99 healthy and one missed fault.',
'''raise NotImplementedError('Evaluate the locked threshold and the always-healthy baseline')
''',
'''print('Test selected detector:',report(test_labels,(test_scores>=threshold).astype(int)))
print('Test always healthy:',report(test_labels,np.zeros(len(test_labels),dtype=int)))
rare=np.array([0]*99+[1]); baseline=report(rare,np.zeros(100,dtype=int))
print('Rare-fault example:',baseline)
assert baseline['accuracy']==.99 and baseline['recall']==0
assert report(np.array([1,1,0]),np.array([1,0,1]))['TP']==1
''')],
'''## Report
Explain class definitions, threshold selection, validation versus test roles, both baselines and cost assumptions. Explain why probabilities require calibration evidence and why synthetic scores cannot authorize machinery decisions.
''')

lab('lab04','Verify an AI-assisted engineering draft','Check a supplied illustrative draft against equations, units, known cases and source provenance. No AI service is called. Use your own permitted external assistant only as an optional extension.',[
md('''## Given task and illustrative draft
Given: area=20 m², irradiance=800 W/m², DC efficiency=0.20, inverter efficiency=0.96. Ignore temperature and other losses.

Draft for critique: “DC power is 3,200 kW; AC power is 3,072 kW. Therefore daily AC energy is 3,072 kWh. The unnamed standard guarantees this result.”

This deliberately flawed text is authored for teaching; it is not attributed to an actual AI platform.
'''),code('''import sys
import numpy as np
print('Python',sys.version.split()[0],'NumPy',np.__version__)
A,G,eta,eta_inv=20.,800.,.20,.96
''')],[
('1. Independent power check','Define dc_power_w(area,irradiance,efficiency). Reject negative area/irradiance and efficiency outside [0,1]. Return watts, then calculate AC watts.',
'''def dc_power_w(area,irradiance,efficiency):
    raise NotImplementedError('Check input bounds and calculate eta*A*G in watts')
dc=dc_power_w(A,G,eta); ac=eta_inv*dc
print('DC W',dc,'AC W',ac)
''',
'''def dc_power_w(area,irradiance,efficiency):
    if area<0 or irradiance<0 or not 0<=efficiency<=1: raise ValueError('Invalid input')
    return area*irradiance*efficiency
dc=dc_power_w(A,G,eta); ac=eta_inv*dc
print('DC W',dc,'AC W',ac)
assert dc==3200 and ac==3072
assert dc_power_w(20,0,.2)==0
assert dc_power_w(0,800,.2)==0
try: dc_power_w(20,800,1.2)
except ValueError: print('Invalid efficiency rejected')
else: raise AssertionError('Invalid efficiency was accepted')
'''),
('2. Energy needs time information','For a new explicit assumption of constant conditions for 2 hours only, compute AC energy in kWh. Do not call it actual daily energy. Explain what a real daily estimate needs.',
'''raise NotImplementedError('Compute energy for an explicitly assumed two-hour interval')
''',
'''hours=2.
energy_kwh=ac/1000*hours
print('Illustrative 2-hour energy under constant conditions:',energy_kwh,'kWh')
assert np.isclose(energy_kwh,6.144)
print('Daily energy is not determined by the original instantaneous input.')
'''),
('3. Verification record','Create a structured record separating correct equation, unit errors, missing time information and unsupported citation. Include whether any real system validation occurred.',
'''raise NotImplementedError('Create your verification record with evidence and limitations')
''',
'''record={
 'equation':'P_DC=eta*A*G, giving watts',
 'unit_error':'Draft uses kW where correct values are W (factor 1000)',
 'energy_limit':'Daily energy needs time-resolved conditions and losses',
 'source_status':'Unnamed standard has not been supplied or verified',
 'verification':'Known-case arithmetic and input checks passed',
 'validation':'No real-system validation; idealized synthetic calculation',
 'AI_use':'Illustrative authored draft; no external AI call in this reference'
}
for k,v in record.items(): print(k+':',v)
''')],
'''## Report and optional extension
Write a corrected answer, state assumptions and limitations, and explain verification versus validation. Optionally ask a permitted assistant the original task, save the actual prompt/output, and audit its claims. Do not upload restricted data. A correct output need not contain an error; report what you actually found rather than inventing one.
''')

ENV='''# AI 101 target environment (not a claim that every supported combination was executed)
# Python >=3.10; local JupyterLab is optional for the learner interface.
numpy>=1.26
jupyterlab>=4
# See AI_101_Validation.md for actual execution versions.
'''
