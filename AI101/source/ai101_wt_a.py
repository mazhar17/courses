"""Code walkthroughs for Modules 3, 4 and 5 (batch A). Module 1 has no code walkthrough (see PR notes)."""

W = {}

W['m03'] = dict(
 title='Read a pump table as X and y',
 supports='Lesson 3.1 (sections “Read each row as an example”, “Separate features from targets” and “Preserve row alignment”) and Lesson 3.3 (section “Check when information becomes available”).',
 objective='Turn a small pump table into a feature matrix X and a target array y. Check their shapes, check that each row stays aligned with its target, and check that every feature exists at decision time.',
 prereqs=[
  'You need Lessons 3.1 to 3.3 and the Module 2 Code walkthrough, which introduces variables, lists, `for` loops and f-strings.',
  'Run the code in Google Colab or Jupyter. NumPy is already installed in Colab.',
 ],
 python_ideas=[
  '`import numpy as np` loads NumPy, a library for working with arrays of numbers. We call it `np` for short.',
  '`np.array(rows)` turns a list of lists into an array. `X.shape` gives its shape as (rows, columns). `X.size` gives the total number of values.',
  '`some_list.append(item)` adds one item to the end of a list.',
  'A tuple such as `("flow", True)` groups values in round brackets. A `for` loop can take them apart: `for name, ok in pairs:`.',
 ],
 example=[
  'Lesson 3.1 uses a pump table in which one row is one steady operating test. The columns are flow rate, pressure rise, shaft speed and measured electrical power. Here you build a table with four tests.',
  'The four tests are synthetic. They were invented for teaching and are not measurements from a real pump.',
 ],
 data_table='''Test  Q (m³/s)  Δp (Pa)  Speed (rad/s)  Measured power (W)
T1      0.020   100000            150                2800
T2      0.015    80000            130                1650
T3      0.025   120000            170                3950
T4      0.018    90000            140                2100''',
 steps=[
  dict(
   heading='Step 1. Store the table, with units in the names',
   explain='Each test is one group of five values: the test identifier, flow rate, pressure rise, shaft angular speed and measured power. The units are written in the comments, so the numbers keep their meaning (Lesson 3.2).',
   code='''# Step 1: the table, one tuple per test (synthetic data)
# (test id, Q in m³/s, pressure rise in Pa, speed in rad/s, power in W)
tests = [
    ("T1", 0.020, 100000, 150, 2800),
    ("T2", 0.015,  80000, 130, 1650),
    ("T3", 0.025, 120000, 170, 3950),
    ("T4", 0.018,  90000, 140, 2100),
]
print("Number of tests:", len(tests))''',
   expected_output='Number of tests: 4',
   output_explain='`len(tests)` counts the items in the list. There are four samples, one per row.'),
  dict(
   heading='Step 2. The shapes in Lesson 3.1',
   explain='Lesson 3.1 says X has shape (n, d) and y has shape (n,). Its example has 120 tests and three features. You can check the lesson’s numbers with plain arithmetic.',
   code='''# Step 2: the lesson's numbers, 120 tests and 3 features
n = 120                   # number of samples (rows)
d = 3                     # number of features (columns)
print("X has shape:", (n, d))
print("y has shape:", (n,))
print("Feature values in X:", n * d)''',
   expected_output='''X has shape: (120, 3)
y has shape: (120,)
Feature values in X: 360''',
   output_explain='This matches Lesson 3.1: 120 × 3 = 360 feature values and 120 target values. The comma in `(n,)` shows that y has one dimension, with n values.'),
  dict(
   heading='Step 3. Which columns may be features?',
   explain='Lesson 3.3 says a valid predictor must exist when the decision is made. Suppose you want to predict the power for a planned operating point. Flow rate, pressure rise and shaft speed are set or known beforehand. The measured power is the target. A repair code that is only written after a failure is not available beforehand. The list below is invented for teaching.',
   code='''# Step 3: is each column available at decision time?
columns = [
    ("flow rate", True),
    ("pressure rise", True),
    ("shaft speed", True),
    ("repair code written after a failure", False),
]

for name, available in columns:
    if available:
        print("can be a feature:   ", name)
    else:
        print("NOT a valid feature:", name)''',
   expected_output='''can be a feature:    flow rate
can be a feature:    pressure rise
can be a feature:    shaft speed
NOT a valid feature: repair code written after a failure''',
   output_explain='A column can be physically meaningful and still invalid for prediction because it appears too late. This check is a thinking aid. Only you can decide, from the engineering question, what is available.'),
  dict(
   heading='Step 4. Build X and y and keep the rows aligned',
   explain='Now you split each test into features and a target. The `for` loop handles one test at a time, so the features and the target in the same position always come from the same test. Then you turn the two lists into NumPy arrays.',
   code='''# Step 4: build X (features) and y (target), then check shapes and alignment
import numpy as np

X_rows = []               # one list of features per test
y_values = []             # one target per test
for test_id, q, dp, speed, power in tests:
    X_rows.append([q, dp, speed])
    y_values.append(power)

X = np.array(X_rows)
y = np.array(y_values)
print("X shape:", X.shape)
print("y shape:", y.shape)
print("Values in X:", X.size)
print("Row 2 of X:", X[2], "-> target", y[2])''',
   expected_output='''X shape: (4, 3)
y shape: (4,)
Values in X: 12
Row 2 of X: [2.5e-02 1.2e+05 1.7e+02] -> target 3950''',
   output_explain='X has 4 rows (tests) and 3 columns (features), so it holds 12 values. Row 2 counts from 0, so it is test T3. Its target is 3950 W, as in the table. NumPy prints the numbers in scientific notation, so 2.5e-02 means 0.025 m³/s. The units are not stored in the array, so you must keep them in your notes (Lesson 3.1).'),
 ],
 try_it=dict(
  instruction='Change a value and observe. In the Step 4 code, change `X_rows.append([q, dp, speed])` to `X_rows.append([q, dp])`. Then run Steps 1 to 4 again.',
  change=('X_rows.append([q, dp, speed])', 'X_rows.append([q, dp])'),
  expected_output='''X shape: (4, 2)
y shape: (4,)
Values in X: 8
Row 2 of X: [2.5e-02 1.2e+05] -> target 3950''',
  expected_observation='The number of columns d changes from 3 to 2, so X has 8 values. The number of rows and the shape of y stay the same. Choosing the features changes the columns, and the target still has one value per test. A different question could use different columns.'),
 limits=[
  'The table has only four invented tests. It shows the structure of a learning table, not a real dataset.',
  'The code does not check units for you. Lesson 3.2 says units and acquisition details stay with the data.',
  'The availability list in Step 3 was written by hand. The code cannot know what is available at decision time.',
  'Rows from one machine over time need extra care (Lesson 3.1). These four tests are treated as independent steady tests.',
 ],
 related='Lab 1 builds X and y from a table and audits flagged rows.',
 notebook='walkthrough_m03.ipynb')

W['m04'] = dict(
 title='Where do targets come from?',
 supports='Lesson 4.1 (section “Supervised learning uses input-target pairs”), Lesson 4.2 (section “Masked-signal reconstruction”) and Lesson 4.3 (sections “Simulated thermal controller” and “Rewards and safety limits”).',
 objective='See, in small plain-Python examples, where the learning signal comes from in three setups: given targets (supervised), targets built from the data (self-supervised) and reward from interaction (reinforcement learning). Nothing is trained here.',
 prereqs=[
  'You need Lessons 4.1 to 4.3 and the Module 2 and 3 Code walkthroughs.',
  'This walkthrough teaches no machine-learning method. It only shows how the roles in each setup look in a few lines of code.',
 ],
 python_ideas=[
  'A list item has a position number that starts at 0. In `signal[2]`, the 2 picks the third item.',
  '`None` is Python’s way to say “no value here”.',
  '`range(n)` counts 0, 1, …, n − 1. `abs(x)` gives the size of x without its sign.',
  '`x in items` checks whether x is in a list. `a if condition else b` gives a when the condition is true and b otherwise.',
 ],
 example=[
  'You use a few invented numbers in three small examples. They are synthetic and have no link to a real machine.',
  'Example 1 shows input-target pairs. Example 2 hides part of a signal and keeps the hidden values as targets. Example 3 runs a very small simulated heater for a few steps, with a fixed rule instead of learning.',
 ],
 data_table='''Example 1 (supplied targets): flow (m³/s), pressure rise (Pa) -> power (W)
Example 2 (built targets):    signal in °C = 20, 21, 22, 23, 24, 25
Example 3 (interaction):      start 296 K, target 300 K, safety limit 305 K''',
 steps=[
  dict(
   heading='Step 1. Supervised: the targets are supplied',
   explain='In supervised learning each example comes with a known target (Lesson 4.1). Here each target is a number, a measured power in W, so this would be a regression problem. If the targets were categories such as intact or cracked, it would be classification.',
   code='''# Step 1: input-target pairs (synthetic)
# inputs: (flow in m³/s, pressure rise in Pa); target: measured power in W
pairs = [
    ((0.020, 100000), 2800),
    ((0.015,  80000), 1650),
    ((0.025, 120000), 3950),
]

for inputs, target in pairs:
    print("inputs", inputs, "-> given target", target, "W")''',
   expected_output='''inputs (0.02, 100000) -> given target 2800 W
inputs (0.015, 80000) -> given target 1650 W
inputs (0.025, 120000) -> given target 3950 W''',
   output_explain='A person or a measurement supplied each target. Training would adjust a model until its outputs come close to these targets.'),
  dict(
   heading='Step 2. Self-supervised: build the target from the data',
   explain='In masked-signal reconstruction (Lesson 4.2) you hide a section of a signal. The hidden values are the target, and the original signal supplies them. Nobody labels anything by hand. A real model would estimate the hidden values. To keep the code simple, a fixed rule stands in for the model: it repeats the last visible value.',
   code='''# Step 2: build a constructed input and a constructed target from one signal
signal = [20.0, 21.0, 22.0, 23.0, 24.0, 25.0]    # observed signal in °C (synthetic)
hidden = [2, 3]                                   # positions we hide

constructed_input = []
for i in range(len(signal)):
    if i in hidden:
        constructed_input.append(None)            # None means "hidden"
    else:
        constructed_input.append(signal[i])

constructed_target = []
for i in hidden:
    constructed_target.append(signal[i])          # original values of the hidden part
print("constructed input: ", constructed_input)
print("constructed target:", constructed_target)

# a fixed stand-in for a model: repeat the last visible value
estimate = [constructed_input[1], constructed_input[1]]
print("estimate:          ", estimate)
print("target - estimate: ", [constructed_target[0] - estimate[0], constructed_target[1] - estimate[1]])''',
   expected_output='''constructed input:  [20.0, 21.0, None, None, 24.0, 25.0]
constructed target: [22.0, 23.0]
estimate:           [21.0, 21.0]
target - estimate:  [1.0, 2.0]''',
   output_explain='The constructed input has a gap. The constructed target keeps the original hidden values, 22.0 and 23.0 °C. The last line shows the disagreement between the target and the estimate. Training aims to make this disagreement smaller. Inputs, targets and an objective all exist even though nobody labelled the data (Lesson 4.2).'),
  dict(
   heading='Step 3. Reinforcement learning: the roles in a loop',
   explain='In reinforcement learning an agent sees a state, picks an action and receives a reward from an environment (Lesson 4.3). Here the state is the temperature, the action is the heater command (1 = on, 0 = off), and the environment is a made-up thermal rule. The policy is a fixed rule you write: heat when below the target. Nothing learns. The reward and the safety limit are kept separate. All numbers, including the reward weights, are invented for teaching.',
   code='''# Step 3: a tiny simulated thermal loop (synthetic, bounded simulation)
temp = 296.0              # state: temperature in K
target = 300.0            # target temperature in K
safety_limit = 305.0      # safety constraint in K (kept separate from the reward)
heat_step = 2.0           # K gained per step when the heater is on
loss_step = 0.5           # K lost per step

for step in range(6):
    action = 1 if temp < target else 0          # policy: heater on below the target
    temp = temp + heat_step * action - loss_step   # environment responds
    reward = -abs(temp - target) - 0.2 * action    # tracking error plus an energy penalty
    safe = temp <= safety_limit
    print(f"step {step}: action {action}, temperature {temp:.1f} K, reward {reward:.1f}, within limit: {safe}")''',
   expected_output='''step 0: action 1, temperature 297.5 K, reward -2.7, within limit: True
step 1: action 1, temperature 299.0 K, reward -1.2, within limit: True
step 2: action 1, temperature 300.5 K, reward -0.7, within limit: True
step 3: action 0, temperature 300.0 K, reward -0.0, within limit: True
step 4: action 0, temperature 299.5 K, reward -0.5, within limit: True
step 5: action 1, temperature 301.0 K, reward -1.2, within limit: True''',
   output_explain='Each row is one pass through state, action, environment and reward. The reward is higher (closer to 0) when the temperature is close to the target and the heater uses less. The “within limit” column is a separate safety check. A good reward does not replace it (Lesson 4.3). The “-0.0” in step 3 is only how Python prints a negative zero.'),
 ],
 try_it=dict(
  instruction='Change a value and observe. In the Step 3 code, change `heat_step = 2.0` to `heat_step = 6.0`. Then run Step 3 again.',
  change=('heat_step = 2.0           # K gained per step when the heater is on', 'heat_step = 6.0           # K gained per step when the heater is on'),
  expected_output='''step 0: action 1, temperature 301.5 K, reward -1.7, within limit: True
step 1: action 0, temperature 301.0 K, reward -1.0, within limit: True
step 2: action 0, temperature 300.5 K, reward -0.5, within limit: True
step 3: action 0, temperature 300.0 K, reward -0.0, within limit: True
step 4: action 0, temperature 299.5 K, reward -0.5, within limit: True
step 5: action 1, temperature 305.0 K, reward -5.2, within limit: True''',
  expected_observation='With a stronger heater the temperature jumps past the target. In step 5 it reaches exactly 305.0 K, the safety limit, and the reward falls to −5.2. Try `heat_step = 8.0` as well: the temperature then goes above the limit and “within limit” becomes False. The reward and the safety limit measure different things. A high reward never proves safe behaviour.'),
 limits=[
  'Nothing in this walkthrough learns. The “model” in Step 2 and the policy in Step 3 are fixed rules that stand in for a learned model.',
  'The temperature rule, the reward weights and the limit in Step 3 are invented. They are not a design for a real heater controller.',
  'The course does not authorise experiments on real machinery. Use bounded simulations only (Lesson 4.3).',
  'Clustering and anomaly detection (Lesson 4.1) are not shown here. Clustering appears in Module 9.',
 ],
 related='',
 notebook='walkthrough_m04.ipynb')

W['m05'] = dict(
 title='Clean, scale and encode: the rules in code',
 supports='Lesson 5.1 (section “Mean-imputation example”), Lesson 5.2 (sections “State the scaling rule”, “Standardization uses training statistics” and “Encode categories without false magnitude”) and Lesson 5.3 (section “Split, fit and apply consistently”).',
 objective='Reproduce the worked examples from Lessons 5.1 and 5.2 in Python: mean imputation, min-max scaling, standardization and one-hot encoding. Then see why the stored training statistics, not the test data, must be used to transform test values.',
 prereqs=[
  'You need Lessons 5.1 to 5.3 and the Module 2 to 4 Code walkthroughs.',
  'No libraries are needed. You write each rule yourself, so you see exactly what it does. Lesson 5.2 names the scikit-learn tools `StandardScaler` and `OneHotEncoder`, which do the same jobs.',
 ],
 python_ideas=[
  '`value is None` checks for a missing value. `value is not None` checks that a value is present.',
  '`sum(items)` adds up a list of numbers. `len(items)` counts them. `enumerate(items)` gives each position together with its item.',
  '`def name(argument):` defines a small reusable function. `return` gives back its result. You met `a if condition else b` in the Module 4 walkthrough.',
  'A list can mix numbers and `None`, for example `[20, 22, None, 24]`.',
 ],
 example=[
  'All examples reuse the numbers from the lessons: the readings [20, 22, missing, 24], the bounds 0 to 100 °C with x = 25 °C, and a training mean of 40 °C with a training standard deviation of 10 °C.',
  'The data are illustrative and synthetic. The lessons do not give a unit for the first list, so treat it as arithmetic only.',
 ],
 data_table='''Readings:            20, 22, missing, 24
Scaling bounds:      0 to 100 °C, x = 25 °C
Training statistics: mean 40 °C, standard deviation 10 °C
Categories:          A, B, C''',
 steps=[
  dict(
   heading='Step 1. Mean imputation',
   explain='Lesson 5.1 fills the missing reading with the mean of the observed values: (20 + 22 + 24) / 3 = 22. The code keeps a record of which position was changed, because Lesson 5.1 says every change must be documented.',
   code='''# Step 1: mean imputation of one missing reading
readings = [20, 22, None, 24]     # None = missing

observed = []
for value in readings:
    if value is not None:
        observed.append(value)
mean_value = sum(observed) / len(observed)
print("Mean of the observed values:", mean_value)

filled = []
changed_positions = []
for position, value in enumerate(readings):
    if value is None:
        filled.append(mean_value)
        changed_positions.append(position)
    else:
        filled.append(value)
print("After imputation:", filled)
print("Changed positions:", changed_positions)''',
   expected_output='''Mean of the observed values: 22.0
After imputation: [20, 22, 22.0, 24]
Changed positions: [2]''',
   output_explain='The missing value became 22, as in Lesson 5.1.  The filled value is an estimate. It does not recover the original measurement. For a predictive pipeline, the mean would come from training data only.'),
  dict(
   heading='Step 2. Min-max scaling',
   explain='The rule in Lesson 5.2 is x_scaled = (x − x_min) / (x_max − x_min). All three values are in °C, so the result has no unit.',
   code='''# Step 2: min-max scaling with stated bounds
x = 25.0                  # observation in °C
x_min = 0.0               # stated lower bound in °C
x_max = 100.0             # stated upper bound in °C
x_scaled = (x - x_min) / (x_max - x_min)
print("Min-max scaled value:", x_scaled)''',
   expected_output='Min-max scaled value: 0.25',
   output_explain='25 °C becomes 0.25, as in Lesson 5.2. The bounds 0 and 100 °C map to 0 and 1. A future value outside those bounds would map outside 0 to 1.'),
  dict(
   heading='Step 3. One-hot encoding',
   explain='Lesson 5.2 says to avoid coding categories A, B and C as 1, 2 and 3, because that adds an order and distances that do not exist. One-hot encoding uses one indicator column per known category.',
   code='''# Step 3: one-hot encoding for three known categories
categories = ["A", "B", "C"]

def one_hot(label):
    row = []
    for category in categories:
        row.append(1 if label == category else 0)
    return row

for label in ["A", "B", "C"]:
    print(label, "->", one_hot(label))''',
   expected_output='''A -> [1, 0, 0]
B -> [0, 1, 0]
C -> [0, 0, 1]''',
   output_explain='These are the same rows as the lesson’s example. The indicators show membership. They carry no physical size. A category that was not in the list would give [0, 0, 0] here. Lesson 5.2 asks you to decide this rule on purpose.'),
  dict(
   heading='Step 4. Standardize with stored training statistics',
   explain='Lesson 5.2 gives z = (x − μ_train) / σ_train. Lesson 5.3 says to apply the stored training statistics to validation and test inputs and not to recalculate them from those sets. The code first does it correctly. Then it shows what happens if you wrongly use the test mean.',
   code='''# Step 4: standardization with stored training statistics
train_mean = 40.0         # mean of the training data in °C (stored)
train_std = 10.0          # standard deviation of the training data in °C (stored)
test_values = [60.0, 25.0]    # new inputs in °C

print("Correct: use the stored training statistics")
for x in test_values:
    z = (x - train_mean) / train_std
    print(f"  x = {x:.0f} °C -> z = {z:.2f}")

wrong_mean = sum(test_values) / len(test_values)   # WRONG: statistic taken from the test set
print("Wrong: mean recomputed from the test values =", wrong_mean)
for x in test_values:
    z = (x - wrong_mean) / train_std
    print(f"  x = {x:.0f} °C -> z = {z:.2f}")''',
   expected_output='''Correct: use the stored training statistics
  x = 60 °C -> z = 2.00
  x = 25 °C -> z = -1.50
Wrong: mean recomputed from the test values = 42.5
  x = 60 °C -> z = 1.75
  x = 25 °C -> z = -1.75''',
   output_explain='The correct values match Lesson 5.2: z = 2 for 60 °C and z = −1.5 for 25 °C. With the wrong mean, the same 60 °C gives 1.75. The numbers changed because the test set leaked into the preprocessing. Lesson 5.3 says this crosses the evaluation boundary even if no test target is used. The z values have no unit. Keep the original °C values for physical meaning.'),
 ],
 try_it=dict(
  instruction='Change a value and observe. In the Step 4 code, change `train_mean = 40.0` to `train_mean = 45.0`. Then run Step 4 again.',
  change=('train_mean = 40.0         # mean of the training data in °C (stored)', 'train_mean = 45.0         # mean of the training data in °C (stored)'),
  expected_output='''Correct: use the stored training statistics
  x = 60 °C -> z = 1.50
  x = 25 °C -> z = -2.00
Wrong: mean recomputed from the test values = 42.5
  x = 60 °C -> z = 1.75
  x = 25 °C -> z = -1.75''',
  expected_observation='The correct z values change to 1.50 and −2.00, because the stored training statistics changed. The wrong values stay the same, because they never use the stored mean. Stored statistics decide how every later input is transformed. If you change them, you must record that change. If the training data changes, you must also refit the transformation on the training data only.'),
 limits=[
  'The values are the lessons’ teaching numbers. They are not sensor data.',
  'The code does not decide how to treat an unseen category, a constant feature or a very different unit. Lesson 5.2 says you must state those rules.',
  'Mean imputation is only one rule. Lesson 5.1 lists others and says to choose from the measurement context.',
  'In a real project, learned preprocessing is fitted inside the training part of each split. This walkthrough only shows the arithmetic.',
 ],
 related='Lab 1 audits flagged rows and units. Lab 2 uses a split and a physical feature.',
 notebook='walkthrough_m05.ipynb')
