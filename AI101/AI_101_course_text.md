# AI 101 for Mechanical Engineers

Version 1.0. Authored foundational course; synthetic teaching examples. Practical notebook work is assessed separately from browser knowledge checks.

## Module 1: What AI is and where it fits

Learning outcomes:
- Explain how AI, machine learning, deep learning, generative AI and data science relate to each other.
- Distinguish automation, robotics and learning, and explain narrow AI and the proposed idea of AGI.
- Identify the decision, measurements, model output and engineering action in a pump-inspection example, and explain what synthetic examples can and cannot show.

### A map of related ideas

## What you are expected to learn

You are expected to explain how artificial intelligence (AI), machine learning (ML), deep learning, generative AI and data science relate to each other. You should also be able to describe what each one does in an engineering system.

## Why this matters to mechanical engineers

Mechanical engineers work with measurements such as temperature, pressure, vibration, flow and current. AI and ML can help find patterns in these measurements or carry out a clearly defined task. Engineers still need to understand the physical system, check the results and take responsibility for decisions. This course explains when these tools can help and what evidence you need before acting on their outputs.

## 1. Artificial intelligence: the broad field

Artificial intelligence is a broad field concerned with systems that carry out tasks associated with intelligent behaviour. These systems can work in different ways. Some follow rules written in advance. Others search for solutions, use stored knowledge or learn patterns from examples. Calling a system AI therefore does not tell you whether it learns from data.

A fixed rule tells a system what to do. A learning method uses examples to learn part of its behaviour. In the infographic, the outer rectangle represents the whole field of AI. It includes several approaches, not just one algorithm.

## 2. Machine learning and deep learning

Machine learning is one approach within AI. An ML model uses examples to learn patterns or to adjust its parameters, which are the values that determine how it turns inputs into an output. For example, a pump-power predictor learns from measurements taken during pump operation. A bearing-fault classifier learns to distinguish the conditions represented in its training examples.

Deep learning is a type of ML that uses neural networks with multiple layers. The nested rectangles in the infographic show this relationship: AI includes ML, and ML includes deep learning. Some AI systems do not use neural networks, and some ML models do not use deep learning.

The term deep learning tells you how a model is built. It does not tell you what the output means or whether the result suits the engineering decision you want to make.

## 3. Classification and generation

Classification means predicting which category an input belongs to. For example, a surface-defect model might label an image as cracked or intact. A neural network with multiple layers can make this prediction without generating explanatory text, code or images.

Generative AI produces content. For example, a system that drafts a maintenance explanation is carrying out a generative task. A language model can use deep learning to generate text.

Deep learning and generation describe different aspects of a system. Deep learning describes the model approach. Generation describes the kind of output. For this reason, generative AI should not be drawn as a required fourth level inside the AI, ML and deep-learning rectangles.

When you describe a system, ask two questions. Which approach does it use? What output does it produce? A deep-learning classifier and a deep-learning text generator use the same broad approach but produce different kinds of output.

## 4. Data science includes the measurement workflow

Data science includes collecting measurements, cleaning data, analysing results, building models and communicating findings. It overlaps with AI and ML, but building a model is only one part of the work.

The slides show five stages: measure, clean, analyse, model and communicate. Each stage matters. Before you use a model to support an engineering explanation, check the sensor calibration information and investigate missing readings. A model can produce an output even when its measurements have problems, so the output alone does not show that the data are reliable.

## 5. Three components in one plant

Consider these three examples:

- A fixed over-temperature trip follows a rule and issues a trip command.
- A bearing-fault classifier learns from examples and produces an estimate related to a fault condition.
- A generative system drafts a maintenance explanation or report.

All three can operate in the same plant, but each does a different job, so each needs a different check. The trip needs its setpoint and response time confirmed. The fault estimate needs testing against independent examples. The maintenance draft needs checking against records and calculations, because a draft can read well and still contain an incorrect calculation or an unsupported claim about equipment behaviour.

## Check your understanding

Can a deep-learning system be non-generative? Try answering before opening the explanation.

ANSWER: Yes. A neural network with multiple layers can classify a surface image as cracked or intact without generating new explanatory content.

Why should generative AI not be shown as another compulsory level inside deep learning?

ANSWER: Generation describes the content a system produces. Deep learning describes the model approach it uses. These descriptions answer different questions.

## Key takeaways

- AI includes systems that learn from data and systems that use other approaches.
- ML is one approach within AI. Deep learning is ML using neural networks with multiple layers.
- Classification predicts a category. Generation produces content.
- Data science includes measurement, data preparation and communication, as well as modelling.
- Identify what each engineering component produces and what evidence is needed to check it.

Pause and explain: A deep-learning model labels each casting image as cracked or intact. Is it generative? Answer with the two questions: which approach does it use, and what output does it produce?

### Automation, robots and general intelligence

## What you are expected to learn

You are expected to distinguish automation, robotics and learning. You should also be able to explain narrow AI and the proposed idea of artificial general intelligence (AGI). The aim is to judge a system by what it does and what evidence supports it, not by its product label.

## 1. Automation describes process execution

Automation means carrying out a process with less manual intervention. A controller can do this by following fixed rules without learning from data. In the course example, a thermostat switches off above 30 °C. This is automation: the thermostat follows a temperature rule. It does not show learning from examples.

The 30 °C threshold is a teaching example, not a recommended setting for equipment. The key question is how the controller decides what to do. Was the rule specified in advance, or was the behaviour learned from data?

## 2. Robotics describes physical sensing and action

A robot is a physical machine that senses, decides and acts. Its decisions may come from conventional control rules, from AI or from a combination of the two. Calling a machine a robot does not tell you whether it learns.

For example, the slides show a conventional PID feedback controller connected to a robot and a sensor. The controller compares the measured output with a target value, called the setpoint, and applies specified feedback rules. This arrangement can work without learning from data. If a component does learn, identify that component and explain what it does.

Automation and robotics can overlap: a robot can carry out an automated process. Both can work without ML, and both can include ML. To decide whether learning is involved, examine how the system works.

## 3. Narrow AI and general intelligence

Narrow AI is designed for particular tasks. Familiar examples include filtering spam, estimating travel times and suggesting text completions. In engineering, a classifier that identifies a defined set of defects is narrow AI. Testing it gives evidence about those tasks under the conditions tested. Doing one task well does not show that a system can perform unrelated tasks or understands more broadly.

AGI refers to proposed AI capabilities that would apply broadly across tasks. People disagree about how to define and test it, so the label alone does not show that a system can do every task. This course does not claim that a current assistant has human understanding or can reliably handle every engineering problem.

For example, an assistant may produce fluent text. That fluency does not provide the evidence or authority needed to approve a pressure-vessel design. Always check the task, the supporting evidence and the actions the system is allowed to take.

## 4. Five questions for evaluating a system

Use the sequence in the slides to describe a system:

- Inputs: What information does the system receive?
- Learned components: Which parts, if any, learn from data?
- Outputs: What does each component produce?
- Permitted actions: What is the system allowed to do with that output?
- Failure consequences: What happens if the output or action is wrong?

These questions bring out details that a product label may leave out. They also separate a recommendation from an action the system has permission to carry out. A maintenance explanation, a classification result and a physical control command each need checks suited to their purpose.

## Worked example: a bearing alert

Consider a hypothetical bearing-alert system that uses vibration measurements. Its inputs are measurements available before the maintenance decision. A trained classifier uses them to estimate a defined condition, such as healthy or needs inspection. The alert is a reason to investigate, not a confirmed diagnosis.

A responsible procedure sends the alert to a qualified person for review. It does not assume that every alert requires an automatic shutdown. Before using the system, check how often it misses faults and how often it raises false alarms. Use representative examples whose conditions have been checked independently.

A similar classification method could be explored on a hypothetical garment-production line, where an image model flags a suspected fabric defect for inspection. This is a possible application, not a claim about a system in any particular factory.

## 5. Matching claims with evidence

A fixed controller shows that a system can follow a specified rule. To call a component ML, check that it actually learns from data. A robot arm shows physical sensing or action, but you still need to examine how it is controlled. A classifier needs performance evidence for its defined task. An AGI claim needs a clear definition and suitable tests.

Describe each component separately. This makes it easier to explain what the machine does, where learning is used and who is responsible for checking its outputs.

## Check your understanding

Is a conventional PID-controlled robot necessarily using ML?

ANSWER: No. It can follow specified feedback rules without learning from data. If another component learns, identify that component separately.

Does a thermostat switching off above 30 °C demonstrate AGI?

ANSWER: No. It shows a thermostat following a fixed automation rule. It provides no evidence of broad general capability.

## Key takeaways

- Automation reduces manual intervention. Robotics involves machines that sense, decide and act.
- Either can use conventional control, AI or a combination.
- The word robot does not tell you whether ML is involved.
- Narrow AI handles defined tasks. People still disagree about how to define and test AGI.
- Check inputs, learning, outputs, permitted actions and the consequences of errors.

Pause and explain: A robot arm is driven by a conventional PID controller. Is it using ML? What would you need to find out before calling any part of it ML?

### Start with an engineering decision

## What you are expected to learn

You are expected to use the pump-inspection example to identify four things: the decision to support, the measurements available, the model output and the engineering action. You should also be able to explain what synthetic teaching examples can and cannot demonstrate.

## 1. The engineering decision comes first

Consider a pump whose vibration and bearing temperature are increasing. Start with a question: should an inspection be requested? This gives the project a clear purpose before you choose an algorithm.

Choosing an algorithm does not, by itself, tell you who will use the result, what information is available or what happens if the result is wrong. State the decision you want to support first. Then consider how a model could help.

## 2. Measurements, model output and inspection

The slides divide the maintenance process into separate stages:

- Inputs: vibration and bearing-temperature measurements available before the decision.
- Model processing: a detector trained on examples uses those measurements.
- Output: a fault score or alert.
- Engineering review: the engineer reviews the output and the evidence behind it.
- Decision: request an inspection when the defined procedure calls for one.

The slides express vibration in millimetres per second and bearing temperature in degrees Celsius. They give no numerical operating limits for either quantity, so you cannot use this example to set limits.

Keep the stages in order. The model supplies information for the decision. The engineer decides what action is appropriate and under which conditions.

## 3. Success includes error consequences

A useful system detects faults while keeping false alarms manageable. Missing a fault matters, but repeated false alarms also make an inspection system less useful, because people stop trusting its alerts.

The lesson sets no numerical performance target and no score at which an alert should be issued. Its purpose is to show how to define the decision and weigh the consequences of errors. It does not describe a detector ready for use on equipment.

## 4. A fault score is an estimate

The course uses the illustrative output "Fault score = 0.8". The score is dimensionless, meaning it has no physical unit. It is a model estimate, and it is not permission to keep operating the pump.

The example does not explain how the score was calculated. A score is a calibrated probability only if, among many cases scoring 0.8, about 80% really are faults. Nothing here shows that, so do not read 0.8 as an 80% chance of failure just because it lies between zero and one.

Before acting on a score, check measurement quality, operating limits and whether the model has been validated, meaning tested on examples that were not used to build it. A practical description also names who will use the result, the conditions in which the system is intended to work, called the operating domain, and the escalation path, which is the route for passing a concern to the responsible decision-maker. This lesson gives no procedure for particular equipment.

## 5. Different components require different checks

The slides distinguish three components:

- A fixed trip follows an automation rule when its specified condition occurs.
- A learned detector uses patterns learned from examples to predict a fault-related score. Check its performance on examples that were not used to fit the model.
- A maintenance assistant generates text. Check that text against the relevant records.

Each check answers a different question. An accurate maintenance explanation does not show that the detector performs well, and a good detector does not make a generated explanation correct.

## 6. Synthetic examples and physical validation

Synthetic examples are constructed for teaching. They help you practise analytical methods and think about what evidence is needed and what could happen if a result is wrong.

They do not show that a real machine is safe or that a maintenance recommendation is valid. When you discuss a result, say what the example demonstrates and what still needs to be checked on physical equipment.

## Check your understanding

State the decision, two inputs and one output in the pump example.

ANSWER: The decision is whether to request an inspection. The inputs are vibration and bearing temperature measured before the decision. The output can be a fault alert or fault score.

Does a fault score of 0.8 authorize continued operation?

ANSWER: No. It is a model estimate. Engineers remain responsible for checking operating limits, measurement quality and model validation, and for passing concerns along the escalation path.

## Key takeaways

- Define the engineering decision before choosing an algorithm.
- Identify the measurements available before the decision and the output the model should produce.
- Consider both missed faults and false alarms.
- Keep model estimates separate from decisions about equipment operation.
- State who will use the output, its operating domain and the escalation path for concerns.
- Synthetic teaching examples do not validate recommendations for real machinery.

Pause and explain: For one mechanical-engineering application, state the decision, two inputs available before that decision, the model output and who reviews it.

### Terms

**AI**: AI is a broad field. It includes systems that carry out tasks associated with intelligent behaviour. Example: A system can use search to plan a task or learn from examples to detect faults.

**Machine learning**: Machine learning uses data to learn patterns or adjust model parameters. Example: Train a model to predict pump power using measured examples.

**Deep learning**: Deep learning is machine learning that uses neural networks with multiple layers. Example: A convolutional neural network (CNN) can identify surface defects.

**Generative AI**: Generative AI produces content, such as text, code or images. Example: Ask it to draft a Python function, then test the function.

**Data science**: Data science includes collecting data, cleaning it, analysing it, building models and explaining the results. Example: Check calibration information and missing readings before fitting a model.

**Automation**: Automation carries out a process with less manual intervention. It can use fixed rules. Example: A thermostat switches at a set temperature.

**Robotics**: Robotics involves physical machines that sense, decide and act. Example: A robot arm can use conventional control without learning from data.

**Narrow AI**: Narrow AI is designed for particular tasks. Example: A classifier identifies a defined set of defects.

**AGI**: AGI refers to proposed AI capabilities that would apply broadly across tasks. There is no single agreed test for it. Example: Check how AGI is defined. Do not assume that an assistant meets that definition.


## Module 2: Engineering problems and modelling approaches

Learning outcomes:
- Choose physics-based, data-driven or hybrid modelling for a stated purpose.
- Distinguish prediction, forecasting, diagnosis, control and optimization.

### Physics, data and hybrid models

A physics-based model uses governing relationships, parameters and boundary or initial conditions. For a pump, hydraulic power is Δp × Q, where pressure rise is in pascals and volumetric flow is in m³/s. The product has units W. Estimating shaft or electrical power requires efficiencies and other losses.

A data-driven model estimates a relationship from observations. It might predict electrical power from flow, pressure rise and speed without explicitly imposing the power equation. A hybrid approach combines physical structure with a learned component, such as learning a residual correction to a physics prediction.

The choice depends on what is known, the quality of measurements, the operating range and the purpose. A model with lower error is not automatically more defensible: its inputs may be unavailable, it may violate limits, or its test may be flawed.

Pause and explain: Calculate hydraulic power for Δp=100,000 Pa and Q=0.02 m³/s.

### Different questions need different outputs

Prediction estimates an unknown outcome from inputs. Forecasting predicts a future outcome and must use information available at its issue time. Diagnosis attempts to identify a condition or cause; a predictive association alone does not prove the physical cause. Control chooses actions over time to regulate a system. Optimization searches for choices that improve an objective subject to limits.

Example: estimating tomorrow's HVAC electricity is forecasting. Flagging an unusual compressor vibration is anomaly detection; declaring a bearing damaged requires additional evidence. Choosing a setpoint is control. Choosing insulation thickness to reduce a cost objective is design optimization.

Do not confuse mathematical optimization during ML training with engineering design optimization. One adjusts model parameters to reduce a training loss; the other adjusts design or operational variables to improve an engineering objective.

Pause and explain: Explain why predicting pump power does not itself optimize pump operation.

### When ML is worth considering

Begin with the simplest adequate baseline. If a trusted equation meets the required accuracy and speed, ML may add maintenance burden rather than value. ML can help when patterns are hard to specify, observations are plentiful, or a costly simulator needs an approximate response model.

Before proposing ML, state the decision, inputs available at use time, output, success criterion and comparison baseline. Ask whether representative data exist. A data model trained at one speed or on one machine may fail at another. A physics model also needs validation of assumptions; physics-based does not mean automatically correct.

Worked example: Δp=100 kPa, Q=0.02 m³/s and efficiency=0.8 imply 2,500 W input power for that idealized relationship. A measured 2,800 W creates a +300 W residual. A hybrid model might learn such residuals, while retaining the physics calculation.

Pause and explain: Name a baseline and a validation requirement for a power-prediction project.

### Terms

**Physics-based model**: A model using physical relationships and stated assumptions. Example: Hydraulic power = pressure rise × flow.

**Data-driven model**: A model inferred from observed input–output data. Example: Predict electrical power from operating records.

**Hybrid model**: A model combining physical structure with learned components. Example: Learn a correction to a datasheet model.

**Simulation**: Computational execution of a model under specified conditions. Example: Simulate a heat-transfer transient.

**Prediction**: An estimate of an unknown output from inputs. Example: Estimate power for a new operating condition.

**Forecasting**: Prediction of a future outcome using available past or forecast inputs. Example: Predict tomorrow’s PV energy.

**Diagnosis**: Identifying a condition or explanation from evidence. Example: Confirm bearing damage through inspection.

**Control**: Selecting actions over time to regulate behaviour. Example: Change fan speed to maintain temperature.

**Optimization**: Searching for choices that improve an objective subject to limits. Example: Choose a geometry with low pressure drop.


## Module 3: The vocabulary of engineering data

Learning outcomes:
- Identify samples, features, targets, labels and metadata.
- Distinguish trustworthy references from error-free truth.

### Read a table as a learning problem

A sample is one example. A dataset contains examples. In a pump table, one row might represent a steady operating test, with columns for flow, pressure rise, speed and measured electrical power. Features are model inputs; the target is what we want to predict. For regression it may be a number; for classification a category.

The word label often means the supplied target annotation, especially for classes. An inspected bearing state can label a vibration example. A feature is not inherently an input for every problem: electrical power is the target in one study and a feature in a fault-detection study.

Write X for a feature matrix of shape (n,d), where n is the sample count and d the feature count. A single scalar target for every example forms y of shape (n,). These conventions help distinguish rows from columns and catch accidental misalignment.

Pause and explain: A table has 120 tests, 3 inputs and one scalar target. State the shapes of X and y.

### Measurements need context

Numbers without units and metadata are hard to interpret. Metadata describe how data were obtained: sensor ID, calibration, timestamp, sampling frequency, window length, operating state and units. Distinguish a raw time sample from a feature computed over a window, such as vibration RMS over one second.

Numerical features can be continuous, such as temperature, or counts, such as cycles. Categorical features describe groups such as material grade or machine ID. An ID used as a number is not necessarily a physical quantity; distance between IDs may have no meaning.

Reference measurements and annotations are often called ground truth. That does not make them error-free. A miscalibrated sensor, uncertain inspection or poorly aligned timestamp can corrupt a target. Record provenance and ask what the reference actually supports.

Pause and explain: Why is machine ID 12 not necessarily twice machine ID 6?

### Available inputs and causal claims

A valid predictor uses information available when the decision is made. A post-failure repair code is not a valid input for predicting that failure beforehand. A signal-window feature must not include future measurements when used for an earlier alarm.

Correlation describes association. Prediction asks whether inputs improve estimates on relevant unseen examples. Causation asks whether an intervention changes the outcome under appropriate conditions. A temperature sensor may correlate with a fault because load changes both; changing the sensor reading would not repair the machine.

Worked example: increasing flow and motor current together in records suggests association. Whether changing flow causes a particular current change depends on pump physics, controls and experimental conditions. A predictive coefficient alone does not establish that relationship.

Pause and explain: Give one tempting feature that would not exist before a maintenance decision.

### Terms

**Dataset**: A collection of examples with associated variables and context. Example: A table of 120 pump tests.

**Sample**: One example in a learning problem. Example: A steady operating test or a labelled signal window.

**Feature**: An input variable used by a model. Example: Pressure rise available before predicting power.

**Target**: The output quantity or category to be learned. Example: Measured electrical power.

**Label**: A supplied target annotation for an example. Example: Inspection confirms a bearing fault.

**Ground truth**: The reference value or annotation used for comparison; it may contain error. Example: A calibrated but still uncertain power measurement.

**Metadata**: Information describing data acquisition and meaning. Example: Units, sensor calibration and sampling frequency.

**Categorical data**: Values representing categories rather than numerical magnitudes. Example: Material grade or machine type.

**Correlation**: Statistical association between variables. Example: Flow and current change together.

**Causation**: A relationship in which an intervention affects an outcome. Example: Test the effect of flow changes under controlled conditions.


## Module 4: How machines learn

Learning outcomes:
- Recognize learning setups from their feedback.
- Classify regression, classification, clustering and anomaly tasks.

### Learning with and without labels

Supervised learning uses input–target pairs. Regression predicts a continuous value such as tool wear in mm. Classification predicts a category or class probability such as intact versus cracked. The task is determined by the target, not by whether the inputs are numbers or images.

Unsupervised learning looks for structure without target labels for the specified task. Clustering groups similar observations. A cluster might reflect load regime, machine type or sensor drift rather than health. Anomaly detection flags deviations from learned normal behaviour; it can use different learning setups depending on available labels.

An anomaly is a reason to investigate, not proof of a fault. For example, unusual current might indicate a new load, changed control settings, faulty sensing or actual mechanical damage.

Pause and explain: What additional evidence would turn an anomaly alert into a confirmed fault label?

### Self-supervised targets come from the data

Self-supervised learning constructs targets from the data themselves. Hide part of a signal and learn to reconstruct it, or predict a next token from preceding tokens. This is different from requiring a human to label every example.

The fact that data lack manually supplied fault labels does not mean training has no objective. A self-supervised task still has targets and a loss, but the target-generation rule comes from the observed data. Representations learned this way may later be adapted to labelled tasks.

An architecture does not determine a unique learning setup. A neural network may be trained with human-labelled targets, self-supervised targets or reinforcement feedback. Keep the task, feedback and model family as separate concepts.

Pause and explain: In masked-signal reconstruction, where does the target come from?

### Reinforcement learning uses interaction

In reinforcement learning, an agent observes a state, selects an action and receives feedback through rewards from an environment. A policy maps information to actions. The objective is usually cumulative reward, so a useful action now can have consequences later.

A battery controller might trade energy cost against degradation. A robot policy might select motor commands. Rewards must express the intended goal, while safety limits constrain allowable actions. A poorly specified reward can encourage behaviour that maximizes a number while violating the actual purpose.

Use simulated environments for beginner exercises. This course does not authorize experimentation on machinery. Distinguish RL from ordinary supervised prediction: labelled input–output examples alone do not establish interactive reward learning.

Pause and explain: Name a state, an action and a reward for a simulated thermal controller.

### Terms

**Supervised learning**: Learning from input–target pairs. Example: Predict power using known measured power targets.

**Unsupervised learning**: Finding structure without supplied target labels for the task. Example: Group operating profiles.

**Self-supervised learning**: Learning with targets constructed from the data themselves. Example: Reconstruct a masked vibration segment.

**Reinforcement learning**: Learning decisions through interaction and rewards. Example: A simulated controller learns a policy.

**Regression**: Predicting a continuous numerical output. Example: Predict temperature in °C.

**Classification**: Predicting a class or class probabilities. Example: Classify normal versus fault.

**Clustering**: Grouping examples by a similarity criterion. Example: Group similar load profiles.

**Anomaly detection**: Flagging observations that deviate from expected behaviour. Example: Flag an unusual sensor pattern for investigation.

**Policy**: A rule or model for choosing actions from available state information. Example: Choose battery charge rate.

**Reward**: Feedback used to evaluate actions in reinforcement learning. Example: Reward comfort and penalize energy consumption.


## Module 5: Preparing engineering data

Learning outcomes:
- Explain cleaning, imputation, scaling and encoding.
- Fit preprocessing only on development training data.

### Investigate before changing readings

Inspect distributions, timestamps, missing values and physically impossible readings. A negative absolute pressure, mixed W and kW columns, or duplicated timestamp can be a data problem. A high temperature may instead be the event you need to detect. Do not delete every unusual reading merely to improve a score.

Missingness can be informative: a sensor may drop out during vibration or communication overload. Imputation fills missing values according to a declared rule; it does not recover the original measurement. Document which values were changed and why.

Worked example: readings [20,22,missing,24] have a mean of 22 over the observed values. Mean imputation inserts 22, but artificially reduces visible variability. When fitting a predictive pipeline, estimate this replacement from training data, not the full dataset.

Pause and explain: Why can removing all high-temperature readings damage a fault-detection dataset?

### Scaling and encoding

Distance-based methods and neural training can be sensitive to feature scale. Min–max scaling uses (x−minimum)/(maximum−minimum). Standardization often uses (x−mean)/standard deviation. Neither changes the physical units of the original observation; keep the original units for reporting and interpretation.

For bounds 0–100°C, 25°C becomes 0.25 under that min–max transform. With training mean 40°C and standard deviation 10°C, 25°C becomes −1.5 under standardization. For a constant feature, the denominator needs an explicit handling rule.

Encoding represents categories numerically. One-hot encoding assigns indicator columns rather than treating machine types A, B and C as magnitudes 1, 2 and 3. Fit category handling on training data and decide how unseen categories will be treated.

Pause and explain: Standardize 60°C using training mean 40°C and standard deviation 10°C.

### Features and repeatable pipelines

Feature engineering uses knowledge to build useful inputs: pressure rise, hydraulic power ΔpQ, vibration RMS, frequency-band energy or temperature above ambient. A feature should be meaningful and available at prediction time. Windowed signal features must not silently include future samples.

A pipeline bundles preprocessing and modelling so that fitting and later inference follow consistent steps. Split data first; fit scalers, imputers and learned feature selection within training folds. Apply the fitted transformation to validation and test inputs without refitting on them.

If sensor units change from W to kW, the same stored numerical model will not necessarily interpret them correctly. Record the expected input contract. Cleaning and feature transformations are part of the model's evidence trail, not invisible preparation.

Pause and explain: Which statistics should a scaler use when transforming the final test set?

### Terms

**Noise**: Variation or error that obscures the quantity of interest. Example: A fluctuating sensor reading.

**Outlier**: An observation unusual relative to a comparison population. Example: A large temperature may be a fault or a measurement error.

**Imputation**: Filling missing values by a stated rule. Example: Use the training median for a missing feature.

**Scaling**: Transforming feature magnitudes to a chosen scale. Example: Map geometry bounds to [0,1].

**Standardization**: A transform commonly subtracting a training mean and dividing by a training standard deviation. Example: A temperature becomes a z-score.

**Normalization**: An overloaded term for rescaling; state the exact rule. Example: This course specifies min–max scaling when using that transform.

**Encoding**: Representing categories in a numerical form. Example: One-hot encode machine type.

**Feature engineering**: Constructing useful inputs using knowledge of the problem. Example: Use ΔpQ as a power-related feature.

**Pipeline**: A repeatable chain of preprocessing and modelling. Example: Fit an imputer and model inside each training fold.


## Module 6: Models, training and inference

Learning outcomes:
- Separate training from inference and parameters from hyperparameters.
- Interpret loss and compare against a baseline.

### A model and its learning algorithm

A model is a representation used to map inputs to outputs. A linear model might be ŷ=b₀+b₁x. A learning algorithm is the procedure that obtains or updates its parameters from data. Least squares estimates coefficients by minimizing a sum of squared residuals. Different algorithms can fit related models.

Training, also called fitting, uses examples to determine parameter values. Inference applies the fitted model to new inputs. Routine prediction does not automatically modify coefficients. Retraining is a separate operation with its own data and validation requirements.

Worked example: ŷ=2+3x has intercept 2 and slope 3. At x=4, inference returns 14. Changing x changes the output. Fitting new data may change 2 or 3; those changes are parameter updates, not simply more inference.

Pause and explain: Predict ŷ for x=5 with ŷ=2+3x. Which numbers are parameters?

### Parameters and hyperparameters

Parameters are fitted values: regression coefficients, neural weights and biases, or tree split values. Hyperparameters govern structure or training: tree-depth limits, learning rate or batch size. They are usually selected through validation rather than fitted by the same parameter-learning operation.

The distinction depends on the method; avoid defining a parameter only as any number in code. A fixed physical efficiency is a model assumption or supplied parameter in the engineering model, but it is not a learned ML parameter unless estimated in fitting.

A training loss quantifies disagreement with the chosen objective. It is not a universal quality score. Minimizing squared error can favour average performance while hiding rare large failures. The loss, evaluation metrics and engineering acceptance criterion may differ.

Pause and explain: Is a fitted slope or a chosen maximum tree depth a hyperparameter?

### Baselines prevent empty success claims

A baseline is a simple comparison approach. For regression, predict the training mean or use a trusted physical relationship. For classification, compare with a majority-class rule and appropriate fault-sensitive metrics. Baselines must use the same evaluation examples and information availability.

Suppose a model has MAE 1.2 kW and a physics baseline has MAE 0.8 kW on the same held-out tests. More elaborate training has not earned a benefit on that metric. Cost, interpretability and operating-range evidence still matter, but “uses AI” is not a performance result.

Keep a record of the data split, preprocessing and version. A random seed helps repeat a random procedure; it does not prove accuracy, eliminate uncertainty or make a biased dataset representative.

Pause and explain: What additional information is needed to interpret “our MAE is 1.2 kW”?

### Terms

**Model**: A representation that maps inputs to outputs or describes a relationship. Example: ŷ=b₀+b₁x.

**Algorithm**: A procedure for performing a computation, including fitting a model. Example: Least squares estimates line coefficients.

**Training**: Using data to fit or update model parameters. Example: Estimate slope and intercept.

**Inference**: Applying a fitted model to an input. Example: Predict power for a new operating point.

**Parameter**: A value fitted within the model. Example: A learned regression slope.

**Hyperparameter**: A setting controlling model structure or training. Example: Maximum tree depth or learning rate.

**Loss function**: The training objective measuring discrepancy or another penalty. Example: Mean squared error.

**Baseline**: A simple comparison method evaluated fairly. Example: A physical power equation or training-mean predictor.

**Random seed**: An initialization value for a pseudorandom procedure. Example: Repeat the same train/validation split.


## Module 7: Your first regression model

Learning outcomes:
- Interpret slope, residuals, MAE, RMSE and R².
- Evaluate on held-out data and report units.

### Fit a line and interpret coefficients

Linear regression models a numerical response. For temperature rise ΔT=b₀+b₁P, P is heater power in W and ΔT in K. The slope has units K/W; the intercept has units K. A physical interpretation requires appropriate assumptions and measurement design, not just a fitted value.

Least squares minimizes squared residuals. This is linearity in the coefficients; a polynomial with coefficients fitted by least squares is also a linear model in that sense. This course begins with a straight line because it makes predictions and errors visible.

Worked example: ΔT=1+0.6P gives 7 K at 10 W. If the measured rise is 8 K, the observation-minus-prediction residual is +1 K. Below, sliders adjust the line on illustrative data. The interaction changes a hypothesis; it does not perform a new experiment.

Pause and explain: What units must the slope have when predicting K from W?

### Three useful metrics and their limits

This course defines residual r=y−ŷ; positive residual means underprediction. MAE averages |r|. RMSE is the square root of the average r² and weights larger errors more strongly. Both use target units. For residuals 1,−2,3 K, MAE=2 K and RMSE=√(14/3)≈2.160 K.

R²=1−SSE/SST compares squared errors with predictions equal to the evaluation-set mean. It is unitless and can be negative. A high R² does not establish causation, low engineering error or safety. When the evaluation target is constant, the usual SST denominator is zero; handle that case rather than silently dividing.

RMSE≥MAE for the same errors, with equality when their absolute magnitudes are all equal. Also inspect residual plots by load, time and operating regime. Aggregate error can hide a narrow region with severe failures.

Pause and explain: For errors −2 and +2 K, are MAE and RMSE equal?

### A minimal, honest regression workflow

Define the output and available inputs. Inspect measurements and units. Set aside relevant unseen data. Fit preprocessing and the model on training data; select among choices using validation. Compare with a training-mean and, where available, physical baseline. Evaluate the locked model on the final test.

Lab 2 uses independent synthetic pump operating designs. It compares ordinary input features with hydraulic power as a physical feature. Its random split is appropriate for this stated independent-design teaching problem; forecasting requires a different split. The reference reports test metrics only after validation selection.

A regression result should state units, data provenance, split strategy, baseline performance and domain limits. A model trained on one laboratory pump does not automatically transfer to every pump.

Pause and explain: State two limitations to include alongside a regression score.

### Terms

**Linear regression**: A regression model linear in its fitted coefficients. Example: Fit temperature rise versus power.

**Coefficient**: A fitted factor multiplying a model term. Example: A slope measured in K/W.

**Intercept**: The additive constant of a fitted model. Example: Predicted rise at zero input under the model.

**Residual**: Observation minus prediction in this course. Example: Measured 8 K minus predicted 7 K gives +1 K.

**MAE**: Mean absolute prediction error. Example: Average |y−ŷ| in kW.

**RMSE**: Square root of mean squared prediction error. Example: Large errors contribute strongly.

**R²**: One minus squared error relative to evaluation-mean squared deviations. Example: A relative score, not an error in watts.


## Module 8: Classification and fault detection

Learning outcomes:
- Read a confusion matrix and calculate precision and recall.
- Explain thresholds and class imbalance.

### Classes, scores and thresholds

A classifier predicts a category or a score associated with a class. A binary detector can label “fault” when its score exceeds a threshold. Some scores are probabilities; others are decision values. A number between zero and one is not automatically a calibrated probability.

The positive class must be declared. Here fault is positive and healthy is negative. TP means a detected fault; FN a missed fault; FP a false alarm; TN a correctly recognized healthy example. A confusion matrix records these counts for a specified threshold and evaluation dataset.

Threshold selection changes decisions. On fixed scores, lowering the threshold generally catches more faults and also labels more healthy cases as faults. Select the threshold on validation data in light of missed-fault and false-alarm consequences, then test it once.

Pause and explain: If fault is positive, what does a false negative represent?

### Read metrics by their question

Accuracy=(TP+TN)/N asks what fraction of all examples were correctly classified. Precision=TP/(TP+FP) asks how many alerts were actual faults. Recall=TP/(TP+FN) asks how many actual faults were detected. F1=2TP/(2TP+FP+FN) combines precision and recall in a particular way; it is not a universal safety objective.

Worked example: TP=8, FP=2, FN=4, TN=86 gives accuracy 94%, precision 80%, recall 66.7% and F1≈72.7%. The strong accuracy hides four missed faults. A denominator of zero needs an explicit reporting rule: no alerts does not provide evidence of useful positive-class precision.

ROC-AUC summarizes ranking behaviour across thresholds. Recognize the term here; for rare faults, also inspect precision–recall performance and class counts. No single number replaces operating-domain evidence.

Pause and explain: Calculate precision and recall for TP=8, FP=2, FN=4.

### Imbalance and deployment consequences

Class imbalance means some classes are much more frequent than others. With 99 healthy examples and one fault, always predicting healthy gives 99% accuracy and zero fault recall. Compare against that baseline, not merely against an impressive-looking accuracy figure.

Lab 3 uses synthetic scores and labels to demonstrate threshold selection. It is not a trained or calibrated machinery detector. Record TP, FP, FN and TN; choose a threshold using validation examples; evaluate a separate fixed test population.

Different machinery can have different costs of missed alarms. A classroom activity can illustrate these trade-offs but cannot approve deployment. State who receives alerts, when an inspection is needed and what evidence is required before acting.

Pause and explain: Why can a high-accuracy detector still be useless for rare faults?

### Terms

**Decision threshold**: A cutoff converting a model score into a decision. Example: Flag fault when score≥0.6.

**Confusion matrix**: Counts of actual and predicted classes. Example: Record TP, FP, FN and TN.

**True positive**: An actual positive correctly detected. Example: A fault correctly flagged.

**False positive**: A negative incorrectly labelled positive. Example: A healthy bearing triggers an alert.

**False negative**: A positive incorrectly labelled negative. Example: A fault is missed.

**Accuracy**: Fraction of all examples correctly classified. Example: (TP+TN)/N.

**Precision**: Fraction of positive predictions that are actual positives. Example: How many alerts were faults?

**Recall**: Fraction of actual positives detected. Example: How many faults were found?

**F1**: Harmonic mean of precision and recall when defined. Example: 2TP/(2TP+FP+FN).

**Class imbalance**: Unequal prevalence of target classes. Example: Faults are rare relative to healthy periods.

**ROC-AUC**: A measure summarizing discrimination through a ROC curve across thresholds. Example: Evaluate ranking, while checking relevant operating metrics too.


## Module 9: Recognizing common ML methods

Learning outcomes:
- Describe the intuition and role of common model families.
- Choose methods by task and evidence, not complexity alone.

### Lines, neighbours and separating boundaries

Linear regression predicts a number using a weighted combination. Logistic regression, despite its name, is commonly used for classification and estimates class probabilities through a link function. Neither name alone establishes performance on your data.

k-nearest neighbours uses nearby examples to estimate an output. Distance depends on scaling and on whether the selected features are meaningful. A support vector machine learns a separating boundary for classification; related support-vector methods can also perform regression. Kernels allow some methods to express nonlinear relations.

The purpose here is recognition, not implementing every method. Ask: what output is needed, what structure is assumed, how much data exist, and how will unseen performance be checked? A method suited to small tabular datasets may not be the first choice for raw images.

Pause and explain: Why could a distance-based method change after switching a length feature from m to mm?

### Trees and ensembles

A decision tree uses tests on features to divide examples into regions, then predicts within each region. A small tree can be inspected; a deep tree can overfit. A regression tree's piecewise predictions are different from a smooth response equation.

An ensemble combines multiple models. A random forest uses randomized trees and aggregates their predictions. Boosting adds models sequentially to reduce the remaining objective errors. These are different constructions, not just synonyms for more trees.

In engineering, a tree may learn a threshold involving load and vibration. Such a rule can support prediction but does not automatically establish a causal fault limit. Validate on relevant machines and operating regimes; do not read learned thresholds as manufacturer-approved limits.

Pause and explain: Explain one difference between a random forest and boosting.

### Grouping, compression and fair selection

k-means forms clusters around centres by minimizing a within-cluster distance objective. The number of clusters is a setting to choose, not a known number of physical faults. Principal component analysis, PCA, projects data onto directions of high variance. High variance is not necessarily high task relevance.

Scaling can substantially change both methods. A large-magnitude pressure variable may dominate distances while a smaller vibration feature matters for faults. Choose preprocessing with the task and units in mind.

Compare candidate models on common development data, with preprocessing inside each fold. Tune on validation and evaluate a locked choice on final test data. A complex method should earn its added cost and maintenance burden through evidence.

Pause and explain: Could the direction of greatest variance be unrelated to a rare fault? Explain.

### Terms

**Logistic regression**: A model commonly used to estimate class probabilities. Example: Estimate a binary fault probability.

**Decision tree**: A model dividing inputs through feature tests. Example: Split by load and vibration.

**Ensemble**: A combination of multiple models. Example: Aggregate predictions from many trees.

**Random forest**: An ensemble of randomized trees. Example: Reduce reliance on one tree.

**Boosting**: Sequentially adding models to improve a training objective. Example: Correct errors of earlier ensemble stages.

**kNN**: A method using nearby examples under a distance rule. Example: Estimate power from similar operating points.

**SVM**: A support-vector method often used for separating classes. Example: Learn a margin-based classification boundary.

**k-means**: A clustering method grouping points around chosen centres. Example: Group operating profiles without fault labels.

**PCA**: A projection onto directions of high variance. Example: Compress correlated sensor features.


## Module 10: Generalization and trustworthy evaluation

Learning outcomes:
- Separate training, validation and test roles.
- Recognize leakage, overfitting and appropriate split boundaries.

### Protect the evaluation boundary

Training data fit parameters. Validation data support choices such as model family, depth, features and thresholds. Final test data estimate performance after those choices are fixed. Repeatedly changing the model in response to test results turns the test into development data.

Cross-validation repeats training and validation over folds within development data. Fit learned preprocessing separately within each training fold. There is no universal split rule: forecasting needs temporal order; transfer to new machines may need holding out whole machines; independent experimental designs may justify a random split.

If overlapping vibration windows from the same event appear in train and test, performance may be optimistic. Define what “new” means for the deployment question. A row count alone does not show independence.

Pause and explain: Which split would test transfer to a machine never used in training?

### Underfitting, overfitting and regularization

Underfitting describes failure to represent the relevant relationship adequately. High errors relative to a useful baseline in low-noise data can suggest a weak model, features or training. High errors alone can also reflect irreducible noise or incorrect labels; investigate before diagnosing.

Overfitting occurs when the learned relationship captures training-specific variation and fails to generalize. A common symptom is lower training error than relevant validation error, though some gap is normal. Compare learning curves and baselines rather than using a single arbitrary rule.

Regularization discourages certain kinds of complex fitting through penalties or constraints. Early stopping chooses a training checkpoint using validation performance. It does not use the final-test score to select the epoch. Bias–variance language describes aspects of prediction error, not moral fairness bias.

Pause and explain: Why does high error on both sets not always prove underfitting?

### Leakage is information crossing the wrong boundary

Data leakage occurs when information unavailable for the intended prediction enters training or selection. Examples include target-derived inputs, future sensor readings, duplicate events across sets and preprocessing learned from all data before evaluation.

Consider scaling all data before a five-fold study. Each held-out fold influenced the scaler, so the procedure evaluated is not the intended one trained only on its fold. Use a pipeline. In a forecast, a centered moving average can include future observations; a chronological split alone does not repair that feature.

After development, test once and report what was actually done. If the test was reused, disclose the limitation and obtain genuinely new evidence where possible. Reproducibility records should include split IDs, transformations, seeds, code and versions.

Pause and explain: Why might a centered moving-average feature leak in a real-time alarm?

### Terms

**Generalization**: Performance on relevant unseen examples. Example: A model works on a held-out machine.

**Training set**: Examples used to fit model parameters. Example: Estimate regression coefficients.

**Validation set**: Examples used to make model-development choices. Example: Select tree depth or an alert threshold.

**Test set**: Examples reserved for evaluating a locked model. Example: Assess final performance without further tuning.

**Cross-validation**: Repeated training/validation splits within development data. Example: Five folds with preprocessing fitted inside each fold.

**Underfitting**: Insufficient representation or learning of the relevant relationship. Example: A straight line misses a strong nonlinear response.

**Overfitting**: Learning training-specific patterns that do not generalize. Example: A deep tree captures incidental noise.

**Regularization**: Constraints or penalties discouraging certain complex fits. Example: Penalize large fitted coefficients.

**Early stopping**: Selecting a training checkpoint using validation performance. Example: Stop before validation loss worsens.

**Data leakage**: Unavailable or evaluation information improperly influencing development. Example: Future readings used for an earlier forecast.


## Module 11: Neural networks and deep learning

Learning outcomes:
- Explain weights, biases, activations, layers and basic training terms.
- Distinguish gradients from parameter updates.

### A neuron is a small computation

A simple neuron computes z=Σwᵢxᵢ+b and then an activation a=f(z). Weights scale input contributions, bias shifts the weighted sum, and activation can introduce nonlinearity. ReLU returns max(0,z). A neuron is a mathematical operation, not a miniature human brain.

Worked example: x₁=2, x₂=1, w₁=0.5, w₂=−1, b=0.2 give z=0.2 and ReLU output 0.2. If z were −0.4, ReLU would return zero. In the activity, adjust inputs and weights to inspect this computation.

Layers contain units, and networks combine layers into mappings. Without nonlinear operations, stacked affine layers collapse to an affine mapping. Adding layers alone does not automatically create a useful nonlinear model.

Pause and explain: Compute ReLU for z=−3 and z=2.

### Loss, gradients and updates

Training defines a loss and calculates how it changes with parameters. A gradient collects derivatives of the loss with respect to those parameters. Backpropagation uses the chain rule to compute these derivatives efficiently through the network. An optimizer uses them to update parameters.

Gradient descent uses θ_new=θ_old−η∇L, where η is the learning rate. Backpropagation computes gradients; it is not itself the complete update policy. A large learning rate can overshoot, while a small one can make progress slow. These effects depend on the problem.

Worked example: parameter 2, gradient 0.5 and learning rate 0.1 give the new parameter 1.95. This example illustrates one update, not proof that a whole training run reaches a global optimum.

Pause and explain: Which operation computes gradients, and which operation uses them to change weights?

### Batches, epochs and realistic expectations

A batch is a group of training examples used for an update in a typical mini-batch procedure. An epoch is one pass through the training set. With 1,000 examples and batches of 50, a standard pass has 20 updates. If sizes are not divisible, the treatment of a final partial batch must be stated.

Deep networks can learn representations that are useful for complex data, but need appropriate data, compute and validation. More epochs can reduce training loss without improving unseen performance. Use validation to choose checkpoints and final test data to report the locked result.

The beginner goal is to understand the computation and vocabulary. No GPU is required for this course. Full architecture design, automatic differentiation software and large-model training belong in later study.

Pause and explain: Would 100 additional epochs guarantee improved test performance? Why?

### Terms

**Neuron**: A unit computing a weighted input plus bias followed by an activation. Example: a=ReLU(w₁x₁+w₂x₂+b).

**Weight**: A learned multiplier within a model. Example: w₁ scales the first feature.

**Bias term**: An additive parameter, distinct from fairness or statistical bias. Example: b shifts a neuron’s input.

**Activation**: A function transforming a neuron’s weighted sum. Example: ReLU clips negative values to zero.

**Layer**: A collection or stage of neural computations. Example: A hidden layer transforms inputs.

**Gradient**: Derivatives describing local change with respect to variables. Example: How loss changes with each weight.

**Backpropagation**: Chain-rule computation of gradients through a network. Example: Calculate derivatives before updates.

**Learning rate**: A setting controlling update scale. Example: η=0.1 in gradient descent.

**Batch**: A group of examples used for an update. Example: 50 examples in one update.

**Epoch**: One pass through the training set. Example: 1,000 examples processed once.


## Module 12: AI for images, signals and sequences

Learning outcomes:
- Match representations and architectures to data types.
- Explain temporal availability and windowing.

### Represent the information before choosing a network

Tabular data represent examples through explicit features. Images represent spatial values in pixels or channels. Signals have sample timing and units. A time series records values indexed by time. Converting these into numerical arrays is representation, not proof that the model understands their engineering meaning.

A multilayer perceptron, MLP, often operates on feature vectors. A convolutional neural network, CNN, uses shared filters over local patterns and is useful for images and some signals. A filter may respond to a local edge pattern, but such a response needs labelled evidence before being interpreted as a crack.

Images of the same component taken from several angles can leak across splits. Hold out relevant components or batches if the intended use is new-component inspection. Annotation quality, lighting and camera changes matter alongside architecture.

Pause and explain: Why might random image splitting overstate performance on new components?

### Sequence architectures are different mechanisms

Recurrent neural networks, RNNs, carry a hidden state through a sequence. LSTM is a recurrent architecture designed to manage information over steps. A transformer uses attention to combine information across positions and needs some way of representing order when order matters.

Attention weights contributions from representations; it is not human attention or proof of causal importance. A transformer is distinct from an RNN even though both can process sequences. The best method depends on data, constraints and evidence; a simple lagged-feature model can be a strong baseline.

Predicting tomorrow's load requires defining the issue time and horizon. Tomorrow's actual temperature is unavailable at issue time; a weather forecast could be available but has its own error. Do not claim measured-weather accuracy as operational forecast accuracy.

Pause and explain: Compare information passed through recurrence with information combined by attention.

### Windows and horizons

Signal features are often computed over windows. RMS summarizes magnitude; spectral features summarize frequency content. State sampling rate, window length and alignment. A 96-row shift means 24 hours only for complete regular 15-minute data. Once rows are removed, use timestamp alignment rather than assuming row positions represent time.

A forecast horizon is the time between issue and target. For a real-time detector, features cannot include future readings. Overlapping windows need careful splits: neighbouring windows can share most of their samples. Leave suitable gaps or hold out events when the task requires independence.

These details often matter more than model size. Draw a timeline of available observations and target times before fitting a sequence predictor. Describe how missing intervals and changed sampling rates are handled.

Pause and explain: Does shifting 96 rows after filtering to daylight still mean yesterday?

### Terms

**Computer vision**: Methods for analysing image or video information. Example: Inspect surface defects.

**Time series**: Observations indexed by time. Example: A temperature history with timestamps.

**MLP**: A multilayer perceptron using fully connected neural layers. Example: Predict from a feature vector.

**CNN**: A network using shared convolutional filters. Example: Detect patterns in inspection images.

**RNN**: A recurrent network carrying state through sequential steps. Example: Process a sequence of sensor values.

**LSTM**: A recurrent architecture with mechanisms for retaining and updating information. Example: Model temporal relationships.

**Transformer**: An architecture using attention over representations. Example: Process sequences with suitable order information.

**Attention**: A mechanism weighting and combining representations. Example: Combine relevant positions, without proving causation.

**Forecast horizon**: Time between forecast issue and target time. Example: A day-ahead prediction.

**Signal window**: A specified interval used to compute features. Example: One-second vibration RMS.


## Module 13: Generative AI and language models

Learning outcomes:
- Explain tokens, context, embeddings and foundation models.
- Separate pretraining, adaptation and prompting.

### What a language model produces

A language model learns patterns over token sequences and can generate or transform text. An LLM is a large language model, typically with many parameters and broad training. Producing a plausible continuation is not equivalent to verifying facts, executing code or consulting an engineering standard.

A foundation model is pretrained on broad data and can support multiple downstream tasks through adaptation or prompting. A multimodal model processes or generates more than one information type, such as text and images. These names describe capabilities and development approaches, not guarantees of correctness.

Generative systems also include diffusion models and generative adversarial networks, GANs. Recognize those names; detailed derivations are outside this course. An generated concept drawing can suggest an idea while failing dimensional, manufacturing or safety requirements.

Pause and explain: Does generating code mean that the code was executed successfully?

### Tokens, context and embeddings

A token is a unit processed by a model: it may be a word fragment, punctuation or another encoded item. Tokenization depends on the model. This course does not imitate a particular provider's tokenizer or claim exact token counts from word counts.

The context window limits information available in an interaction. Long context does not guarantee accurate use of every detail. An embedding represents an item as a numerical vector. Similarity can help retrieve related passages, but vector proximity is not proof that a passage supports a claim.

Attention combines representations according to learned computations. “Cell” might mean a PV cell, battery cell or spreadsheet cell; context helps disambiguation. Always supply the intended system and units rather than expecting the model to infer missing assumptions correctly.

Pause and explain: Why is counting words not a reliable exact token count?

### What changes weights and what does not

Pretraining learns broadly useful patterns from a corpus. Fine-tuning updates model parameters on additional examples for a task, domain or behaviour. Transfer learning reuses knowledge from earlier training; fine-tuning is one form, while using a frozen feature extractor is another.

Prompting supplies instructions, context and examples during inference. Zero-shot uses no demonstration examples; few-shot includes some. Adding example lab reports to a prompt does not by itself update the model's weights. Service providers may have separate retention or training policies, so do not infer privacy from this computational distinction.

Retrieving a manual and putting it in context is also not inherently retraining. Keep these mechanisms separate when deciding how to improve an engineering assistant. First ensure the source and revision are correct, then test the resulting answer.

Pause and explain: Which changes weights: fine-tuning, adding examples to a prompt, or retrieving a manual?

### Terms

**Foundation model**: A model pretrained on broad data for reuse across downstream tasks. Example: Adapt a broadly trained model to an engineering task.

**LLM**: A large language model processing and generating token sequences. Example: Draft an explanation that still needs verification.

**Token**: A model-specific unit such as a word fragment or punctuation. Example: One word may produce several tokens.

**Context window**: The finite content available within a model interaction. Example: The model cannot reliably use an omitted datasheet.

**Embedding**: A numerical vector representing an item. Example: Retrieve related manual passages by similarity.

**Multimodal model**: A model handling multiple information types. Example: Discuss an image together with text.

**Pretraining**: Initial learning on broad data before downstream use. Example: Learn reusable language patterns.

**Fine-tuning**: Updating model parameters using additional training examples. Example: Adapt behaviour for a labelled task.

**Transfer learning**: Reusing knowledge from earlier training for another task. Example: Use a frozen image feature extractor.

**Prompting**: Supplying instructions and context at inference time. Example: Request an explanation with units.

**Diffusion model**: A generative model learning a reverse process from noised examples. Example: Generate an illustrative image.

**GAN**: A generative approach involving generator and discriminator training. Example: Recognize the model-family name.


## Module 14: Using AI assistants effectively

Learning outcomes:
- Build a prompt with task, evidence, assumptions and checks.
- Explain retrieval, tools, APIs and agent boundaries.

### Write an engineering prompt

State the task, audience, system, given values and units, assumptions and requested output. Ask the model to distinguish supplied facts from assumptions and to identify missing information. A useful prompt makes checking easier; it does not make the answer true.

Example: “For a rooftop PV array with area 20 m², irradiance 800 W/m² and efficiency 0.20, estimate DC power ignoring temperature. Show units. Explain what else is needed for daily energy.” The independent check is ηAG=3,200 W. At inverter efficiency 0.96, the simplified AC estimate is 3,072 W.

A single instantaneous irradiance cannot establish daily energy. Energy requires time information and the relevant losses. Ask for a draft, verify equations and values independently, test code on a known case, revise and disclose allowed AI assistance.

Pause and explain: What is missing if an assistant turns one instantaneous power value into daily energy?

### Retrieval supplies evidence at inference time

Retrieval-augmented generation, RAG, searches a collection for relevant material, adds retrieved passages to model context, and generates an answer using that context. Retrieval may use keywords, embeddings or both. RAG does not inherently update model parameters.

For maintenance, approved manuals can supply operating limits. Verify that a cited passage exists, matches the correct machine and revision, and supports the claim. A retrieved paragraph about a different inverter is not good evidence even if its terms look similar.

Grounding connects output to supplied evidence. It can improve checking, but does not eliminate misreading, irrelevant retrieval or hallucination. Never treat a citation label as proof without opening the actual source.

Pause and explain: What three checks should you make on a retrieved operating limit?

### Tools act; agents coordinate

An assistant is an interface supporting a user's tasks. A tool performs an operation, such as executing Python or searching documents. An API defines a software interface for requesting an operation. An agent system can select actions and use tools across steps toward a goal with a defined degree of autonomy.

Writing code is different from executing it, and execution without errors is different from correct engineering results. An assistant can propose an action while a tool carries it out. State action permissions, limits, logs and human approval responsibility for real systems.

This course has no connected AI service and sends no chat or data. The prompt builder produces text for you to review and optionally use elsewhere. Lab 4 verifies a supplied illustrative draft locally; it does not call an LLM.

Pause and explain: List checks between an assistant drafting code and a tool applying it to a real system.

### Terms

**Zero-shot prompting**: Giving a task without demonstration examples. Example: Ask for an explanation directly.

**Few-shot prompting**: Including demonstration examples in the context. Example: Supply two examples of the desired output format.

**Grounding**: Connecting output to relevant supplied evidence. Example: Use and check an actual datasheet passage.

**Retrieval**: Searching for material relevant to a query. Example: Find a maintenance manual section.

**RAG**: Retrieval followed by adding evidence to context for generation. Example: Answer using approved manuals.

**Tool**: A function or system carrying out an operation. Example: Run Python or search a local file.

**API**: A defined interface for software to request operations. Example: Submit data through a documented function interface.

**Assistant**: An interface helping users complete tasks. Example: A conversational engineering helper.

**Agent**: A system selecting and coordinating actions across steps toward a goal. Example: A bounded workflow with permissions and logs.


## Module 15: Reliability and responsible practice

Learning outcomes:
- Explain uncertainty, shift, verification and validation.
- Identify evidence, privacy and accountability requirements.

### Uncertainty and changing conditions

## What you are expected to learn

Distinguish aleatoric uncertainty from epistemic uncertainty, explain why a model's confidence may be unreliable outside its evaluated conditions, and recognize the difference between a distribution shift and gradual drift. Use these distinctions to decide when to monitor, defer a prediction or gather new evidence.

## Two sources of uncertainty

Aleatoric uncertainty is variation in observations or unresolved processes, such as sensor measurement noise. Repeating measurements may characterize this variation, but it cannot remove the underlying variability. Epistemic uncertainty comes from limited knowledge: sparse measurements in an operating regime, incomplete training examples or assumptions that may not represent the equipment. More informative observations can reduce some epistemic uncertainty. They cannot repair an inadequate model structure; a confidently estimated answer from a flawed model may still be wrong.

## Operating coverage is more than input bounds

Interpolation estimates within conditions represented by relevant observations. Extrapolation estimates beyond the covered operating domain, where behavior is less well supported. A point can fall between the minimum and maximum of each input and still be unrepresentative: combinations of inputs, plant configurations or operating regimes may be missing. Define the domain using the conditions relevant to the intended use, not just convenient rectangular limits, and evaluate performance on evidence from that domain.

## Calibration and confidence

Calibration checks whether stated probabilities agree with observed frequencies under defined conditions. For example, among a sufficiently large set of comparable cases assigned about 80% probability, a calibrated model should be correct about 80% of the time. This is a group-level property, not a promise about an individual prediction and not an explanation of why the model made it. Assess calibration on independent data representative of the intended operating conditions. High model confidence is not proof of calibration, accuracy or permission to extrapolate.

## Distribution shift and drift

Distribution shift occurs when the deployment population differs from the development population, such as transferring a model from one plant type to another. Drift describes gradual change in data or relationships over time, for example sensor ageing, wear or a changing control regime. A random seed only controls aspects of randomized computation; it cannot correct either kind of mismatch.

Monitor input ranges, missingness, output and alert patterns, and compare them with development conditions. Input changes are warning signals, not proof by themselves that accuracy has degraded; check outcomes when trustworthy labels become available. Define action rules in advance: investigate, obtain new validation evidence, recalibrate where justified, retrain only with appropriate data, or defer predictions when conditions fall outside the validated domain.

## Check your understanding

Can high model confidence justify using a model outside its validated operating domain?

ANSWER: No. Confidence is not proof of calibration or accuracy, and calibration is only checked for the conditions evaluated. Outside the validated domain, defer the prediction or gather new validation evidence.

A pump model developed at one plant is moved to a different type of plant. Is this drift or distribution shift?

ANSWER: Distribution shift: the deployment population differs from the development population. Drift is gradual change over time, such as sensor ageing or wear.

## Key takeaways

- Aleatoric uncertainty is variation in the observations; epistemic uncertainty comes from limited knowledge.
- Define the operating domain by the conditions that matter, not only by the minimum and maximum of each input.
- Calibration is a group-level property. High confidence is not proof of accuracy or permission to extrapolate.
- Distribution shift is a change of population; drift is gradual change over time.
- Set monitoring, deferral and revalidation rules before deployment.

Pause and explain: Can a high model confidence justify using it outside the validated operating domain?

### Verification and validation are different checks

## What you are expected to learn

Separate implementation verification from real-system validation, select evidence appropriate to each, and keep enough provenance for another engineer to reproduce and audit the procedure.

## Verification: did we implement the method correctly?

Verification checks whether the intended equations, code or algorithm were implemented correctly. Use known cases, dimensional analysis, bounds, limiting cases and sign conventions, and confirm that the workflow can be repeated. For a pump power model, the product of pressure drop and volumetric flow, delta-p x Q, has units Pa x m^3/s = W. A unit check and a test against a known calculation can catch implementation errors; they do not establish that the model represents a real pump.

## Validation: does it represent the real system?

Validation asks whether the model is adequate for its intended purpose on the physical system. Compare predictions with appropriate independent, calibrated measurements across relevant operating conditions. A synthetic dataset or simulator can test whether code runs and the evaluation workflow behaves as expected, but agreement with synthetic data alone provides no physical validation of real hardware. Keep evidence used for final validation independent of fitting and model selection, and preserve the final test boundary until development decisions are complete.

## Provenance and reproducibility

Record how and when data were acquired, sensor and calibration context, units, transformations, split identifiers, code and environment versions, model settings, and material manual decisions. This lets another person regenerate the stated procedure and understand which evidence supports each result. Reproducibility is not correctness: the same bug can produce the same wrong answer repeatedly. A random seed can make randomized steps more repeatable under stated conditions, but does not guarantee identical results across environments or validate a model.

## Re-check after changes

A new sensor, recalibration, operating regime or plant can change the evidence or the system being represented. Review calibration, set explicit deferral rules for unsupported conditions, and establish criteria for collecting new validation data or retraining. Maintain named reviewers and auditable records; neither a successful synthetic test nor a reproducible run substitutes for physical evidence.

## Check your understanding

Is matching a synthetic simulator enough to validate predictions for real equipment?

ANSWER: No. It can verify that the code and evaluation workflow behave as intended. Validation needs independent, calibrated measurements from the real system across the relevant operating conditions.

A unit check confirms that Δp × Q gives watts. Is that verification or validation?

ANSWER: Verification. It checks the implementation, not whether the model represents a real pump.

## Key takeaways

- Verification checks that the method was implemented correctly; validation checks that it represents the real system.
- Agreement with synthetic data or a simulator does not validate real equipment.
- Keep final validation evidence independent of fitting and model selection.
- Record provenance so another engineer can reproduce and audit the work. Reproducible does not mean correct.
- Re-check after a new sensor, recalibration, operating regime or plant.

Pause and explain: Is matching a synthetic simulator enough to validate predictions for real equipment?

### Responsible use and human oversight

## What you are expected to learn

Recognize unsupported AI-generated claims, protect restricted information, document permitted assistance, and define specific human responsibility and authority to intervene before AI-assisted work affects an engineering decision.

## Check output integrity

Hallucination or confabulation is plausible but false or unsupported output. In engineering, it may appear as an invented standard citation, incorrect material property or flawed equation. Trace claims to original, authoritative sources and independently check equations with known numerical cases, units and assumptions. A fluent response or citation label is not evidence. Pass outputs through a verification gate before using them in a report, calculation or system action.

Use precise language for different kinds of bias. Data-coverage bias means relevant machines, people or operating conditions are missing or underrepresented in the examples. Social fairness concerns unequal performance or impact across people or groups when relevant to the application. The bias term in a neural network is an additive model parameter. These are distinct meanings and need different analyses; do not treat one as evidence about another.

## Protect information and systems

Do not share restricted personal, assessment or proprietary data without permission and appropriate safeguards. Follow institutional disclosure and information-handling policies. Generated code and connected tools can introduce security risks; review their behavior, permissions, inputs and outputs before integrating them with engineering systems. Use source control and logging so changes and actions can be examined.

## Make human oversight operational

“Human in the loop” is not a control unless responsibility is specific. Name the reviewer and decision owner, state which outputs require review, define what evidence must be checked, and give an authorized person explicit ability to pause or stop an action. Keep an audit trail of data provenance, assumptions, units, baseline comparisons and decisions. For an unsupported claim, restricted information or sensor shift, specify the corrective action rather than relying on a general warning.

## Account for resources and disclosure

AI computation consumes physical resources. Choose methods scaled to the engineering task and balance analytical needs against available compute and resource constraints; avoid unsupported numerical claims about a tool's footprint. Disclose AI assistance as required by institutional policy and retain a verifiable reasoning trail so a reviewer can distinguish supplied evidence, generated suggestions and the engineer's final decisions.

## Check your understanding

What evidence and disclosure would you attach to an AI-assisted lab submission?

ANSWER: State which AI assistance you used, as policy requires. Trace claims to authoritative sources, show known-case, unit and assumption checks, and keep a reasoning trail that separates supplied evidence, generated suggestions and your own decisions.

Why is "a human in the loop" not enough on its own?

ANSWER: Oversight works only when responsibility is specific: a named reviewer, defined checks and the authority to pause or stop an action.

## Key takeaways

- Trace AI-generated claims to authoritative sources, and check equations with known cases and units.
- Data-coverage bias, social fairness and the neural-network bias term are different ideas.
- Do not share restricted personal, assessment or proprietary data without permission and safeguards.
- Human oversight needs a named reviewer, defined checks and the authority to stop an action.
- Disclose AI assistance as policy requires and keep a verifiable reasoning trail.

Pause and explain: What evidence and disclosure would you attach to an AI-assisted lab submission?

### Terms

**Aleatoric uncertainty**: Variation inherent in observations or unresolved processes. Example: Measurement noise in a temperature reading.

**Epistemic uncertainty**: Uncertainty due to limited knowledge, data or assumptions. Example: Sparse measurements in a load regime.

**Calibration**: Agreement of stated probabilities or intervals with observed frequencies under defined conditions. Example: Check fault probability groups on independent data.

**Interpolation**: Estimating within covered input conditions. Example: Predict within a sampled operating region.

**Extrapolation**: Estimating beyond covered input conditions. Example: Use a model at a higher temperature than observed.

**Distribution shift**: A difference between development and deployment data distributions. Example: Transfer from one plant type to another.

**Drift**: Change in data or relationships over time. Example: Sensor wear alters readings.

**Hallucination**: Plausible but false or unsupported generated output. Example: An invented standard citation.

**Verification**: Checking correct implementation of the intended method. Example: Test units and a known calculation.

**Validation**: Checking suitability against real-system evidence for the intended use. Example: Compare with calibrated experiments.

**Provenance**: Records of where data and results came from. Example: Keep source, units, transformations and versions.

**Human oversight**: Defined human responsibility and ability to review, intervene or stop. Example: An engineer approves an operating action.


## Module 16: Engineering applications and your mini-project

Learning outcomes:
- Distinguish surrogate models, feasibility constraints, digital twins and physics-informed methods, and identify the evidence each engineering application needs.
- Frame a bounded project with traceable data, a relevant baseline, leakage-resistant evaluation, physical checks and stated limitations.
- Separate browser knowledge scores from practical evidence and prepare a reproducible, reviewable mini-project submission.

### Applications with different evidence needs

## What you are expected to learn

Explain why engineering applications require different evidence; describe how a surrogate supports design search; distinguish an objective from constraints and feasibility; and identify the defining data connection in a digital twin.

## Application determines the evidence

AI can support design, manufacturing, thermofluids, maintenance and robotics. The model and evidence should follow the decision: screening candidate designs, estimating a thermal response, identifying a possible fault and coordinating a robot are not interchangeable tasks. The Module 16 examples use a motor-driven centrifugal pump with piped connections and instrumentation to make those physical conditions concrete.

State what decision the model informs, which inputs are available at that decision, and the operating conditions for which its output is intended. A strong score on one dataset does not by itself show that the system is suitable for another machine, load range or operating regime.

## Surrogates accelerate search, not sign-off

A high-fidelity simulation can be expensive to run for every design. A surrogate learns an approximation from evaluated designs or operating cases and can screen additional candidates at lower cost. For example, it can help compare pump or geometry candidates without rerunning an expensive flow simulation for every option. Its accuracy is supported only where the underlying evidence represents the inputs and conditions being considered.

Re-evaluate promising candidates with the original simulation or experiment. Verification checks that the intended model or calculation was implemented correctly; physical validation checks its adequacy against appropriate evidence from the real system. A surrogate helps explore the design space but does not replace either check or authorize a hardware claim.

An uncertainty-aware search method such as Bayesian optimization can use a surrogate to prioritize which candidate to evaluate next. It can make expensive searches more efficient, but it does not verify the implementation, prove constraint satisfaction or establish physical validity.

## Objectives and constraints answer different questions

An objective states the performance goal, such as reducing a pump's electrical power demand. Constraints and bounds define which designs or outcomes are permitted—for example, a minimum required flow or a maximum allowable stress. The feasible design space contains only candidates that satisfy all stated constraints.

A candidate can have an attractive predicted objective and still be infeasible: a design that predicts low power but violates a stress or flow limit is not acceptable. Check constraint values and their units separately from the objective; do not treat a good score as evidence that a design meets its bounds.

## Connected twins and physics-informed learning

An isolated CAD model has no active data connection to the physical equipment. A digital twin maintains a data linkage with its physical counterpart—for example, a digital representation that receives ongoing pressure, flow or temperature measurements for monitoring and state estimation. The connection, not visual similarity, is the key distinction.

An active sensor connection also creates data-integrity and cybersecurity responsibilities. Check that the measurements and data path are trustworthy, and investigate disagreement between the model and independent physical readings before acting on a prediction.

Physics-informed learning incorporates physical equations or constraints into a learning approach, for example by adding a penalty when a predicted state violates a governing equation or conservation relationship. A physics-informed neural network (PINN) is one particular architectural family; it is not a synonym for every hybrid or physics-informed model. Examples of physical structure include a force relationship such as F = ma or thermodynamic constraints.

## Check your understanding

A surrogate predicts a promising pump design. What must happen before the design is accepted?

ANSWER: Re-evaluate it with the original simulation or experiment, check every constraint and its units separately from the objective, and validate it against evidence from the real system.

What makes a digital twin different from an isolated CAD model?

ANSWER: An active data connection to the physical equipment, such as ongoing pressure, flow or temperature measurements. Visual similarity is not the distinction.

## Key takeaways

- Choose the model and the evidence to match the engineering decision.
- A surrogate speeds up design search; re-evaluate promising candidates with the original simulation or experiment.
- The objective states the goal; constraints decide which designs are feasible.
- A digital twin has an active data connection to the physical equipment; an isolated CAD model does not.
- Physics-informed learning builds physical equations into learning; a PINN is one particular type.

Pause and explain: A surrogate predicts a promising design. Which checks establish feasibility, and what makes a digital twin different from an isolated CAD model?

### A small project you can defend

## What you are expected to learn

Frame a bounded engineering task; document its inputs, target, data provenance and operating domain; keep training separate from locked evaluation data; and report baselines, quantitative errors and physical checks in a reproducible way.

## Bound the decision and document the data

Choose one manageable task: predict pump power, classify supplied bearing scores, group operating profiles or critique an AI-assisted calculation. For the pump example, predict measured electrical input power in kW from available flow and pressure-rise inputs. Hydraulic power is pressure rise multiplied by volumetric flow; estimating electrical input power also requires accounting for efficiency and losses. State the decision and intended user, target, inputs available at decision time, and what evidence would make the result useful.

Define the operating domain using relevant physical bounds, operating parameters and load ranges. Record the data source, units, relevant measurement context and assumptions. Use approved measurements when available; if you use synthetic data, label it clearly and restrict claims to what the synthetic example demonstrates. Synthetic data can exercise a workflow but cannot validate a real machine.

## Separate training from evaluation

Choose a split that reflects intended use. When examples share a machine, event, design or time sequence, keep related records together or hold out an appropriate group or later period; random row splitting can make evaluation too optimistic.

Fit preprocessing using training data only. Use validation data to make development choices, then lock the final test set and use it only for the final evaluation. This keeps information from the evaluation examples out of preprocessing and model selection.

## Compare baselines and report quantitative errors

Compare the model with a training-mean predictor and, when appropriate, a known physical calculation on the same evaluation cases. For pump power, the training-mean predictor is a simple reference; an appropriate physical calculation supplies a second comparison. A baseline helps show whether the model adds value beyond a simple or established approach.

On the locked test set, report task-appropriate measures with units. For regression, show MAE and RMSE in the target's unit and residuals in consistent SI units; residuals show signed prediction errors and can reveal systematic under- or over-prediction, such as errors that grow at high pressure. For classification, report the relevant class counts and measures such as precision and recall. Interpret the results in engineering terms rather than presenting a score alone.

Add an independent physical check or known case, and state domain limits and assumptions. Model metrics summarize performance on selected examples; they do not establish physical validity outside the evaluated conditions.

Retain evidence for each stage: the decision, inputs and provenance for problem framing; the split, baseline and fitted preprocessing for development; locked-test errors and limitations for evaluation; and known-case or independent physical checks for verification. This record lets a reviewer distinguish a repeatable method from an unsupported conclusion.

## Keep the project reproducible and your own

The four starter notebooks cover data inspection, pump-power modelling, fault detection and verification of an AI-assisted engineering draft. Begin with the relevant starter, inspect its assumptions, and explain any changes in your own words. A complete reference is an example of a route, not a substitute for your own work.

Keep the notebook runnable from a clean kernel and record the data, environment, split, baseline, modelling choices, checks, limitations and failure modes. Follow institutional policy for AI assistance, disclose permitted use and checks, and do not submit private or restricted information to an external service without authorization.

## Check your understanding

Write one project sentence containing a decision, inputs, an output and evidence.

ANSWER: For example: to help decide whether a pump is operating efficiently, predict measured electrical input power in kW from the flow and pressure rise available at decision time, and compare locked-test MAE and RMSE with a training-mean baseline and a physical calculation.

Why can a random row split make results look too optimistic?

ANSWER: Related records from the same machine, event or time sequence can end up in both the training and test sets, so the test no longer reflects new conditions.

## Key takeaways

- Bound the project to one decision, with documented inputs, target, data provenance and operating domain.
- Label synthetic data clearly; it can exercise a workflow but cannot validate a real machine.
- Fit preprocessing on training data only and keep the final test set locked.
- Compare with a training-mean baseline and, where appropriate, a physical calculation.
- Report errors with units, add a physical check, and keep the notebook reproducible and your own.

Pause and explain: Write one project sentence containing decision, inputs, output and evidence.

### Submit evidence, not only a browser score

## What you are expected to learn

Distinguish the browser knowledge grade from practical assessment; explain the mini-project rubric; and prepare work that another person can rerun, review and assess within stated operating limits.

## A browser score measures knowledge checks

The browser grade combines the mean of the best module quiz scores (70%) with the final blueprint assessment (30%). The optional browser completion record requires at least 70% on every module quiz and on the final. Lessons and flashcard ratings do not contribute to that grade.

The score is a knowledge check, not a practical evaluation. The file exposes answer keys and progress can be edited, so a browser score cannot authenticate a learner, establish model validity or authorize deployment.

## The practical rubric evaluates engineering evidence

The infographic groups the mini-project rubric into data and preprocessing (45%), evaluation and physics (45%), and reproducibility and AI disclosure (10%). The course's detailed rubric breaks those groups down: problem/data (20%) plus baseline/split/preprocessing (25%); evaluation/interpretation (25%) plus physical verification/limitations (20%); and reproducibility/AI-use disclosure (10%). These are the same three groups, shown at different levels of detail.

The rubric asks whether the problem and data are well defined, the baseline and split are justified, preprocessing is isolated from evaluation data, results are interpreted with physical checks, and the work can be reproduced with appropriate AI-use disclosure. The course cannot inspect or certify a notebook automatically; an instructor or peer reviewer can inspect the evidence and ask you to reproduce a result.

## Make the submission reproducible and bounded

Restart the kernel and run every cell from top to bottom. Resolve unrecorded variable dependencies, inspect outputs, and make the notebook runnable by a reviewer. State the model-selection rationale, failure modes or thresholds, and the physical operating domain—including the valid machine bounds, operating parameters and load ranges.

Submit runnable notebooks, domain limitations, independent physics checks and AI disclosures. Preserve enough information about the data, environment and decisions for a reviewer to reproduce the result, then explain one modelling choice and one failure mode. A browser completion record must not be described as evidence that a model is safe or ready to deploy.

## Check your understanding

What can a clean, reproducible project show that a browser score cannot?

ANSWER: That the work runs from top to bottom, uses a justified split and baseline, reports errors with units and physical checks, and states its limits, all of which a reviewer can rerun. A browser score only checks knowledge.

Which operating limits must a reviewer see?

ANSWER: The physical operating domain: the valid machine bounds, operating parameters and load ranges for which the results are claimed.

## Key takeaways

- The browser grade combines 70% mean best module quiz score and 30% final assessment; it checks knowledge only.
- A browser score cannot authenticate a learner, validate a model or authorize deployment.
- The practical rubric weights data and preprocessing 45%, evaluation and physics 45%, and reproducibility and AI disclosure 10%.
- Restart the kernel and run the notebook from top to bottom before submitting.
- Submit runnable notebooks, operating limits, independent physics checks and AI disclosures.

Pause and explain: What can a clean, reproducible project demonstrate that a browser score cannot, and which operating limits must a reviewer see?

### Terms

**Surrogate model**: A fast approximation to an expensive experiment or simulator. Example: Predict pressure drop during geometry search.

**Objective**: A quantity to improve in an optimization problem. Example: Minimize energy consumption.

**Constraint**: A requirement limiting permitted choices or outcomes. Example: Keep stress below a stated limit.

**Feasibility**: Satisfaction of the stated bounds and constraints. Example: Verified stress meets the limit.

**Digital twin**: A digital representation connected through data to a physical counterpart. Example: A monitored system representation, not an isolated CAD file.

**Physics-informed learning**: Learning using physical structure, equations or constraints. Example: Penalize a conservation residual.

**Reproducibility**: Ability to regenerate the stated procedure with its documented inputs and environment. Example: Run a notebook from a clean kernel.

**Operating domain**: The conditions for which suitability has been evaluated. Example: A specified machine and load range.


# AI 101 mini-project submission checklist

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
