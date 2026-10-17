"""Code walkthroughs for Modules 10, 11 and 12 (batch C). Module 13 has no code walkthrough (see PR notes)."""

W = {}

W['m10'] = dict(
 title='Check the evaluation boundary',
 supports='Lesson 10.1 (section “Cross-validation stays inside development data”) and Lesson 10.3 (sections “Leakage violates an information boundary” and “Preprocessing can leak without using target labels”).',
 objective='Reproduce the five-fold counts from Lesson 10.1. Then check two kinds of leakage with very small examples: the same machine in both training and test data, and a mean fitted on data that includes the held-out value.',
 prereqs=[
  'You need Lessons 10.1 to 10.3 and the earlier code walkthroughs. They introduce variables, lists, `for` loops, tuples, `def`, `sum`, `len` and f-strings.',
  'Run the code in Google Colab or Jupyter. This walkthrough uses plain Python only.',
 ],
 python_ideas=[
  '`a // b` divides a by b and drops any fraction. Here `100 // 5` is 20.',
  '`x not in items` is true when x is not in the list. You met `x in items` in the Module 4 walkthrough.',
  '`range(n)` counts 0, 1, …, n − 1. You met it in the Module 4 walkthrough.',
 ],
 example=[
  'Steps 1 and 2 use the numbers of Lesson 10.1: 100 independent examples in five folds. Step 3 uses six invented rows from three machines. Step 4 uses five invented numbers.',
  'All data are synthetic and dimensionless. They are invented for teaching and are not measurements from real equipment.',
 ],
 data_table='''Step 3: six rows from three machines
row 1: M1    row 2: M1
row 3: M2    row 4: M2
row 5: M3    row 6: M3

Step 4: training values 10, 12, 14, 16 and one held-out value 40''',
 steps=[
  dict(
   heading='Step 1. Count the examples in one fold',
   explain='Lesson 10.1 divides 100 independent examples into five equal folds. In each iteration one fold is held out for validation. The other four folds are used for training.',
   code='''# Step 1: five-fold counts from Lesson 10.1
n_examples = 100
n_folds = 5
fold_size = n_examples // n_folds        # examples in one fold
n_train = n_examples - fold_size         # examples left for training
print("Examples per fold:", fold_size)
print("In one iteration:", n_train, "for training and", fold_size, "for validation")''',
   expected_output='''Examples per fold: 20
In one iteration: 80 for training and 20 for validation''',
   output_explain='This matches Lesson 10.1: 20 examples per fold, 80 for training and 20 for validation. These are counts of examples, not physical quantities.'),
  dict(
   heading='Step 2. List the five validation folds',
   explain='Now you list which examples each fold holds out. The examples are numbered 0 to 99. Fold 1 holds out examples 0 to 19, fold 2 holds out 20 to 39, and so on. Every example is held out exactly once.',
   code='''# Step 2: the validation examples of each fold
for fold in range(n_folds):
    first = fold * fold_size
    last = first + fold_size - 1
    print(f"Fold {fold + 1}: validation examples {first} to {last}; {n_train} examples left for training")''',
   expected_output='''Fold 1: validation examples 0 to 19; 80 examples left for training
Fold 2: validation examples 20 to 39; 80 examples left for training
Fold 3: validation examples 40 to 59; 80 examples left for training
Fold 4: validation examples 60 to 79; 80 examples left for training
Fold 5: validation examples 80 to 99; 80 examples left for training''',
   output_explain='The five validation parts do not overlap and together cover all 100 examples. Cross-validation stays inside the development data. It does not replace a separate final test set (Lesson 10.1). This simple numbering is only correct when the examples are independent, as in the lesson.'),
  dict(
   heading='Step 3. Check whether a machine appears on both sides of a split',
   explain='Lesson 10.1 says that predicting a machine absent from development is a different question from predicting later rows of a known machine. Here the function `shared_machines` lists the machines that appear in both the training rows and the test rows. An empty list means that no machine appears on both sides.',
   code='''# Step 3: which machines appear in both training and test rows?
rows = [("row 1", "M1"), ("row 2", "M1"),
        ("row 3", "M2"), ("row 4", "M2"),
        ("row 5", "M3"), ("row 6", "M3")]

def shared_machines(test_rows):
    train_machines = []
    test_machines = []
    for row, machine in rows:
        if row in test_rows:
            test_machines.append(machine)
        else:
            train_machines.append(machine)
    shared = []
    for machine in test_machines:
        if machine in train_machines and machine not in shared:
            shared.append(machine)
    return shared

print("Mixed-rows split, machines in both sets:", shared_machines(["row 2", "row 4", "row 6"]))
print("Machine hold-out split, machines in both sets:", shared_machines(["row 5", "row 6"]))''',
   expected_output='''Mixed-rows split, machines in both sets: ['M1', 'M2', 'M3']
Machine hold-out split, machines in both sets: []''',
   output_explain='In the mixed-rows split every test machine also appears in training. The model could recognise those machines. In the hold-out split, machine M3 is completely absent from training. Only this second split can show how the procedure behaves on a machine it has not seen. Use it when the intended use is a new machine.'),
  dict(
   heading='Step 4. See a preprocessing leak',
   explain='Lesson 10.3 says that fitting a scaler on all data lets held-out examples influence the training procedure. Here the “fitted value” is a mean. The correct way fits the mean on the training values only. The leaky way includes the held-out value. Then each value is centred by subtracting the mean.',
   code='''# Step 4: a mean fitted with and without the held-out value
train_values = [10, 12, 14, 16]
held_out = [40]

mean_train = sum(train_values) / len(train_values)
mean_all = (sum(train_values) + sum(held_out)) / (len(train_values) + len(held_out))

print(f"Mean fitted on training values only: {mean_train:.1f}")
print(f"Mean fitted on all values: {mean_all:.1f}")
print(f"Held-out value after centring (correct): {held_out[0] - mean_train:.1f}")
print(f"Held-out value after centring (leaky): {held_out[0] - mean_all:.1f}")''',
   expected_output='''Mean fitted on training values only: 13.0
Mean fitted on all values: 18.4
Held-out value after centring (correct): 27.0
Held-out value after centring (leaky): 21.6''',
   output_explain='The leaky mean (18.4) moved toward the held-out value 40. The held-out example made itself look less unusual. The correct procedure fits the mean on training values only and then applies that stored value to the held-out example. The same idea applies to a scaler or an imputer inside every cross-validation fold.'),
 ],
 try_it=dict(
  instruction='Change a value and observe. In Step 4, change `held_out = [40]` to `held_out = [60]`. Then run the cell again.',
  change=('held_out = [40]', 'held_out = [60]'),
  expected_output='''Mean fitted on training values only: 13.0
Mean fitted on all values: 22.4
Held-out value after centring (correct): 47.0
Held-out value after centring (leaky): 37.6''',
  expected_observation='The correct mean stays at 13.0, because it never sees the held-out value. The leaky mean moves from 18.4 to 22.4, so the leak grows when the held-out value is further from the training values.'),
 limits=[
  'The data are tiny, synthetic and dimensionless. They show how to count and check. They do not show how large a real leak would be.',
  'Step 2 numbers the folds in order. This is only correct for independent examples. For time series or grouped data, use the splits taught in Lessons 10.1 and 10.3.',
  'Step 4 uses a mean as a very simple fitted value. A real scaler or imputer is checked in the same way: which examples contributed to its fitted values?',
  'The code checks a boundary. It does not fit or evaluate a model.',
 ],
 related='Lab 2 (Module 7) and Lab 3 (Module 8) use a train and test split. This walkthrough shows how to check the boundary behind such a split.',
 notebook='walkthrough_m10.ipynb')

W['m11'] = dict(
 title='One neuron, one update, one epoch',
 supports='Lesson 11.1 (sections “Follow the computation through a neuron”, “Apply the ReLU activation” and “Work through the supplied forward calculation”), Lesson 11.2 (section “Calculate the supplied numerical step”) and Lesson 11.3 (section “Calculate updates per epoch”).',
 objective='Reproduce the three numerical examples of Module 11: the forward calculation of one neuron with ReLU, one gradient-descent update, and the number of updates per epoch.',
 prereqs=[
  'You need Lessons 11.1 to 11.3 and the earlier code walkthroughs. They introduce variables, `def`, `return`, `for` loops, f-strings and `//`.',
  'Run the code in Google Colab or Jupyter. This walkthrough uses plain Python only. It does not train a network.',
 ],
 python_ideas=[
  '`max(a, b)` gives the larger of two numbers. `max(0, z)` is exactly the ReLU rule of Lesson 11.1.',
  '`def relu(z):` defines a function, as in the Module 5 walkthrough.',
  '`a // b` drops the fraction, as in the Module 10 walkthrough.',
 ],
 example=[
  'All numbers come from the lessons. The neuron uses x₁ = 2, x₂ = 1, w₁ = 0.5, w₂ = −1 and b = 0.2. The update uses θ_old = 2, gradient 0.5 and learning rate η = 0.1. The epoch example has 1,000 training examples and batch size 50.',
  'Lessons 11.1 and 11.2 treat these values as dimensionless. They are teaching numbers and not measurements from real equipment.',
 ],
 data_table='''Forward example:  x1 = 2, x2 = 1, w1 = 0.5, w2 = -1, b = 0.2
Update example:   theta_old = 2, gradient = 0.5, learning rate = 0.1
Epoch example:    1000 training examples, batch size 50''',
 steps=[
  dict(
   heading='Step 1. The weighted sum of one neuron',
   explain='Lesson 11.1 calculates the weighted sum z = w₁x₁ + w₂x₂ + b. First calculate the two products. Then add them and the bias. Applying the activation is a separate, later step.',
   code='''# Step 1: weighted sum of one neuron (dimensionless numbers)
x1 = 2
x2 = 1
w1 = 0.5
w2 = -1
b = 0.2

contribution1 = w1 * x1
contribution2 = w2 * x2
z = contribution1 + contribution2 + b
print(f"First contribution: {contribution1:.1f}")
print(f"Second contribution: {contribution2:.1f}")
print(f"Weighted sum z: {z:.1f}")''',
   expected_output='''First contribution: 1.0
Second contribution: -1.0
Weighted sum z: 0.2''',
   output_explain='This matches Lesson 11.1. The two contributions cancel, so z equals the bias, 0.2.'),
  dict(
   heading='Step 2. Apply the ReLU activation',
   explain='ReLU is a = max(0, z). Negative values give zero. Positive values pass through unchanged. First you check the three examples from the lesson. Then you apply ReLU to the z from Step 1.',
   code='''# Step 2: ReLU, a = max(0, z)
def relu(z):
    return max(0, z)

for test_z in [-3, 0.2, 2]:
    print(f"ReLU({test_z}) = {relu(test_z)}")

a = relu(z)
print(f"Neuron output a: {a:.1f}")''',
   expected_output='''ReLU(-3) = 0
ReLU(0.2) = 0.2
ReLU(2) = 2
Neuron output a: 0.2''',
   output_explain='The three values match the lesson: −3 gives 0, 0.2 gives 0.2 and 2 gives 2. Because z = 0.2 is positive, ReLU leaves it unchanged. This is a forward calculation only. It does not calculate a gradient or change a weight.'),
  dict(
   heading='Step 3. One gradient-descent update',
   explain='Lesson 11.2 gives the rule θ_new = θ_old − η∇L. Here the gradient is supplied by the lesson. The code does not derive it from a loss function.',
   code='''# Step 3: one update, theta_new = theta_old - learning_rate * gradient
theta_old = 2
gradient = 0.5            # supplied by the lesson
learning_rate = 0.1       # a training setting, not a fitted weight

adjustment = learning_rate * gradient
theta_new = theta_old - adjustment
print(f"Adjustment: {adjustment:.2f}")
print(f"New parameter: {theta_new:.2f}")''',
   expected_output='''Adjustment: 0.05
New parameter: 1.95''',
   output_explain='This matches Lesson 11.2: 0.1 × 0.5 = 0.05 and 2 − 0.05 = 1.95. The learning rate scales the gradient before it is subtracted. It is chosen by the engineer. It is not learned.'),
  dict(
   heading='Step 4. Count the updates in an epoch',
   explain='Lesson 11.3 has 1,000 training examples and a batch size of 50. Each batch gives one update. One epoch is one pass through all the examples. So updates per epoch = 1,000 ÷ 50.',
   code='''# Step 4: updates per epoch
n_total = 1000
batch_size = 50
updates_per_epoch = n_total // batch_size
print("Updates per epoch:", updates_per_epoch)

epochs = 3
print("Updates after 3 epochs:", epochs * updates_per_epoch)''',
   expected_output='''Updates per epoch: 20
Updates after 3 epochs: 60''',
   output_explain='This matches Lesson 11.3: 20 updates per epoch. The second line assumes that each epoch uses the same 20 batches. An epoch counts passes through the data. An update counts changes of the parameters. They are different counts. More training updates do not by themselves mean better performance on unseen data.'),
 ],
 try_it=dict(
  instruction='Change a value and observe. In Step 4, change `batch_size = 50` to `batch_size = 100`. Then run the cell again.',
  change=('batch_size = 50', 'batch_size = 100'),
  expected_output='''Updates per epoch: 10
Updates after 3 epochs: 30''',
  expected_observation='With larger batches, one epoch needs fewer updates: 1,000 ÷ 100 = 10. The number of epochs is unchanged. This shows that epochs and updates are different counts.'),
 limits=[
  'The code does not train a network. It follows three small calculations by hand-sized numbers.',
  'The gradient in Step 3 is given. The lesson does not derive it from a loss. Backpropagation is not shown here.',
  'The numbers are dimensionless teaching numbers. They say nothing about the performance of a real network or real equipment.',
  'Step 4 assumes that the number of examples divides evenly by the batch size, as in the lesson.',
 ],
 related='No course lab trains a neural network. This walkthrough shows only the arithmetic behind one neuron, one update and one epoch.',
 notebook='walkthrough_m11.ipynb')

W['m12'] = dict(
 title='Windows, timestamps and what is available at issue time',
 supports='Lesson 12.2 (section “Define the forecast issue time”) and Lesson 12.3 (sections “Use timestamps rather than filtered row positions”, “Define horizon and information availability” and “Handle overlapping windows and temporal gaps”).',
 objective='Check the 96-samples-per-day rule, see why a row number is not a clock after rows are removed, calculate the RMS of two small windows, check which inputs exist at a forecast issue time, and see how overlapping windows share samples.',
 prereqs=[
  'You need Lessons 12.1 to 12.3 and the earlier code walkthroughs. They introduce variables, lists, tuples, `for` loops, `def`, `sum`, `len`, `range`, `**` and f-strings.',
  'Run the code in Google Colab or Jupyter. This walkthrough uses plain Python only.',
 ],
 python_ideas=[
  '`items[a:b]` is a slice. It gives the items from position a up to, but not including, position b. For example `[10, 20, 30, 40][1:3]` is `[20, 30]`.',
  '`x ** 0.5` is the square root of x. You met it in the Module 7 walkthrough.',
  'A time can be stored as the number of minutes since midnight. 60 means 01:00 and 90 means 01:30.',
 ],
 example=[
  'Step 1 uses the numbers of Lesson 12.3: samples every 15 minutes over 24 hours. Steps 2 to 5 use a few invented signal values and times.',
  'All data are synthetic. The signal values are in arbitrary units. They are not measurements from real equipment.',
 ],
 data_table='''Step 3 signal (arbitrary units), 8 samples:
3, -3, 3, -3, 1, 1, 1, 1

Step 4 inputs for a next-day load forecast issued at 18:00:
observed load up to 18:00
published weather forecast, issued at 12:00
tomorrow's measured weather''',
 steps=[
  dict(
   heading='Step 1. How many 15-minute samples make 24 hours?',
   explain='Lesson 12.3 says that for complete, regular data sampled every 15 minutes, 96 samples correspond to 24 hours. You can check this with arithmetic.',
   code='''# Step 1: samples in 24 hours at one sample every 15 minutes
hours = 24
minutes_per_hour = 60
sample_interval = 15      # minutes between samples
n_samples = hours * minutes_per_hour // sample_interval
print("Samples in 24 hours:", n_samples)''',
   expected_output='Samples in 24 hours: 96',
   output_explain='24 × 60 ÷ 15 = 96. This is true only for complete, regular data. The next step shows why.'),
  dict(
   heading='Step 2. A row number is not a clock',
   explain='Here the sensor sends a sample every 15 minutes. The times are stored in minutes since midnight. In the second list, the sample at 45 minutes is missing. The row at position 3 then belongs to a different time.',
   code='''# Step 2: row position versus actual timestamp (minutes since midnight)
complete = [0, 15, 30, 45, 60, 75]
with_gap = [0, 15, 30, 60, 75, 90]      # the sample at 45 is missing

print("Row 3, complete data: time", complete[3], "min")
print("Row 3, data with a gap: time", with_gap[3], "min")
print("Time covered by the six rows with a gap:", with_gap[-1] - with_gap[0], "min")
print("Six complete rows would cover:", complete[-1] - complete[0], "min")''',
   expected_output='''Row 3, complete data: time 45 min
Row 3, data with a gap: time 60 min
Time covered by the six rows with a gap: 90 min
Six complete rows would cover: 75 min''',
   output_explain='The same row number points to 45 min in one list and to 60 min in the other. Six rows cover 90 minutes, not 75. Counting rows therefore does not measure time after a gap. Use the actual timestamps, as Lesson 12.3 says. `with_gap[-1]` means the last item of the list.'),
  dict(
   heading='Step 3. Calculate the RMS of two windows',
   explain='Lesson 12.3 says that RMS summarises signal magnitude over a window. To calculate it: square each value, take the mean of the squares, then take the square root. The signal below has two windows of four samples each. The window length is four samples, so it must be recorded together with the sampling interval.',
   code='''# Step 3: mean and RMS of two windows (arbitrary units)
signal = [3, -3, 3, -3, 1, 1, 1, 1]
window_length = 4         # samples per window

for start in [0, 4]:
    window = signal[start:start + window_length]
    mean_value = sum(window) / len(window)
    squares = 0
    for value in window:
        squares += value ** 2
    rms = (squares / len(window)) ** 0.5
    print(f"Window starting at sample {start}: mean {mean_value:.1f}, RMS {rms:.1f}")''',
   expected_output='''Window starting at sample 0: mean 0.0, RMS 3.0
Window starting at sample 4: mean 1.0, RMS 1.0''',
   output_explain='The first window swings between +3 and −3. Its mean is 0.0, but its RMS is 3.0. The mean hides the swing and the RMS shows it. The second window is steady at 1, so mean and RMS are both 1.0. An RMS value is only meaningful together with its window length and sampling rate.'),
  dict(
   heading='Step 4. Check what exists at the issue time',
   explain='Lesson 12.3 gives a next-day load forecast issued at 18:00. A feature may be used only if it already exists at that time. The list below marks each input as available or not. The inputs follow the lesson.',
   code='''# Step 4: inputs for a next-day load forecast issued at 18:00
inputs = [
    ("observed load up to 18:00", True),
    ("published weather forecast, issued at 12:00", True),
    ("tomorrow's measured weather", False),
]

for name, available in inputs:
    if available:
        print("Use:     ", name)
    else:
        print("Exclude: ", name)''',
   expected_output='''Use:      observed load up to 18:00
Use:      published weather forecast, issued at 12:00
Exclude:  tomorrow's measured weather''',
   output_explain='Observed load before the issue time exists. A forecast issued earlier also exists, but its uncertainty must be recorded. Tomorrow’s measured weather does not exist at 18:00 today. Using it would evaluate a different information scenario. The code only repeats the lesson’s judgement. You must still decide the availability yourself for each real input.'),
  dict(
   heading='Step 5. Overlapping windows share samples',
   explain='Lesson 12.3 says that adjacent windows can share raw samples. Here you list the sample positions of each window. The windows are four samples long and start two samples apart. Then you check which windows share a sample with window 0.',
   code='''# Step 5: sample positions of overlapping windows
n_signal = 10             # samples in the signal
window_length = 4
step = 2                  # samples between window starts

windows = []
for start in range(0, n_signal - window_length + 1, step):
    windows.append(list(range(start, start + window_length)))

for number, w in enumerate(windows):
    print(f"Window {number}: samples {w}")

for number, w in enumerate(windows):
    shared = 0
    for sample in w:
        if sample in windows[0]:
            shared += 1
    print(f"Window {number} shares {shared} samples with window 0")''',
   expected_output='''Window 0: samples [0, 1, 2, 3]
Window 1: samples [2, 3, 4, 5]
Window 2: samples [4, 5, 6, 7]
Window 3: samples [6, 7, 8, 9]
Window 0 shares 4 samples with window 0
Window 1 shares 2 samples with window 0
Window 2 shares 0 samples with window 0
Window 3 shares 0 samples with window 0''',
   output_explain='Window 1 shares two samples with window 0. If window 0 were in the training set and window 1 in the test set, the test window would contain training information. Window 2 and later share nothing with window 0. Use a chronological split with a suitable gap, as Lesson 12.3 says. `range(0, 7, 2)` counts 0, 2, 4, 6. `list(...)` turns it into a list.'),
 ],
 try_it=dict(
  instruction='Change a value and observe. In Step 5, change `step = 2` to `step = 4`. Then run the cell again.',
  change=('step = 2                  # samples between window starts', 'step = 4                  # samples between window starts'),
  expected_output='''Window 0: samples [0, 1, 2, 3]
Window 1: samples [4, 5, 6, 7]
Window 0 shares 4 samples with window 0
Window 1 shares 0 samples with window 0''',
  expected_observation='When the step equals the window length, the windows no longer share samples. Only two windows fit into ten samples, and the last two samples are not used. Neighbouring windows can still be correlated in time. Non-overlap does not by itself prove independence.'),
 limits=[
  'The signals are tiny, synthetic and in arbitrary units. They do not show how a real sensor behaves.',
  'Step 2 shows one missing sample. Lesson 12.2 asks you to inspect gaps and choose a treatment that fits the gap. This code does not fill or remove any gap.',
  'Step 4 repeats a judgement from the lesson. Code cannot decide by itself what is available at the issue time.',
  'The code does not build a forecast model or an RNN. It only checks windows and information boundaries.',
 ],
 related='No course lab uses time windows. Lab 2 (Module 7) uses a train and test split on independent designs. This walkthrough shows the timing checks needed for signals.',
 notebook='walkthrough_m12.ipynb')
