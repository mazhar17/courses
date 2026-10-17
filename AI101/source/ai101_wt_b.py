"""Code walkthroughs for Modules 6, 7, 8 and 9 (batch B)."""

W = {}

W['m06'] = dict(
 title='Fit once, predict many times',
 supports='Lesson 6.1 (sections “Training fits; inference applies” and “Worked linear example”), Lesson 6.2 (sections “Parameters are fitted values” and “Mean absolute and squared error emphasize different things”) and Lesson 6.3 (section “Interpret the supplied MAE example”).',
 objective='Use the Lesson 6.1 model ŷ = 2 + 3x in Python. See that predicting does not change the coefficients, that fitting finds them from examples, and that fitting again can change them. Then compare two losses and a model with a baseline.',
 prereqs=[
  'You need Lessons 6.1 to 6.3 and the Module 2 to 5 Code walkthroughs.',
  'This walkthrough uses scikit-learn, which is already installed in Google Colab. It is the library behind the `model.fit` and `model.predict` lines shown in Lesson 6.1.',
 ],
 python_ideas=[
  '`from sklearn.linear_model import LinearRegression` loads one model type from scikit-learn.',
  '`model = LinearRegression()` creates a model. `model.fit(X, y)` learns its parameters from the examples. `model.predict(X_new)` applies the fitted model to new inputs.',
  'After fitting, `model.intercept_` holds the fitted intercept and `model.coef_` holds the fitted slope or slopes. The trailing underscore is scikit-learn’s way to mark values learned during fitting.',
  '`x ** 2` means x squared.',
 ],
 example=[
  'Lesson 6.1 gives the model ŷ = 2 + 3x. The lesson says this arithmetic example has no physical units, so the numbers here have none either.',
  'The training points below lie exactly on that line. They are synthetic and were made for teaching.',
 ],
 data_table='''Training examples (synthetic, no units)
x    1   2   3   4   5
y    5   8  11  14  17     (y = 2 + 3x)''',
 steps=[
  dict(
   heading='Step 1. Inference with fixed parameters',
   explain='Lesson 6.1 says the intercept is 2 and the slope is 3. At x = 4, inference gives ŷ = 2 + 3 × 4 = 14. Predicting uses the parameters. It does not change them.',
   code='''# Step 1: inference with a model whose parameters are already known
b0 = 2                    # intercept
b1 = 3                    # slope

x_new = 4
y_hat = b0 + b1 * x_new
print("Prediction at x = 4:", y_hat)

x_new = 10                # a different input; the parameters stay as they are
print("Prediction at x = 10:", b0 + b1 * x_new)
print("Parameters after predicting:", b0, b1)''',
   expected_output='''Prediction at x = 4: 14
Prediction at x = 10: 32
Parameters after predicting: 2 3''',
   output_explain='The prediction at x = 4 is 14, as in the lesson. A new input gives a new prediction, but b0 and b1 are unchanged.'),
  dict(
   heading='Step 2. Fit with scikit-learn, then predict',
   explain='Now the computer finds the parameters. X must be a table with one row per example and one column per feature (Module 3), so each x value sits in its own list. The `fit` call learns the intercept and slope from the examples. The `predict` call only applies them.',
   code='''# Step 2: training (fit) and inference (predict)
import numpy as np
from sklearn.linear_model import LinearRegression

X_train = np.array([[1], [2], [3], [4], [5]])    # shape (5, 1): 5 examples, 1 feature
y_train = np.array([5, 8, 11, 14, 17])

model = LinearRegression()
model.fit(X_train, y_train)                      # training: learn the parameters
print(f"Fitted intercept: {model.intercept_:.2f}")
print(f"Fitted slope: {model.coef_[0]:.2f}")

print(f"Prediction at x = 4: {model.predict(np.array([[4]]))[0]:.2f}")
print(f"Intercept after predicting: {model.intercept_:.2f}")''',
   expected_output='''Fitted intercept: 2.00
Fitted slope: 3.00
Prediction at x = 4: 14.00
Intercept after predicting: 2.00''',
   output_explain='Fitting recovers the intercept 2 and the slope 3 that generated the points. The prediction at x = 4 is 14, and predicting did not change the intercept. `model.predict` returns an array, so `[0]` picks its first value.'),
  dict(
   heading='Step 3. Fitting again can change the parameters',
   explain='Lesson 6.1 says fitting again may change the intercept or slope. Here you fit a new model on different examples that follow y = 1 + 4x. Retraining is a separate operation with its own data.',
   code='''# Step 3: fit a new model on different examples
y_other = np.array([5, 9, 13, 17, 21])           # y = 1 + 4x

model_2 = LinearRegression()
model_2.fit(X_train, y_other)
print(f"New intercept: {model_2.intercept_:.2f}")
print(f"New slope: {model_2.coef_[0]:.2f}")
print(f"First model still has slope: {model.coef_[0]:.2f}")''',
   expected_output='''New intercept: 1.00
New slope: 4.00
First model still has slope: 3.00''',
   output_explain='Different training examples gave different parameters. The first model keeps its own parameters, because you created a second model object. In a real project, retraining needs its own data and validation (Lesson 6.1).'),
  dict(
   heading='Step 4. The loss changes what fitting emphasizes',
   explain='Lesson 6.2 says mean absolute error (MAE) averages the absolute residuals. Mean squared error (MSE) squares them before averaging, so large residuals count more. Here are four residuals. One is much larger than the others. They are invented, in an arbitrary unit.',
   code='''# Step 4: the same residuals, two different losses
residuals = [1, 1, 1, 10]

abs_total = 0
sq_total = 0
for r in residuals:
    abs_total += abs(r)
    sq_total += r ** 2

print("MAE:", abs_total / len(residuals))
print("MSE:", sq_total / len(residuals))''',
   expected_output='''MAE: 3.25
MSE: 25.75''',
   output_explain='One large residual of 10 dominates the MSE. It contributes 100 of the total 103 in the sum of squares. It contributes 10 of the total 13 in the sum of absolute values. The choice of loss changes what fitting emphasizes. MSE is not in the units of the output, but its square root is (Module 7).'),
  dict(
   heading='Step 5. Compare a model with a baseline',
   explain='In Lesson 6.3 the supplied model has an MAE of 1.2 kW and the physical baseline has an MAE of 0.8 kW on the same held-out tests. Convert both to watts, then compare them.',
   code='''# Step 5: model versus baseline on the same held-out tests
ml_mae_kw = 1.2           # MAE of the ML model in kW
baseline_mae_kw = 0.8     # MAE of the physical baseline in kW

ml_mae_w = ml_mae_kw * 1000
baseline_mae_w = baseline_mae_kw * 1000
print(f"ML model MAE: {ml_mae_w:.0f} W")
print(f"Baseline MAE: {baseline_mae_w:.0f} W")

if ml_mae_w < baseline_mae_w:
    print("The ML model has the lower MAE on these tests.")
else:
    print("The baseline has the lower MAE, so the ML model has not shown an improvement.")''',
   expected_output='''ML model MAE: 1200 W
Baseline MAE: 800 W
The baseline has the lower MAE, so the ML model has not shown an improvement.''',
   output_explain='1.2 kW is 1,200 W and 0.8 kW is 800 W, as in Lesson 6.3. The baseline has the lower error. Lesson 6.3 says to report that result and not to force a case for ML. Cost, interpretability and evidence for the operating range also matter.'),
 ],
 try_it=dict(
  instruction='Change a value and observe. In the Step 5 code, change `ml_mae_kw = 1.2` to `ml_mae_kw = 0.5`. Then run Step 5 again.',
  change=('ml_mae_kw = 1.2           # MAE of the ML model in kW', 'ml_mae_kw = 0.5           # MAE of the ML model in kW'),
  expected_output='''ML model MAE: 500 W
Baseline MAE: 800 W
The ML model has the lower MAE on these tests.''',
  expected_observation='The conclusion flips. A lower error on the same held-out tests is evidence for the ML model on that metric. Lesson 6.3 still asks you to check that the comparison is fair: the same examples, the same information at prediction time and the stated metric.'),
 limits=[
  'The numbers in Steps 1 to 4 have no physical meaning. In a real application you must state the units of the input and of the output.',
  'The training points lie exactly on a line, so the fit is perfect. Real measurements contain noise, and fitted coefficients would not be this clean.',
  'The code does not hold out any examples, so it says nothing about performance on unseen data. Module 7 covers evaluation on held-out data.',
  'The MAE values in Step 5 are the lesson’s numbers. They are not results from a real model.',
 ],
 related='Lab 2 fits and evaluates a pump-power model.',
 notebook='walkthrough_m06.ipynb')

W['m07'] = dict(
 title='Residuals, MAE, RMSE and R² by hand',
 supports='Lesson 7.1 (section “Calculate the supplied prediction”), Lesson 7.2 (sections “Begin with signed residuals”, “MAE and RMSE retain target units” and “R² is a relative score”) and Lesson 7.3 (section “Use three distinct stages”, the baseline comparison).',
 objective='Reproduce the temperature-rise examples from Lessons 7.1 and 7.2 in Python: the prediction and residual at 10 W, then MAE, RMSE and R² for three observations. Then compare the model with a training-mean baseline.',
 prereqs=[
  'You need Lessons 7.1 to 7.3 and the Module 2 to 6 Code walkthroughs.',
  'No libraries are needed. You calculate each metric yourself, so you see exactly what it measures.',
 ],
 python_ideas=[
  '`x ** 0.5` is the square root of x. `x ** 2` is x squared.',
  'In an f-string, `{value:.3f}` shows three digits after the decimal point.',
  'A `for` loop can add to a running total: `total += abs(r)` means `total = total + abs(r)`.',
 ],
 example=[
  'The heater model from Lesson 7.1 is ΔT = b₀ + b₁P, with b₀ = 1 K and b₁ = 0.6 K/W. The temperature rises and predictions come from the lessons.',
  'The data are illustrative and synthetic. They are not from a real heater.',
 ],
 data_table='''Measured ΔT (K):    5   8  10
Predicted ΔT (K):   4  10   7
Training targets for a baseline (K): 4, 8, 10, 12''',
 steps=[
  dict(
   heading='Step 1. One prediction and its residual',
   explain='At P = 10 W, ΔT_predicted = 1 K + 0.6 K/W × 10 W = 7 K. The measured rise is 8 K. The residual is r = y − ŷ, measured minus predicted.',
   code='''# Step 1: prediction and residual (Lesson 7.1)
b0 = 1.0                  # intercept in K
b1 = 0.6                  # slope in K/W
power = 10.0              # heater power in W

predicted = b0 + b1 * power       # K
measured = 8.0                    # measured temperature rise in K
residual = measured - predicted   # K
print(f"Predicted rise: {predicted:.1f} K")
print(f"Residual: {residual:+.1f} K")''',
   expected_output='''Predicted rise: 7.0 K
Residual: +1.0 K''',
   output_explain='The prediction is 7 K and the residual is +1 K, as in Lesson 7.1. The positive sign means the prediction is below the measurement.'),
  dict(
   heading='Step 2. Residuals, MAE and RMSE for three observations',
   explain='Lesson 7.2 gives three measurements, [5, 8, 10] K, and three predictions, [4, 10, 7] K. MAE averages the absolute residuals. RMSE squares the residuals, averages them and takes the square root. Both are in kelvin.',
   code='''# Step 2: residuals, MAE and RMSE (Lesson 7.2)
measured = [5, 8, 10]     # measured temperature rises in K
predicted = [4, 10, 7]    # predicted temperature rises in K

residuals = []
for i in range(len(measured)):
    residuals.append(measured[i] - predicted[i])
print("Residuals (K):", residuals)

abs_total = 0
sq_total = 0
for r in residuals:
    abs_total += abs(r)
    sq_total += r ** 2
n = len(residuals)
mae = abs_total / n
rmse = (sq_total / n) ** 0.5
print(f"MAE:  {mae:.3f} K")
print(f"RMSE: {rmse:.3f} K")''',
   expected_output='''Residuals (K): [1, -2, 3]
MAE:  2.000 K
RMSE: 2.160 K''',
   output_explain='These match Lesson 7.2: residuals [1, −2, 3] K, MAE = 2 K and RMSE ≈ 2.160 K. RMSE is at least as large as MAE, because squaring gives the larger residual (3 K) more influence.'),
  dict(
   heading='Step 3. R² compares with predicting the mean',
   explain='R² = 1 − SSE/SST. SSE is the sum of the squared residuals. SST is the sum of the squared distances of the measurements from their own mean. The squared units cancel, so R² has no unit. A value below zero means the model did worse than predicting the mean.',
   code='''# Step 3: R-squared (Lesson 7.2)
mean_measured = sum(measured) / n
sse = sq_total                          # sum of squared residuals, in K²
sst = 0
for y in measured:
    sst += (y - mean_measured) ** 2     # in K²

r2 = 1 - sse / sst
print(f"SSE = {sse:.2f} K², SST = {sst:.2f} K²")
print(f"R²  = {r2:.4f}")''',
   expected_output='''SSE = 14.00 K², SST = 12.67 K²
R²  = -0.1053''',
   output_explain='R² ≈ −0.1053, as in Lesson 7.2. It is negative because the model’s squared error (14) is larger than the squared error of always predicting the mean (12.67). It is a comparison, not a safety threshold.'),
  dict(
   heading='Step 4. Compare with a training-mean baseline',
   explain='Lesson 7.3 asks you to compare with a training-mean baseline on the same evaluation examples. The baseline predicts the mean of the training targets for every example. Here the training targets are [4, 8, 10, 12] K. The evaluation examples are the same three measurements as in Step 2.',
   code='''# Step 4: training-mean baseline on the same evaluation examples
train_targets = [4, 8, 10, 12]               # training targets in K
baseline_value = sum(train_targets) / len(train_targets)

baseline_total = 0
for y in measured:
    baseline_total += abs(y - baseline_value)
baseline_mae = baseline_total / len(measured)

print(f"Baseline prediction for every example: {baseline_value:.1f} K")
print(f"Baseline MAE: {baseline_mae:.3f} K")
print(f"Model MAE:    {mae:.3f} K")
if baseline_mae < mae:
    print("The simple baseline has the lower MAE.")
else:
    print("The model has the lower MAE.")''',
   expected_output='''Baseline prediction for every example: 8.5 K
Baseline MAE: 1.833 K
Model MAE:    2.000 K
The simple baseline has the lower MAE.''',
   output_explain='The simple baseline beats the model on MAE here. Lesson 7.3 says to compare with a fair baseline and to report the result honestly. With only three evaluation examples, this comparison is also very uncertain.'),
 ],
 try_it=dict(
  step=1,
  instruction='Change a value and observe. In the Step 2 code, change `predicted = [4, 10, 7]` to `predicted = [4, 8, 7]`. Then run Steps 2 to 4 again.',
  change=('predicted = [4, 10, 7]    # predicted temperature rises in K', 'predicted = [4, 8, 7]     # predicted temperature rises in K'),
  expected_output='''Residuals (K): [1, 0, 3]
MAE:  1.333 K
RMSE: 1.826 K
SSE = 10.00 K², SST = 12.67 K²
R²  = 0.2105
Baseline prediction for every example: 8.5 K
Baseline MAE: 1.833 K
Model MAE:    1.333 K
The model has the lower MAE.''',
  expected_observation='One better prediction changes every metric. The residuals are smaller, so MAE and RMSE fall, and R² becomes positive. The model now beats the baseline on MAE. RMSE (1.826 K) is still larger than MAE (1.333 K), because the 3 K residual dominates it.'),
 limits=[
  'Three evaluation examples are far too few to support a conclusion. They are used here only to follow the arithmetic.',
  'The code does not split data, fit a model or plot residuals. Lesson 7.2 asks you to plot residuals against load, time and operating regime.',
  'If the evaluation targets were all equal, SST would be zero and R² would need an explicit rule (Lesson 7.2).',
  'The data are synthetic. A good score here says nothing about a real heater.',
 ],
 related='Lab 2 computes these metrics on a held-out test set after selecting a model on validation data.',
 notebook='walkthrough_m07.ipynb')

W['m08'] = dict(
 title='From scores to a confusion matrix',
 supports='Lesson 8.1 (sections “Declare the positive class” and “Select a threshold using validation”), Lesson 8.2 (section “Calculate the supplied example”) and Lesson 8.3 (section “Compare with the majority-class baseline”).',
 objective='Turn detector scores into fault decisions with a threshold, count TP, FP, FN and TN, and calculate accuracy, precision, recall and F1. Then see why accuracy alone misleads for rare faults, and how the threshold changes the counts.',
 prereqs=[
  'You need Lessons 8.1 to 8.3 and the Module 2 to 7 Code walkthroughs.',
  'No libraries are needed. Counting and dividing is enough to see what each metric asks.',
 ],
 python_ideas=[
  '`a >= b` is true when a is greater than or equal to b.',
  '`zip(list_a, list_b)` lets a `for` loop go through two lists at the same time. `for score, label in zip(scores, labels):` takes one item from each per pass.',
  'In an f-string, `{value:.1%}` shows a fraction as a percentage with one decimal digit. 0.94 becomes 94.0%.',
 ],
 example=[
  'The first example uses ten invented detector scores and the actual classes. A label of 1 means a real fault and 0 means healthy. Fault is the positive class. These are evaluation labels, not a judgement about what is desirable (Lesson 8.1).',
  'The scores are synthetic and are not calibrated probabilities. They are not from a trained or tested machinery detector.',
 ],
 data_table='''Score   0.95 0.80 0.65 0.55 0.45 0.40 0.30 0.20 0.15 0.05
Actual     1    1    0    1    1    0    0    0    0    0   (1 = fault)''',
 steps=[
  dict(
   heading='Step 1. Apply a threshold and count TP, FP, FN and TN',
   explain='Lesson 8.1 labels an example as a fault when the score is at least the threshold. You compare each decision with the actual class. A true positive is a fault predicted as a fault. A false negative is a missed fault. A false positive is a false alarm. A true negative is a healthy example predicted as healthy.',
   code='''# Step 1: threshold the scores and count the four outcomes (synthetic data)
scores = [0.95, 0.80, 0.65, 0.55, 0.45, 0.40, 0.30, 0.20, 0.15, 0.05]
actual = [1, 1, 0, 1, 1, 0, 0, 0, 0, 0]        # 1 = fault (positive class), 0 = healthy
threshold = 0.5

tp = fp = fn = tn = 0
for score, label in zip(scores, actual):
    predicted_fault = score >= threshold
    if predicted_fault and label == 1:
        tp += 1
    elif predicted_fault and label == 0:
        fp += 1
    elif (not predicted_fault) and label == 1:
        fn += 1
    else:
        tn += 1

print(f"Threshold {threshold}: TP={tp}, FP={fp}, FN={fn}, TN={tn}")''',
   expected_output='Threshold 0.5: TP=3, FP=1, FN=1, TN=5',
   output_explain='Four alerts were raised, and three of them were real faults. One real fault, with score 0.45, was missed because it fell below the threshold. One healthy example, with score 0.65, caused a false alarm.'),
  dict(
   heading='Step 2. The metrics for the lesson’s counts',
   explain='Lesson 8.2 gives TP = 8, FP = 2, FN = 4 and TN = 86, so N = 100. Each metric answers a different question. Accuracy: what fraction of all examples were right? Precision: what fraction of alerts were real faults? Recall: what fraction of real faults were found?',
   code='''# Step 2: metrics from the lesson's counts
tp, fp, fn, tn = 8, 2, 4, 86
n = tp + fp + fn + tn

accuracy = (tp + tn) / n
precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1 = 2 * tp / (2 * tp + fp + fn)

print(f"N = {n}")
print(f"Accuracy:  {accuracy:.1%}")
print(f"Precision: {precision:.1%}")
print(f"Recall:    {recall:.1%}")
print(f"F1:        {f1:.1%}")''',
   expected_output='''N = 100
Accuracy:  94.0%
Precision: 80.0%
Recall:    66.7%
F1:        72.7%''',
   output_explain='These match Lesson 8.2. The accuracy of 94% looks high, but the detector found only 8 of the 12 real faults. Four faults were missed. The high accuracy does not describe fault detection adequately on its own.'),
  dict(
   heading='Step 3. The always-healthy baseline',
   explain='Lesson 8.3 describes a dataset with 99 healthy examples and one fault. A rule that always predicts healthy never raises an alert. You calculate its accuracy and its fault recall.',
   code='''# Step 3: the majority-class baseline
healthy = 99
faults = 1
n = healthy + faults

# "always healthy": every healthy example is right, every fault is missed
tp, fp, fn, tn = 0, 0, faults, healthy

accuracy = (tp + tn) / n
recall = tp / (tp + fn)
print(f"Accuracy: {accuracy:.1%}")
print(f"Fault recall: {recall:.1%}")''',
   expected_output='''Accuracy: 99.0%
Fault recall: 0.0%''',
   output_explain='The baseline has 99% accuracy and detects no fault. As Lesson 8.3 says, a high accuracy can belong to a rule that never finds the event of interest. Compare a detector with this baseline and look at positive-class performance.'),
  dict(
   heading='Step 4. How the threshold changes the counts',
   explain='Lesson 8.1 says that lowering the threshold catches more faults but can raise more false alarms. You use the same ten scores from Step 1 with three thresholds. In a real project you would choose the threshold on validation data and then evaluate it once on the test data.',
   code='''# Step 4: the same scores with different thresholds
scores = [0.95, 0.80, 0.65, 0.55, 0.45, 0.40, 0.30, 0.20, 0.15, 0.05]
actual = [1, 1, 0, 1, 1, 0, 0, 0, 0, 0]

print("threshold  TP  FP  FN  TN  recall")
for threshold in [0.3, 0.5, 0.7]:
    tp = fp = fn = tn = 0
    for score, label in zip(scores, actual):
        predicted_fault = score >= threshold
        if predicted_fault and label == 1:
            tp += 1
        elif predicted_fault and label == 0:
            fp += 1
        elif (not predicted_fault) and label == 1:
            fn += 1
        else:
            tn += 1
    recall = tp / (tp + fn)
    print(f"{threshold:>9}  {tp:>2}  {fp:>2}  {fn:>2}  {tn:>2}  {recall:.0%}")''',
   expected_output='''threshold  TP  FP  FN  TN  recall
      0.3   4   3   0   3  100%
      0.5   3   1   1   5  75%
      0.7   2   0   2   6  50%''',
   output_explain='A lower threshold finds more faults (recall rises from 50% to 100%) but also raises more false alarms (FP rises from 0 to 3). The scores did not change. Only the decision rule changed. Which row is best depends on the cost of a missed fault compared with a false alarm (Lesson 8.3).'),
 ],
 try_it=dict(
  instruction='Change a value and observe. In the Step 4 code, change `for threshold in [0.3, 0.5, 0.7]:` to `for threshold in [0.1, 0.5, 0.9]:`. Then run Step 4 again.',
  change=('for threshold in [0.3, 0.5, 0.7]:', 'for threshold in [0.1, 0.5, 0.9]:'),
  expected_output='''threshold  TP  FP  FN  TN  recall
      0.1   4   5   0   1  100%
      0.5   3   1   1   5  75%
      0.9   1   0   3   6  25%''',
  expected_observation='At 0.1 almost everything is flagged: all four faults are found, but five of the six healthy examples raise an alarm. At 0.9 only the highest score is flagged, so three of the four faults are missed. Extreme thresholds trade one kind of error for the other.'),
 limits=[
  'Ten invented scores are far too few to choose a threshold. The example only shows how the counts move.',
  'The scores are not calibrated probabilities (Lesson 8.1). Choosing a cutoff does not show that a score is a probability.',
  'If there are no alerts, precision has a zero denominator and needs an explicit reporting rule (Lesson 8.2). The code above does not handle that case.',
  'Nothing here authorizes deployment. Real alerts need an engineering procedure with defined recipients, evidence and authority (Lesson 8.3).',
 ],
 related='Lab 3 selects a threshold on validation scores and reports a fixed test result with an always-healthy baseline.',
 notebook='walkthrough_m08.ipynb')

W['m09'] = dict(
 title='Units, neighbours, clusters and variance',
 supports='Lesson 9.1 (section “Unit scaling and method selection”), Lesson 9.3 (sections “Unsupervised grouping and compression” and “Feature scaling implications”).',
 objective='See three ideas from Module 9 in short examples. Distance-based methods depend on feature units. A k-means cluster count is your choice. PCA ranks directions by variance, not by usefulness.',
 prereqs=[
  'You need Lessons 9.1 to 9.3 and the Module 2 to 8 Code walkthroughs.',
  'Steps 2 and 3 use scikit-learn, which is already installed in Google Colab. You do not need to know how the algorithms work inside. The lessons ask you to recognize their roles.',
 ],
 python_ideas=[
  '`def name(arguments):` defines a function. You met it in the Module 5 walkthrough.',
  '`from sklearn.cluster import KMeans` and `from sklearn.decomposition import PCA` load two scikit-learn tools. `KMeans(n_clusters=2)` asks for two groups. `PCA()` finds directions in the data.',
  '`n_init=10` and `random_state=0` fix how k-means starts, so you get the same result every time (Lesson 6.3 on seeds).',
  '`.tolist()` turns a NumPy array into an ordinary list. `sorted(items)` sorts a list.',
 ],
 example=[
  'Step 1 compares nearest neighbours for the same points, with a length written in metres and then in millimetres. Steps 2 and 3 use six invented operating profiles, each with a load in kW and a vibration level in mm/s.',
  'All data are synthetic. The groups below are not fault classes.',
 ],
 data_table='''Step 1 (length in m, vibration in mm/s):
  A = (0.10, 5.0)   B = (0.50, 2.1)   query = (0.12, 2.0)
Steps 2 and 3 (load in kW, vibration in mm/s):
  (10, 1.0) (12, 1.2) (11, 1.1) (40, 3.0) (42, 3.2) (41, 3.1)''',
 steps=[
  dict(
   heading='Step 1. Changing units changes the nearest neighbour',
   explain='Lesson 9.1 says kNN uses distances in feature space. Changing a length from metres to millimetres multiplies its number by 1,000. The physical situation is the same, but the nearest neighbour can change. Here “distance” is the straight-line distance: square the differences, add them and take the square root.',
   code='''# Step 1: the same three points, with the length in m and then in mm
def distance(p, q):
    return ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** 0.5

def nearest(points, query):
    best_name = None
    best_distance = None
    for name, x, y in points:
        d = distance((x, y), query)
        if best_distance is None or d < best_distance:
            best_name = name
            best_distance = d
    return best_name

# features: (length, vibration in mm/s)
points_m = [("A", 0.10, 5.0), ("B", 0.50, 2.1)]
query_m = (0.12, 2.0)
points_mm = [("A", 100.0, 5.0), ("B", 500.0, 2.1)]
query_mm = (120.0, 2.0)

print("Nearest neighbour with length in m: ", nearest(points_m, query_m))
print("Nearest neighbour with length in mm:", nearest(points_mm, query_mm))''',
   expected_output='''Nearest neighbour with length in m:  B
Nearest neighbour with length in mm: A''',
   output_explain='The two runs describe the same physical points. Only the unit of one feature changed, and the answer changed. In millimetres, the length differences are about 1,000 times larger and dominate the distance. Distance-based methods need scaling that respects the physical units (Lesson 9.3).'),
  dict(
   heading='Step 2. PCA ranks by variance, not by usefulness',
   explain='PCA finds directions that capture the most variance in the data (Lesson 9.3). The `explained_variance_ratio_` values show the share of the total variance in each direction. Here the load changes much more than the vibration in these units, so the first direction is almost all the variance. High variance does not mean the direction is useful for finding a fault.',
   code='''# Step 2: PCA on six operating profiles (synthetic)
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

profiles = np.array([
    [10, 1.0], [12, 1.2], [11, 1.1],      # lower load
    [40, 3.0], [42, 3.2], [41, 3.1],      # higher load
])                                         # columns: load in kW, vibration in mm/s

pca = PCA()
pca.fit(profiles)
ratios = pca.explained_variance_ratio_
print(f"Share of variance, direction 1: {ratios[0]:.4f}")
print(f"Share of variance, direction 2: {ratios[1]:.4f}")''',
   expected_output='''Share of variance, direction 1: 1.0000
Share of variance, direction 2: 0.0000''',
   output_explain='The first direction holds almost all the variance, because the load differs by about 30 kW and the vibration by about 2 mm/s. PCA does not know which variable matters for a fault. A rare fault could sit in a low-variance direction and be thrown away. The ratios are dimensionless.'),
  dict(
   heading='Step 3. k-means: you choose the number of clusters',
   explain='k-means groups unlabelled points around centres (Lesson 9.3). You tell it how many groups to make. Here you ask for two. The sizes are sorted, because k-means may number its groups in any order.',
   code='''# Step 3: k-means with k = 2 on the same profiles
k = 2
kmeans = KMeans(n_clusters=k, n_init=10, random_state=0)
kmeans.fit(profiles)

sizes = np.bincount(kmeans.labels_)     # how many points are in each group
print("Group sizes:", sorted(sizes.tolist()))''',
   expected_output='Group sizes: [3, 3]',
   output_explain='The two groups match the lower-load and higher-load profiles, three points each. These groups are mathematical groups, not fault classes. They could be two load regimes or two machine types. Only measurement context and independent evidence can say what they mean (Lesson 9.3).'),
 ],
 try_it=dict(
  instruction='Change a value and observe. In the Step 3 code, change `k = 2` to `k = 3`. Then run Step 3 again.',
  change=('k = 2\n', 'k = 3\n'),
  expected_output='Group sizes: [1, 2, 3]',
  expected_observation='The algorithm splits one of the natural groups, because you asked for three. Which group it splits can depend on the starting point. It does not warn you, although the points do not form three natural groups. The number k is your choice and does not show how many real machine states exist. Lesson 9.3 suggests comparing several values of k, checking stability and checking the physical meaning.'),
 limits=[
  'Six invented points show the ideas. They are not a test of the methods. The lessons do not ask you to implement kNN, PCA or k-means.',
  'The walkthrough does not compare methods. Lesson 9.3 requires a fair comparison: preprocessing fitted inside each training fold, tuning on validation folds and one locked final test.',
  'Decision trees, random forests, boosting, logistic regression and SVMs are not shown. Lessons 9.1 and 9.2 ask you to recognize them, not to implement them.',
  'The group sizes for k = 2 and k = 3 were the same for 50 different random starts in a check. Which points share a group for k = 3 can still change with the start.',
 ],
 related='',
 notebook='walkthrough_m09.ipynb')
