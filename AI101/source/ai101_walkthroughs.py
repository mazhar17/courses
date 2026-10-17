"""Optional 'Code' walkthroughs for AI 101 (static text shown on the course page).

Python never runs inside the course page. Learners read the code and the expected
output here, then run the same code in Google Colab or Jupyter from the notebook.

Each walkthrough is written only from material taught in that module or earlier.
Expected outputs are written by hand and re-checked by test_walkthroughs.py, which
executes the code and compares stdout exactly.
"""
from ai101_notebooks import nb, md, code

REPO_COLAB = 'https://colab.research.google.com/github/mazhar17/courses/blob/main/AI101/AI_101_notebooks/'
NOTEBOOK_DIR = 'AI_101_notebooks/'

POINTS_TABLE = '''Point  Δp (kPa)  Q (m³/s)  Measured input power (W)
A           100     0.020                      2800
B            80     0.015                      1650
C           120     0.025                      3950'''

WALKTHROUGHS = {
 'm02': dict(
  title='Pump power: physics prediction and residual',
  supports='Lesson 2.1 (sections “Pump-power example” and “Residual correction”) and Lesson 2.3 (section “Hybrid pump example”). Lesson 2.2 is used for the caution about causes.',
  objective='Reproduce the Lesson 2.3 pump example in Python: calculate hydraulic power, predicted input power and the residual. Then see how the size and sign of a residual depend on the efficiency you assume.',
  prereqs=[
   'You need Module 1 and Lessons 2.1 to 2.3. You do not need earlier Python experience.',
   'To run the code, open it in Google Colab (you sign in with a Google account) or download the notebook and use Jupyter. Reading this page needs neither.',
  ],
  python_ideas=[
   'A variable is a name that stores a value. In `q = 0.02`, the name `q` stores the number 0.02.',
   'A line that starts with `#` is a comment. Python ignores it. It is a note for people.',
   '`print(...)` shows a result below the code.',
   'An f-string is text that starts with `f"` and can contain values inside braces. In `{x:.1f}`, the `.1f` means “one digit after the decimal point”. In `{x:+.1f}`, the `+` also shows the sign.',
   'A list holds several items in order. A `for` loop repeats the same steps once for each item.',
   '`if` and `else` choose between two messages.',
  ],
  example=[
   'Lesson 2.3 gives one operating point: Δp = 100 kPa, Q = 0.02 m³/s, efficiency η = 0.8 and a measured input power of 2,800 W. You will check the lesson’s numbers first. Then you will repeat the same calculation for three operating points.',
   'The three points below are synthetic. They were invented for teaching. They are not measurements from a real pump. Point A is the worked example from Lesson 2.3.',
  ],
  data_table=POINTS_TABLE,
  steps=[
   dict(
    heading='Step 1. Convert the pressure unit',
    explain='Lesson 2.1 uses pressure rise Δp in pascals (Pa). The example gives 100 kPa. One kilopascal is 1,000 pascals, so you convert first.',
    code='''# Step 1: convert kilopascals (kPa) to pascals (Pa)
dp_kpa = 100              # pressure rise in kPa
dp_pa = dp_kpa * 1000     # 1 kPa = 1000 Pa
print(f"Pressure rise: {dp_pa} Pa")''',
    expected_output='Pressure rise: 100000 Pa',
    output_explain='100 kPa is 100,000 Pa. This matches Lesson 2.1. Without this step, the result would be wrong by a factor of 1,000.'),
   dict(
    heading='Step 2. Calculate hydraulic power',
    explain='The relationship is P_h = Δp × Q. Pa × m³/s gives W, so the unit works out to watts.',
    code='''# Step 2: hydraulic power, P_h = delta p × Q
q = 0.02                  # volumetric flow rate in m³/s
p_hydraulic = dp_pa * q   # Pa × m³/s = W
print(f"Hydraulic power: {p_hydraulic:.1f} W")''',
    expected_output='Hydraulic power: 2000.0 W',
    output_explain='This matches the 2,000 W in Lesson 2.1.'),
   dict(
    heading='Step 3. Predict the input power',
    explain='Lesson 2.1 states the input-power relationship P_in = P_h / η. Here η is efficiency. It has no unit. Use η = 0.8, as in the lesson. This is an idealized relationship with one fixed efficiency.',
    code='''# Step 3: predicted input power, P_in = P_h / efficiency
efficiency = 0.8          # dimensionless
p_input_pred = p_hydraulic / efficiency
print(f"Predicted input power: {p_input_pred:.1f} W")''',
    expected_output='Predicted input power: 2500.0 W',
    output_explain='This matches the 2,500 W in Lessons 2.1 and 2.3. Hydraulic power (2,000 W) and input power (2,500 W) are different quantities. They are different because of the assumed efficiency.'),
   dict(
    heading='Step 4. Calculate the residual',
    explain='Lesson 2.1 defines the residual as r = y − ŷ, which is the measured value minus the predicted value. Here y is the measured input power of 2,800 W and ŷ is the prediction from Step 3.',
    code='''# Step 4: residual = measured - predicted
p_measured = 2800         # measured input power in W (from the lesson)
residual = p_measured - p_input_pred
print(f"Residual: {residual:+.1f} W")

if residual > 0:
    print("The measurement is above the prediction.")
else:
    print("The measurement is at or below the prediction.")''',
    expected_output='''Residual: +300.0 W
The measurement is above the prediction.''',
    output_explain='r = +300 W, as in Lesson 2.3. A positive residual means the physics prediction is below the measurement. The residual shows a discrepancy. As Lesson 2.1 says, it does not by itself prove the physical cause.'),
   dict(
    heading='Step 5. Repeat for three operating points',
    explain='Now you repeat Steps 1 to 4 for three synthetic points. Each point is a group of four values inside round brackets: a name, Δp in kPa, Q in m³/s and the measured input power in W. The `for` loop takes the points one at a time. The unit conversion is now written inside the loop.',
    code='''# Step 5: the same calculation for three synthetic operating points
efficiency = 0.8          # dimensionless; you will change this later

points = [
    ("A", 100, 0.020, 2800),
    ("B",  80, 0.015, 1650),
    ("C", 120, 0.025, 3950),
]

print("Point  P_hyd (W)  P_in (W)  Measured (W)  Residual (W)")
for name, dp_kpa, q, p_measured in points:
    p_hydraulic = dp_kpa * 1000 * q
    p_input_pred = p_hydraulic / efficiency
    residual = p_measured - p_input_pred
    print(f"{name:<7}{p_hydraulic:>9.1f}{p_input_pred:>10.1f}{p_measured:>14.1f}{residual:>14.1f}")''',
    expected_output='''Point  P_hyd (W)  P_in (W)  Measured (W)  Residual (W)
A         2000.0    2500.0        2800.0         300.0
B         1200.0    1500.0        1650.0         150.0
C         3000.0    3750.0        3950.0         200.0''',
    output_explain='Point A repeats the lesson example. At all three synthetic points the measured power is above the prediction, so every residual is positive. This only suggests that the simple model leaves something out. It does not show why. Three invented points also say nothing about a real pump.'),
  ],
  try_it=dict(
   instruction='Change a value and observe. In the Step 5 code, change `efficiency = 0.8` to `efficiency = 0.75`. Then run the cell again.',
   change=('efficiency = 0.8          # dimensionless; you will change this later',
           'efficiency = 0.75         # dimensionless; you will change this later'),
   expected_output='''Point  P_hyd (W)  P_in (W)  Measured (W)  Residual (W)
A         2000.0    2666.7        2800.0         133.3
B         1200.0    1600.0        1650.0          50.0
C         3000.0    4000.0        3950.0         -50.0''',
   expected_observation='All three residuals get smaller. Point C changes from +200 W to −50 W, so its sign flips. You changed one assumption and the residuals changed. A residual depends on the physics assumptions as well as on the measurement. A hybrid model that learns residuals learns a correction to the baseline you chose.'),
  limits=[
   'The example uses one fixed efficiency and steady operation. Real pump efficiency changes with the operating point.',
   'The data are synthetic and have no measurement uncertainty. Nothing here validates a real pump or real equipment.',
   'Lesson 2.1 says that hydraulic, shaft and electrical power are different quantities. This example only follows the lesson’s “input power”.',
   'The code only calculates residuals. It does not fit or train a model. Fitting a model starts in Module 7 and in Lab 2.',
  ],
  related='Lab 2 (Module 7) uses a physical quantity such as hydraulic power as an input to a fitted regression model.',
  notebook='walkthrough_m02.ipynb'),
}


def step_code(w, upto=None):
    """Return the list of code strings for the walkthrough steps."""
    return [s['code'] for s in w['steps'][:upto]]


def notebook_for(module_id):
    w = WALKTHROUGHS[module_id]
    cells = [md('# ' + w['title'] + '\n\n**Optional code walkthrough for AI 101 (Module ' + str(int(module_id[1:])) + ').** Not graded. Quiz scores do not depend on it.\n\n**Objective.** ' + w['objective'] + '\n\n**Supports.** ' + w['supports'] + '\n\nRun the cells from top to bottom. All data are synthetic and invented for teaching.\n')]
    cells.append(md('## About the data\n\n' + '\n\n'.join(w['example']) + '\n\n```\n' + w['data_table'] + '\n```\n'))
    for s in w['steps']:
        cells.append(md('## ' + s['heading'] + '\n\n' + s['explain']))
        cells.append(code(s['code']))
        cells.append(md('**Expected output**\n\n```\n' + s['expected_output'] + '\n```\n\n' + s['output_explain']))
    t = w['try_it']
    cells.append(md('## Try it\n\n' + t['instruction'] + '\n\n**Expected result**\n\n```\n' + t['expected_output'] + '\n```\n\n' + t['expected_observation']))
    cells.append(md('## Limits\n\n' + '\n'.join('- ' + x for x in w['limits']) + '\n\n' + w['related']))
    return nb(w['title'], cells)


def public_data():
    """Data embedded in the course page (no code is executed there)."""
    out = {}
    for k, w in WALKTHROUGHS.items():
        d = {x: w[x] for x in ['title', 'supports', 'objective', 'prereqs', 'python_ideas', 'example', 'data_table', 'steps', 'limits', 'related', 'notebook']}
        d['try_it'] = {'instruction': w['try_it']['instruction'], 'expected_output': w['try_it']['expected_output'], 'expected_observation': w['try_it']['expected_observation']}
        d['colab'] = REPO_COLAB + w['notebook']
        d['download'] = NOTEBOOK_DIR + w['notebook']
        out[k] = d
    return out
