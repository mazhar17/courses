"""Code walkthroughs for Modules 14, 15 and 16 (batch D)."""

W = {}

W['m14'] = dict(
 title='Check an AI-assisted photovoltaic estimate',
 supports='Lesson 14.1 (sections “Verify a photovoltaic power estimate” and “Keep power and energy distinct”).',
 objective='Calculate the photovoltaic (PV) power of Lesson 14.1 yourself. Use the result to catch a factor-of-1,000 unit error in a claimed answer. Then see why one power value cannot give daily energy.',
 prereqs=[
  'You need Lessons 14.1 to 14.3 and the earlier code walkthroughs. They introduce variables, `if` and `else`, f-strings and `for` loops.',
  'Run the code in Google Colab or Jupyter. This walkthrough uses plain Python only. It calls no AI service.',
 ],
 python_ideas=[
  '`a / b` divides a by b. `a * b` multiplies. You used both in the Module 2 walkthrough.',
  'In an f-string, `{value:.3f}` shows three digits after the decimal point, as in the Module 7 walkthrough.',
 ],
 example=[
  'The illustrative array of Lesson 14.1 has area A = 20 m², irradiance G = 800 W/m², module efficiency 0.20 and inverter efficiency 0.96. The simplified model is P_DC = η A G and P_AC = η_inv P_DC.',
  'Suppose an assistant answers “3,200 kW”. You check that claim. The numbers are an authored teaching case. They are not from real equipment.',
 ],
 data_table='''Area A:                    20 m²
Irradiance G:              800 W/m²
Module efficiency:         0.20  (dimensionless)
Inverter efficiency:       0.96  (dimensionless)
Claim to check:            3200 kW''',
 steps=[
  dict(
   heading='Step 1. Calculate the DC power yourself',
   explain='Do your own calculation before you trust an answer. The unit check comes first: m² × W/m² gives W. The efficiencies have no unit.',
   code='''# Step 1: P_DC = efficiency * area * irradiance
efficiency = 0.20         # dimensionless
area = 20                 # m²
irradiance = 800          # W/m²
p_dc = efficiency * area * irradiance   # W
print(f"DC power: {p_dc:.1f} W")
print(f"DC power: {p_dc / 1000:.1f} kW")''',
   expected_output='''DC power: 3200.0 W
DC power: 3.2 kW''',
   output_explain='This matches Lesson 14.1: 3,200 W, which is 3.2 kW. Dividing by 1,000 converts watts to kilowatts.'),
  dict(
   heading='Step 2. Calculate the AC power',
   explain='The inverter converts DC to AC. With inverter efficiency 0.96 the simplified AC estimate is P_AC = η_inv P_DC.',
   code='''# Step 2: P_AC = inverter efficiency * P_DC
inverter_efficiency = 0.96   # dimensionless
p_ac = inverter_efficiency * p_dc
print(f"AC power: {p_ac:.1f} W")
print(f"AC power: {p_ac / 1000:.3f} kW")''',
   expected_output='''AC power: 3072.0 W
AC power: 3.072 kW''',
   output_explain='This matches Lesson 14.1: 3,072 W, which is 3.072 kW. The estimate is simplified. It ignores temperature effects and other losses.'),
  dict(
   heading='Step 3. Test a claimed answer',
   explain='Suppose an assistant writes “P_DC = 3,200 kW”. Convert the claim to watts and compare it with your own result. A ratio near 1,000 points to a unit error.',
   code='''# Step 3: compare a claimed value with your own calculation
claimed_kw = 3200
claimed_w = claimed_kw * 1000     # 1 kW = 1000 W
ratio = claimed_w / p_dc
print(f"Claimed DC power: {claimed_w} W")
print(f"Ratio claimed / calculated: {ratio:.1f}")
if ratio > 100 or ratio < 0.01:
    print("The claim is off by a large factor. Check the units first.")
else:
    print("The claim is the same order of magnitude as the calculation.")''',
   expected_output='''Claimed DC power: 3200000 W
Ratio claimed / calculated: 1000.0
The claim is off by a large factor. Check the units first.''',
   output_explain='The claim has the right digits but the wrong unit. It is 1,000 times too large, as Lesson 14.1 explains. A fluent answer can contain a correct-looking number with the wrong unit. This check only finds the large unit error. A claim that is close but wrong would pass it.'),
  dict(
   heading='Step 4. Power is not energy',
   explain='Energy is the time integral of power. Lesson 14.1 allows one explicitly illustrative calculation: constant power for two hours only. It must not be presented as a daily yield. Energy in kWh is power in kW times time in hours.',
   code='''# Step 4: energy under an explicit constant-power assumption
p_ac_kw = p_ac / 1000     # kW
hours = 2                 # stated duration, constant power assumed
energy_kwh = p_ac_kw * hours
print(f"Energy in {hours} h at constant power: {energy_kwh:.3f} kWh")
print("This is not a daily yield. A daily value needs a time profile.")''',
   expected_output='''Energy in 2 h at constant power: 6.144 kWh
This is not a daily yield. A daily value needs a time profile.''',
   output_explain='3.072 kW × 2 h = 6.144 kWh, as in Lesson 14.1. The result is valid only for the two stated hours and the constant-power assumption. Sunshine changes during the day. One power value cannot give daily energy.'),
 ],
 try_it=dict(
  instruction='Change a value and observe. In Step 4, change `hours = 2` to `hours = 3`. Then run the cell again.',
  change=('hours = 2                 # stated duration, constant power assumed', 'hours = 3                 # stated duration, constant power assumed'),
  expected_output='''Energy in 3 h at constant power: 9.216 kWh
This is not a daily yield. A daily value needs a time profile.''',
  expected_observation='Energy grows in proportion to the duration: 3.072 kW × 3 h = 9.216 kWh. The assumption that power stays constant for three hours is now less realistic. A longer duration does not make the estimate more correct.'),
 limits=[
  'The model is a simplified teaching case. It has no temperature effect, shading or other losses.',
  'The numbers are authored for teaching. Nothing here shows the performance of real equipment.',
  'The checks in this walkthrough find unit and arithmetic errors. They do not check the physical assumptions or the source of the numbers.',
  'The code calls no AI assistant. Use your own permitted assistant only as an optional extension, and check its answer in the same way.',
 ],
 related='Lab 4 (Module 14) checks a supplied illustrative draft against equations, units, known cases and source provenance. This walkthrough shows the same habit on one calculation.',
 notebook='walkthrough_m14.ipynb')

W['m15'] = dict(
 title='Verification checks and an input-range warning',
 supports='Lesson 15.1 (sections “Operating coverage is more than input bounds” and “Distribution shift and drift”) and Lesson 15.2 (sections “Verification: did we implement the method correctly?” and “Validation: does it represent the real system?”).',
 objective='Write a small automatic known-case test and use it to catch a unit bug. Then check whether a new operating point is covered by the training conditions, and raise a warning when recent inputs leave the development range.',
 prereqs=[
  'You need Lessons 15.1 to 15.3 and the earlier code walkthroughs. They introduce variables, lists, tuples, `def`, `abs`, `if`, `for` loops and f-strings.',
  'Run the code in Google Colab or Jupyter. This walkthrough uses plain Python only.',
 ],
 python_ideas=[
  '`def check(name, got, expected):` defines a function with three inputs. It prints PASS or FAIL.',
  '`a and b` is true only when both a and b are true. `min(items)` and `max(items)` give the smallest and the largest number in a list.',
  '`count += 1` adds 1 to a counter. It means `count = count + 1`.',
 ],
 example=[
  'The first example uses the pump power relationship of Lesson 15.2, P = Δp × Q, with the values of the Module 2 example: 100 kPa and 0.02 m³/s give 2,000 W.',
  'The second and third examples use invented pump operating conditions: flow rate Q in m³/s and pressure rise Δp in kPa. All data are synthetic and are not from real equipment.',
 ],
 data_table='''Training operating points (synthetic): Q (m³/s), delta p (kPa)
0.010   60
0.012   70
0.020   95
0.028  120
0.030  130''',
 steps=[
  dict(
   heading='Step 1. A known-case test',
   explain='Lesson 15.2 says verification uses known cases, dimensional analysis and bounds. Here you write the function `check`. It compares a result with an expected value and prints PASS or FAIL. Then you test a hydraulic power function with a known case and with a scaling rule.',
   code='''# Step 1: verification with known cases
def check(name, got, expected):
    if abs(got - expected) < 1e-9:
        print(f"PASS: {name}")
    else:
        print(f"FAIL: {name} (got {got}, expected {expected})")

def hydraulic_power(dp_kpa, q):
    return dp_kpa * 1000 * q      # kPa -> Pa, then Pa * m³/s = W

check("100 kPa and 0.02 m³/s give 2000 W", hydraulic_power(100, 0.02), 2000)
check("doubling the flow doubles the power", hydraulic_power(100, 0.04), 2 * hydraulic_power(100, 0.02))''',
   expected_output='''PASS: 100 kPa and 0.02 m³/s give 2000 W
PASS: doubling the flow doubles the power''',
   output_explain='Both tests pass. The first is a known case from the Module 2 example. The second is a scaling rule: power is proportional to flow. Passing shows that the function implements the intended equation. It does not show that the equation represents a real pump.'),
  dict(
   heading='Step 2. Catch a unit bug',
   explain='Now a version of the function forgets the conversion from kilopascals to pascals. The same known case should reveal the bug.',
   code='''# Step 2: the known case catches a bug
def hydraulic_power_buggy(dp_kpa, q):
    return dp_kpa * q             # forgot kPa -> Pa

check("buggy function, known case", hydraulic_power_buggy(100, 0.02), 2000)''',
   expected_output='FAIL: buggy function, known case (got 2.0, expected 2000)',
   output_explain='The test fails because the result is 1,000 times too small. Without the known case, the bug could have stayed hidden. The same function would also give the same wrong answer every time. Reproducibility is not correctness (Lesson 15.2).'),
  dict(
   heading='Step 3. Is a new point covered by the training data?',
   explain='Lesson 15.1 says that a point can be inside the minimum and maximum of each input and still be unrepresentative. Here you check two things for each new point: whether each input is within its training range, and how many training points lie nearby. “Nearby” here means within 0.005 m³/s and within 10 kPa. This closeness rule is an invented example, not a standard.',
   code='''# Step 3: inside each input range, but is the combination covered?
train_points = [(0.010, 60), (0.012, 70), (0.020, 95), (0.028, 120), (0.030, 130)]
q_values = []
dp_values = []
for q, dp in train_points:
    q_values.append(q)
    dp_values.append(dp)

new_points = [("P1", 0.011, 65), ("P2", 0.030, 60)]
for name, q, dp in new_points:
    inside = (min(q_values) <= q and q <= max(q_values)
              and min(dp_values) <= dp and dp <= max(dp_values))
    near = 0
    for train_q, train_dp in train_points:
        if abs(q - train_q) <= 0.005 and abs(dp - train_dp) <= 10:
            near += 1
    if inside and near > 0:
        print(f"{name}: inside each input range; {near} nearby training points -> covered")
    elif inside:
        print(f"{name}: inside each input range; {near} nearby training points -> not covered, treat as extrapolation")
    else:
        print(f"{name}: outside an input range -> extrapolation")''',
   expected_output='''P1: inside each input range; 2 nearby training points -> covered
P2: inside each input range; 0 nearby training points -> not covered, treat as extrapolation''',
   output_explain='Both points are inside the training range of each input. But P2 combines the largest flow with the smallest pressure rise. No training point is near that combination. A check of each input alone would have accepted P2. Define the operating domain by the combinations that were actually observed.'),
  dict(
   heading='Step 4. Warn when recent inputs leave the development range',
   explain='Lesson 15.1 says to monitor input ranges and compare them with the development conditions. An input change is a warning signal. It is not proof that accuracy has dropped. Here you count recent flow readings that lie outside the development range of 0.010 to 0.030 m³/s.',
   code='''# Step 4: a simple input-range monitor
dev_min = 0.010           # m³/s, from the development data
dev_max = 0.030           # m³/s
recent = [0.012, 0.026, 0.034, 0.036]    # new flow readings, synthetic

outside = 0
for q in recent:
    if q < dev_min or q > dev_max:
        outside += 1

print(f"Readings outside the development range: {outside} of {len(recent)}")
if outside > 0:
    print("Warning signal: the inputs have moved. This does not prove the accuracy has dropped.")
    print("Next: check outcomes when trustworthy labels are available.")''',
   expected_output='''Readings outside the development range: 2 of 4
Warning signal: the inputs have moved. This does not prove the accuracy has dropped.
Next: check outcomes when trustworthy labels are available.''',
   output_explain='Two of the four readings are outside the range seen in development. The model may now be extrapolating. The check does not say whether the predictions are wrong. It tells you to look. Decide the action rules in advance, as the lesson says.'),
 ],
 try_it=dict(
  instruction='Change a value and observe. In Step 4, change the list to `recent = [0.012, 0.026, 0.024, 0.036]`. Then run the cell again.',
  change=('recent = [0.012, 0.026, 0.034, 0.036]', 'recent = [0.012, 0.026, 0.024, 0.036]'),
  expected_output='''Readings outside the development range: 1 of 4
Warning signal: the inputs have moved. This does not prove the accuracy has dropped.
Next: check outcomes when trustworthy labels are available.''',
  expected_observation='Only one reading is now outside the range, and the warning still appears. Any reading outside the range raises the warning. A real monitor would also use a rule for how many readings and how long, and that rule must be decided in advance.'),
 limits=[
  'The data are synthetic. The coverage rule in Step 3 and the range check in Step 4 are simple teaching examples, not standards.',
  'Passing a known-case test is verification. It is not validation. Validation needs independent, calibrated measurements from the real system (Lesson 15.2).',
  'The code does not measure calibration, drift in accuracy or uncertainty. It only checks implementation and input ranges.',
  'Real operating domains have more than two inputs, and the closeness rule would need justification for each.',
 ],
 related='Lab 4 (Module 14) uses known cases and unit checks on a supplied draft. This walkthrough adds coverage and input-range warnings.',
 notebook='walkthrough_m15.ipynb')

W['m16'] = dict(
 title='Screen candidates, then check constraints on the original',
 supports='Lesson 16.1 (sections “Surrogates accelerate search, not sign-off” and “Objectives and constraints answer different questions”).',
 objective='Use predicted values to screen five design candidates. Check an objective and two constraints separately. Then re-check the chosen candidate with the original calculation, as Lesson 16.1 requires.',
 prereqs=[
  'You need Lessons 16.1 to 16.3 and the earlier code walkthroughs. They introduce variables, lists, tuples, `for` loops, `if`, f-strings and `.append`.',
  'Run the code in Google Colab or Jupyter. This walkthrough uses plain Python only. It does not build a surrogate model.',
 ],
 python_ideas=[
  '`", ".join(items)` joins a list of text items into one text, with a comma and a space between them.',
  'In an f-string, `{value:+.0f}` shows a number with its sign and no decimal digits. You met `+` in the Module 2 walkthrough.',
  '`len(items) == 0` is true when the list is empty.',
 ],
 example=[
  'Five invented pump design candidates were screened by a surrogate. The surrogate gives a predicted electrical power, a predicted flow rate and a predicted maximum stress for each. The objective is low power. The constraints are a flow of at least 0.015 m³/s and a stress of at most 120 MPa.',
  'All numbers are synthetic and were invented for teaching. The surrogate values and the “original simulation” values are not from real equipment. The code does not build a surrogate. It only checks its predictions.',
 ],
 data_table='''Candidate  Predicted power (W)  Predicted flow (m³/s)  Predicted stress (MPa)
A                 2400                 0.016                     110
B                 2100                 0.013                     100
C                 2250                 0.017                     125
D                 2300                 0.018                     115
E                 2600                 0.020                      90''',
 steps=[
  dict(
   heading='Step 1. Choose by the objective alone',
   explain='The objective is the lowest predicted power. First look at what happens when you use only the objective. The code keeps the best candidate seen so far.',
   code='''# Step 1: lowest predicted power, ignoring the constraints
candidates = [
    ("A", 2400, 0.016, 110),
    ("B", 2100, 0.013, 100),
    ("C", 2250, 0.017, 125),
    ("D", 2300, 0.018, 115),
    ("E", 2600, 0.020,  90),
]   # (name, power in W, flow in m³/s, stress in MPa), all predicted

best = candidates[0]
for c in candidates:
    if c[1] < best[1]:
        best = c
print(f"Lowest predicted power: {best[0]} at {best[1]} W")''',
   expected_output='Lowest predicted power: B at 2100 W',
   output_explain='Candidate B has the lowest predicted power. Do not accept it yet. The objective says what you want. The constraints say what is allowed.'),
  dict(
   heading='Step 2. Check each constraint separately',
   explain='Lesson 16.1 says that a candidate with an attractive objective can still be infeasible. Check the flow and the stress separately, with their units. A candidate is feasible only if it satisfies all constraints.',
   code='''# Step 2: constraint check for every candidate
min_flow = 0.015          # m³/s
max_stress = 120          # MPa

feasible = []
for name, power, flow, stress in candidates:
    reasons = []
    if flow < min_flow:
        reasons.append("flow below limit")
    if stress > max_stress:
        reasons.append("stress above limit")
    if len(reasons) == 0:
        feasible.append((name, power, flow, stress))
        print(name, "feasible")
    else:
        print(name, "not feasible:", ", ".join(reasons))''',
   expected_output='''A feasible
B not feasible: flow below limit
C not feasible: stress above limit
D feasible
E feasible''',
   output_explain='Candidate B, the best by the objective, violates the flow limit. Candidate C violates the stress limit. Only A, D and E are in the feasible design space.'),
  dict(
   heading='Step 3. Choose the best feasible candidate',
   explain='Now apply the objective again, but only to the feasible candidates.',
   code='''# Step 3: best predicted power among the feasible candidates
best = feasible[0]
for c in feasible:
    if c[1] < best[1]:
        best = c
print(f"Best feasible candidate by predicted power: {best[0]} at {best[1]} W")''',
   expected_output='Best feasible candidate by predicted power: D at 2300 W',
   output_explain='Candidate D is the best feasible candidate according to the surrogate. This is only a prediction. The surrogate helps you screen. It does not sign off a design.'),
  dict(
   heading='Step 4. Re-check the chosen candidate with the original',
   explain='Lesson 16.1 says to re-evaluate promising candidates with the original simulation or experiment. Here the “original” values for candidate D are invented numbers. Compare the power using the course convention r = y − ŷ, where y is the original value. Then check both constraints again with the original values.',
   code='''# Step 4: re-evaluate candidate D with the original calculation (synthetic values)
original_power = 2380     # W
original_flow = 0.0175    # m³/s
original_stress = 118     # MPa

predicted_power = best[1]
residual = original_power - predicted_power
print(f"Original power: {original_power} W; surrogate predicted: {predicted_power} W")
print(f"Residual (original - predicted): {residual:+.0f} W")

if original_flow >= min_flow:
    print("Flow constraint with original value: satisfied")
else:
    print("Flow constraint with original value: violated")

if original_stress <= max_stress:
    print(f"Stress constraint with original value: satisfied (margin {max_stress - original_stress} MPa)")
else:
    print(f"Stress constraint with original value: violated (over the limit by {original_stress - max_stress} MPa)")''',
   expected_output='''Original power: 2380 W; surrogate predicted: 2300 W
Residual (original - predicted): +80 W
Flow constraint with original value: satisfied
Stress constraint with original value: satisfied (margin 2 MPa)''',
   output_explain='The surrogate under-predicted the power by 80 W and under-predicted the stress by 3 MPa. The original values still satisfy both constraints, but the stress margin is only 2 MPa. This check is verification against the original calculation. It is not physical validation. It does not authorize a hardware claim.'),
 ],
 try_it=dict(
  instruction='Change a value and observe. In Step 2, change `max_stress = 120` to `max_stress = 115`. Then run Step 2, Step 3 and Step 4 again, in this order.',
  change=('max_stress = 120          # MPa', 'max_stress = 115          # MPa'),
  step=1,
  expected_output='''A feasible
B not feasible: flow below limit
C not feasible: stress above limit
D feasible
E feasible
Best feasible candidate by predicted power: D at 2300 W
Original power: 2380 W; surrogate predicted: 2300 W
Residual (original - predicted): +80 W
Flow constraint with original value: satisfied
Stress constraint with original value: violated (over the limit by 3 MPa)''',
  expected_observation='Candidate D passes the screening, because its predicted stress is exactly 115 MPa. But the original value is 118 MPa, so D violates the tighter limit. The surrogate would have passed a candidate that the original calculation rejects. This is why promising candidates must be re-checked.'),
 limits=[
  'All numbers are synthetic. The “original” values are invented. They are not from a simulation or a real pump.',
  'The code does not build or train a surrogate. It checks predicted values against constraints and against given original values.',
  'One re-check of one candidate shows nothing about the accuracy of the surrogate elsewhere. A surrogate is supported only where its training evidence covers the inputs.',
  'Passing a constraint check on the original calculation is verification, not physical validation on real hardware.',
 ],
 related='Lesson 16.2 describes a mini-project with a baseline, a split and an independent physical check. This walkthrough practises only the objective, constraint and re-check habit of Lesson 16.1.',
 notebook='walkthrough_m16.ipynb')
