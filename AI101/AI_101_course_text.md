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

Artificial intelligence is a broad field concerned with systems that carry out tasks associated with intelligent behaviour. These systems can work in different ways. Some follow rules written in advance. Others search for solutions, use stored knowledge or learn patterns from examples [1]. Calling a system AI therefore does not tell you whether it learns from data.

A fixed rule tells a system what to do. A learning method uses examples to learn part of its behaviour. In the infographic, the outer rectangle represents the whole field of AI. It includes several approaches, not just one algorithm.

## 2. Machine learning and deep learning

Machine learning is one approach within AI. An ML model uses examples to learn patterns or to adjust its parameters, which are the values that determine how it turns inputs into an output [2]. For example, a pump-power predictor learns from measurements taken during pump operation. A bearing-fault classifier learns to distinguish the conditions represented in its training examples.

Deep learning is a type of ML that uses neural networks with multiple layers [3], [4]. The nested rectangles in the infographic show this relationship: AI includes ML, and ML includes deep learning. Some AI systems do not use neural networks, and some ML models do not use deep learning.

The term deep learning tells you how a model is built. It does not tell you what the output means or whether the result suits the engineering decision you want to make.

## 3. Classification and generation

Classification means predicting which category an input belongs to. For example, a surface-defect model might label an image as cracked or intact. A neural network with multiple layers can make this prediction without generating explanatory text, code or images.

Generative AI produces content [4]. For example, a system that drafts a maintenance explanation is carrying out a generative task. A language model can use deep learning to generate text.

Deep learning and generation describe different aspects of a system. Deep learning describes the model approach. Generation describes the kind of output. For this reason, generative AI should not be drawn as a required fourth level inside the AI, ML and deep-learning rectangles.

When you describe a system, ask two questions. Which approach does it use? What output does it produce? A deep-learning classifier and a deep-learning text generator use the same broad approach but produce different kinds of output.

## 4. Data science includes the measurement workflow

Data science includes collecting measurements, cleaning data, analysing results, building models and communicating findings [5]. It overlaps with AI and ML, but building a model is only one part of the work.

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

Automation means carrying out a process with less manual intervention [6]. A controller can do this by following fixed rules without learning from data. In the course example, a thermostat switches off above 30 °C. This is automation: the thermostat follows a temperature rule. It does not show learning from examples.

The 30 °C threshold is a teaching example, not a recommended setting for equipment. The key question is how the controller decides what to do. Was the rule specified in advance, or was the behaviour learned from data?

## 2. Robotics describes physical sensing and action

A robot is a physical machine that senses, decides and acts. Its decisions may come from conventional control rules, from AI or from a combination of the two. Calling a machine a robot does not tell you whether it learns.

For example, the slides show a conventional PID feedback controller connected to a robot and a sensor. The controller compares the measured output with a target value, called the setpoint, and applies specified feedback rules [7]. This arrangement can work without learning from data. If a component does learn, identify that component and explain what it does.

Automation and robotics can overlap: a robot can carry out an automated process. Both can work without ML, and both can include ML. To decide whether learning is involved, examine how the system works.

## 3. Narrow AI and general intelligence

Narrow AI is designed for particular tasks. Familiar examples include filtering spam, estimating travel times and suggesting text completions. In engineering, a classifier that identifies a defined set of defects is narrow AI. Testing it gives evidence about those tasks under the conditions tested. Doing one task well does not show that a system can perform unrelated tasks or understands more broadly.

AGI refers to proposed AI capabilities that would apply broadly across tasks. People disagree about how to define and test it, so the label alone does not show that a system can do every task [8]. This course does not claim that a current assistant has human understanding or can reliably handle every engineering problem.

For example, an assistant may produce fluent text. That fluency does not provide the evidence or authority needed to approve a pressure-vessel design. Always check the task, the supporting evidence and the actions the system is allowed to take.

## 4. Five questions for evaluating a system

Use the sequence in the slides to describe a system:

- Inputs: What information does the system receive?
- Learned components: Which parts, if any, learn from data?
- Outputs: What does each component produce?
- Permitted actions: What is the system allowed to do with that output?
- Failure consequences: What happens if the output or action is wrong?

These questions bring out details that a product label may leave out [9]. They also separate a recommendation from an action the system has permission to carry out. A maintenance explanation, a classification result and a physical control command each need checks suited to their purpose.

## Worked example: a bearing alert

Consider a hypothetical bearing-alert system that uses vibration measurements. Its inputs are measurements available before the maintenance decision. A trained classifier uses them to estimate a defined condition, such as healthy or needs inspection. The alert is a reason to investigate, not a confirmed diagnosis.

A responsible procedure sends the alert to a qualified person for review. It does not assume that every alert requires an automatic shutdown. Before using the system, check how often it misses faults and how often it raises false alarms [10]. Use representative examples whose conditions have been checked independently.

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

Consider a pump whose vibration and bearing temperature are increasing. Start with a question: should an inspection be requested? This gives the project a clear purpose before you choose an algorithm [11].

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

The example does not explain how the score was calculated. A score is a calibrated probability only if, among many cases scoring 0.8, about 80% really are faults [12]. Nothing here shows that, so do not read 0.8 as an 80% chance of failure just because it lies between zero and one.

Before acting on a score, check measurement quality, operating limits and whether the model has been validated, meaning tested on examples that were not used to build it. A practical description also names who will use the result, the conditions in which the system is intended to work, called the operating domain, and the escalation path, which is the route for passing a concern to the responsible decision-maker [9]. This lesson gives no procedure for particular equipment.

## 5. Different components require different checks

The slides distinguish three components:

- A fixed trip follows an automation rule when its specified condition occurs.
- A learned detector uses patterns learned from examples to predict a fault-related score. Check its performance on examples that were not used to fit the model.
- A maintenance assistant generates text. Check that text against the relevant records.

Each check answers a different question. An accurate maintenance explanation does not show that the detector performs well, and a good detector does not make a generated explanation correct.

## 6. Synthetic examples and physical validation

Synthetic examples are constructed for teaching. They help you practise analytical methods and think about what evidence is needed and what could happen if a result is wrong.

They do not show that a real machine is safe or that a maintenance recommendation is valid [13]. When you discuss a result, say what the example demonstrates and what still needs to be checked on physical equipment.

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

## What you are expected to learn

This lesson compares physics-based, data-driven and hybrid models. You will use the pump example to distinguish hydraulic power, input power and a residual correction.

## Physics-based, data-driven and hybrid models

A physics-based model uses governing relationships, stated parameters and appropriate conditions [14]. For a pump, hydraulic power is calculated from pressure rise and volumetric flow rate [15]. The model must still be checked against its assumptions and physical measurements.

A data-driven model estimates an input-output relationship from observations [16]. For example, it can estimate electrical power from flow rate, pressure rise and shaft speed without explicitly imposing a hydraulic-power equation.

A hybrid model retains a physical baseline and adds a learned correction [14], [17]. It is useful when the physical calculation is informative but does not represent every observed effect.

## Pump-power example

The hydraulic-power relationship is:

P_h = Δp × Q

- P_h: hydraulic power, in watts (W).
- Δp: pressure rise, in pascals (Pa).
- Q: volumetric flow rate, in cubic metres per second (m³/s).

For Δp = 100 kPa = 100,000 Pa and Q = 0.02 m³/s:

P_h = 100,000 Pa × 0.02 m³/s = 2,000 W

The stated input-power relationship is:

P_in = P_h / η

Here, η is efficiency and is dimensionless. With η = 0.8, P_in = 2,500 W. The stated input-power meaning and the corresponding efficiency must be matched; hydraulic, shaft and electrical power are different quantities.

## Residual correction

A residual compares a measured value with a prediction:

r = y − ŷ

For measured input power y = 2,800 W and predicted input power ŷ = 2,500 W, r = +300 W. A positive residual means that the baseline prediction is below the measurement. It identifies a discrepancy; it does not, by itself, prove its physical cause.

## Choose an approach within its evidence limits

Use a physics-based model when its governing relationships, parameters and assumptions are suitable for the question. Consider a data-driven model when representative observations cover the intended use and the relevant relationship is difficult to specify directly. A hybrid can retain a useful physical baseline and learn a correction when repeatable residual patterns and adequate data support one. None of these choices guarantees reliable extrapolation: outside the evidence and assumptions used for validation, check the model rather than trusting a confident numerical output.

## Check your understanding

Why are 2,000 W and 2,500 W different in this example?

ANSWER: 2,000 W is hydraulic power. 2,500 W is input power calculated using the stated dimensionless efficiency of 0.8.

## Key takeaways

- Physics models use physical relationships; data-driven models learn from observations; hybrid models use both.
- State the power quantity and use consistent SI units.
- A residual can support a learned correction, but it does not establish a cause.

Pause and explain: Calculate hydraulic power for Δp=100,000 Pa and Q=0.02 m³/s.

### Different questions need different outputs

## What you are expected to learn

This lesson matches an engineering question to the required output: prediction, forecasting, diagnosis, control or optimization. It also distinguishes ML training optimization from engineering design optimization.

## Prediction and forecasting

Prediction estimates an unknown output from supplied inputs. Estimating pump power at a stated operating condition is a prediction problem.

Forecasting estimates a future outcome [18]. Tomorrow's HVAC electricity demand or PV energy generation are forecasting examples. A forecast must use only information available when the forecast is issued.

## Diagnosis, control and optimization

Diagnosis asks which condition or cause explains the evidence [10]. An unusual vibration can produce an anomaly alert, but confirming bearing damage requires additional evidence such as physical inspection.

Control selects actions to regulate system behaviour over time [7]. Adjusting a fan-speed command to maintain a target temperature is a control task.

Optimization searches feasible choices that improve an objective while satisfying constraints [19]. Selecting insulation thickness to reduce a life-cycle cost is a design-optimization example. A power prediction can inform this search, but a prediction alone does not optimize the system.

## Two different uses of optimization

ML training optimization changes internal model parameters, such as weights, to reduce a mathematical loss function [4].

Engineering design optimization changes physical design or operational variables to improve an engineering objective under physical constraints. Identify the variables, objective and limits before using the word “optimization”.

## Check your understanding

Why does predicting pump power not itself optimize pump operation?

ANSWER: Prediction estimates power for supplied inputs. Optimization also needs decision variables, an objective, constraints and a search over feasible choices.

Does an unusual vibration alert confirm bearing damage?

ANSWER: No. It indicates that investigation is required; diagnosis needs additional evidence.

## Key takeaways

- Prediction estimates an output; forecasting estimates a future output.
- Diagnosis explains evidence; control selects regulating actions.
- Optimization requires objectives, constraints and feasible decision variables.
- Training loss reduction and engineering-performance improvement are different goals.

Pause and explain: Explain why predicting pump power does not itself optimize pump operation.

### When ML is worth considering

## What you are expected to learn

This lesson explains when ML may add value to an engineering project. You will use a simple baseline, check whether the inputs and data are suitable, and interpret a hybrid residual model.

## Start with a baseline

A baseline is a simple comparison method [16]. Begin with the simplest adequate approach for the engineering decision. If a trusted equation meets the required accuracy and speed, additional ML can add maintenance burden without sufficient benefit.

ML may be worth evaluating when relevant patterns cannot be specified directly, observations are suitable for the intended use, or a costly simulator needs an approximate response model [20]. These conditions justify evaluation; they do not guarantee success.

## Four checks before proposing ML

- Purpose: state the engineering decision and required output.
- Inputs: confirm that the inputs are available when the decision is made.
- Baseline: retain a simple comparison method.
- Coverage: check that measurements represent the intended operating range.

Also state the success criterion and project scope. Data from one machine or operating condition may not represent another [21].

When checking coverage, consider whether the data represent the conditions expected at use: different loads, operating modes, shifts or seasonal environments. A model trained only on one narrow condition may not support decisions in another. State the intended operating domain and collect or evaluate evidence for the conditions that matter.

## Hybrid pump example

The physical baseline is:

P_in = Δp × Q / η

For Δp = 100,000 Pa, Q = 0.02 m³/s and η = 0.8, the hydraulic power is 2,000 W and the predicted input power is 2,500 W. If the measured input power is 2,800 W, then:

r = y − ŷ = +300 W

A hybrid model can learn a correction from residuals while retaining the physical calculation [14]. One residual does not show that the correction will apply across other operating conditions.

## Validate the proposed benefit

Compare the proposed model with the baseline for the stated purpose. Check physical assumptions against calibrated measurements and check whether observations cover the intended operating range. Add complexity only when the evidence shows a useful improvement in accuracy, speed or the required engineering outcome.

## Check your understanding

What must be stated before proposing ML for an engineering project?

ANSWER: State the decision, the inputs available at use time, the required output, the success criterion, a comparison baseline and whether representative data are available.

## Key takeaways

- Use a simple adequate baseline before adding ML.
- Check purpose, available inputs, baseline and operating coverage.
- Hybrid models retain physical structure and learn from discrepancies.
- Validate both data coverage and physical assumptions.

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

## What you are expected to learn

You will identify samples, features, targets and labels in an engineering table, then describe the shapes of the arrays used for learning.

## Read each row as an example

A dataset is a collection of examples and their associated variables and context [16]. A sample is one example. In the pump dataset, one row represents a steady operating test. Its columns include flow rate, pressure rise, shaft speed and measured electrical power.

Features are the input variables used by a model. The target is the output quantity or category to be learned. When estimating pump power, flow rate, pressure rise and speed are features; measured electrical power is the target. A numerical target supports a regression problem, while a category supports classification.

A label is a supplied target annotation. For example, an inspected bearing condition can label a vibration example. Feature and target roles depend on the question: electrical power can be a target in power estimation and an input in fault detection.

The same sample row may also be called an observation or instance in other materials. These terms refer to one example in the dataset; keep its feature values aligned with its corresponding target.

## Separate features from targets

The feature matrix X has shape (n, d): n sample rows and d feature columns. A target array y containing one scalar target for each sample has shape (n,). These shapes describe array structure, rather than the physical units of its measurements.

For 120 pump tests and three features:

- X has shape (120, 3).
- X contains 120 × 3 = 360 feature values.
- y has shape (120,), with 120 target values.

Flow rate is recorded in m³/s, pressure rise in Pa, shaft angular speed in rad/s and electrical power in W in the slide example. Keep each variable's meaning and unit associated with its column.

## Preserve row alignment

The features and target at the same row position must describe the same test. The slides use test identifiers to maintain this correspondence when extracting separate arrays. A test identifier records which example a row represents; it is not automatically a physically meaningful predictor.

## Notice when rows are time ordered

A table can contain independent tests or repeated readings from a time series [18]. When rows are successive measurements from the same machine, their order and dependence matter; treating them as independent examples can mislead evaluation. Preserve timestamps and choose splits that match the intended prediction or transfer question, as developed in Modules 10 and 12.

## Check your understanding

A table contains 120 tests, three input variables and one scalar target. What are the shapes of X and y?

ANSWER: X has shape (120, 3), and y has shape (120,). X contains 360 feature values. Each target must remain aligned with the matching test row.

## Key takeaways

- A sample is an example; features are model inputs; the target is the required output.
- Feature and target roles follow the engineering question.
- Array shapes distinguish sample rows from feature columns.
- Keep matching features, targets and test identifiers aligned.

Pause and explain: A table has 120 tests, 3 inputs and one scalar target. State the shapes of X and y.

### Measurements need context

## What you are expected to learn

You will explain why measurements need units and acquisition context, distinguish numerical quantities from categorical identifiers, and assess the limitations of reference data.

## Metadata gives measurements meaning

Metadata describes how data were obtained and what they mean [22]. Record units, sensor identifier, calibration, timestamp, sampling frequency, window length and operating state. A power value in W and the same numerical value in kW represent different magnitudes; the unit is essential to interpretation.

Sampling frequency describes the number of samples collected per unit time. A raw time sample and a feature calculated over a window are different data objects. The lesson example is vibration root mean square (RMS) over one second: the computed feature summarizes a window rather than being a single raw reading.

## Numerical quantities and categories

Numerical variables can describe continuous quantities, such as temperature, or counts, such as mechanical cycles. Categorical variables identify groups, such as material grade or machine identity.

Writing a machine identifier as a number does not give it a physical magnitude. Machine ID 12 is not necessarily twice machine ID 6. Differences and ratios between those identifiers have no physical meaning unless the field explicitly represents a quantity rather than an identity.

Some categories have an order and others do not [23]. For example, inspection labels such as healthy, watch and replace are ordinal: their order matters, but the distance from healthy to watch is not necessarily equal to the distance from watch to replace. A material type is usually nominal, with no natural order. Keep this distinction when encoding categories; assigning numbers does not automatically make them measured quantities.

## Ground truth is a reference

Ground truth is the reference measurement or annotation used for comparison. It is not a guarantee of an error-free value. Miscalibrated sensors, uncertain inspections and poorly aligned timestamps can corrupt the supplied target.

A calibrated power measurement can still have uncertainty [24]. Record provenance: the origin of the reference and how it was obtained. This context helps determine which claims the reference supports. Metadata improves interpretation but does not establish causation.

## Check your understanding

Why is machine ID 12 not necessarily twice machine ID 6?

ANSWER: The numbers identify categories or individual machines. They do not represent a physical quantity for which that ratio has meaning.

Why can a ground-truth target be imperfect?

ANSWER: It can contain measurement or annotation error, including calibration problems, uncertain inspection or timestamp misalignment.

## Key takeaways

- Keep units and acquisition metadata with measurements.
- Distinguish raw readings from features computed over time windows.
- Categorical identifiers do not imply numerical magnitude.
- Check the provenance and uncertainty of reference targets.

Pause and explain: Why is machine ID 12 not necessarily twice machine ID 6?

### Available inputs and causal claims

## What you are expected to learn

You will check whether an input exists at decision time and distinguish statistical association, predictive performance and causal claims.

## Check when information becomes available

A valid predictor uses information available when the decision is made. A repair code recorded after a failure cannot be used to predict that failure beforehand. Including it gives the model information that would not exist when an earlier warning was required.

This is information leakage [25]. A feature computed from a signal window can also leak information if the window includes measurements taken after the intended decision. Check the measurement timestamps and the window boundary against the alarm or prediction time.

## Three different questions

Correlation describes statistical association: do variables vary together?

Prediction asks whether available inputs estimate outputs on relevant unseen examples. Successful prediction establishes useful estimation under the evaluated conditions, rather than proving that an input causes the output.

Causation asks whether an intervention changes the outcome under appropriate conditions [26]. The slides distinguish observational records, evaluation on unseen data and controlled intervention evidence. Match the claim to the evidence actually available.

## Flow and motor current example

Records in which flow rate and motor current increase together show an association. Whether changing flow causes a particular current change depends on pump physics, controls and experimental conditions. A predictive coefficient alone does not establish that causal relationship.

Similarly, a temperature sensor can correlate with a fault because load changes both. Changing the recorded sensor value would not repair the equipment. Investigate the physical system before turning an association into an intervention recommendation.

## Check your understanding

Which input would be invalid for a warning issued before a failure: current vibration information or a repair code recorded after the failure?

ANSWER: The post-failure repair code is invalid because it was unavailable when the warning had to be issued. A vibration feature must also exclude measurements after that decision time.

Does a predictive association establish physical causation?

ANSWER: No. A causal claim needs evidence about interventions under appropriate physical and experimental conditions.

## Key takeaways

- Verify input availability at the intended decision time.
- Exclude post-event information and future measurements from earlier predictions.
- Correlation, prediction and causation answer different questions.
- Use physical and experimental evidence to assess causal interventions.

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

## What you are expected to learn

You will distinguish supervised and unsupervised learning from the feedback available, identify regression and classification tasks, and explain why an anomaly alert requires investigation.

## Supervised learning uses input-target pairs

In supervised learning, each training example pairs inputs with a known target [16]. The model learns a relationship between them. Predicting power from operating measurements and known measured power targets is an engineering example.

Regression predicts a continuous numerical value, such as tool wear measured in mm or pressure drop measured in Pa. Classification predicts a category or class probability, such as intact versus cracked. The target determines this distinction: numerical inputs or image inputs can support either task.

## Unsupervised learning finds structure

Unsupervised learning searches for structure without supplied target labels for the specified task [16]. Clustering groups observations according to a similarity criterion. Grouping operating profiles can reveal different load regimes or machine types.

A cluster is not automatically a health category. Similar observations may share an operating regime or sensor drift rather than a confirmed fault. Interpret the groups using the measurement context and engineering evidence.

A useful analogy is studying with an answer key versus sorting unlabeled parts. In supervised learning, examples come with reference targets, like practice questions with known answers. In unsupervised learning, the model looks for structure without supplied class labels, like grouping parts by observed similarity. These approaches answer different questions; unlabeled groups do not become confirmed fault classes without further evidence.

## Anomaly detection and fault confirmation

Anomaly detection flags departures from expected behaviour [27]. Depending on the available labels, it can use different learning setups. An anomaly is a reason to investigate rather than proof of mechanical damage.

For example, unusual vibration or current can reflect a changed load, altered control settings, sensor problems or an actual fault. The resources show physical inspection, functional testing and independent reference measurements as ways to assess the alert and establish whether a fault is present.

## When only some examples have labels

Semi-supervised learning uses a smaller labelled set together with additional unlabelled examples [28]. It can help when labels are costly, but unlabelled data do not automatically improve a model: their distribution and the method's assumptions must fit the task. Keep the labelled reference and evaluation procedure explicit.

## Check your understanding

What distinguishes regression from classification?

ANSWER: Regression has a continuous numerical target; classification has a category or class-probability output. The input format does not determine the distinction.

What additional evidence can turn an anomaly alert into a confirmed fault label?

ANSWER: Independent evidence such as physical inspection, functional testing or calibrated reference measurements is needed to confirm the fault and rule out other explanations.

## Key takeaways

- Supervised learning uses input-target pairs.
- Unsupervised learning finds structure without task-specific target labels.
- Clusters require engineering interpretation.
- An anomaly alert supports investigation; fault confirmation requires additional evidence.

Pause and explain: What additional evidence would turn an anomaly alert into a confirmed fault label?

### Self-supervised targets come from the data

## What you are expected to learn

You will explain how self-supervised learning constructs targets from observed data, follow a masked-signal reconstruction task, and distinguish model architecture from learning feedback.

## Construct targets from observations

Self-supervised learning obtains training targets from the data themselves through a target-generation rule [29]. Examples in the lesson include reconstructing a hidden part of a signal and predicting a next token from preceding tokens.

The absence of manually supplied fault labels does not remove the training objective. There are still inputs, targets and a loss used to evaluate disagreement. The difference is how the targets are obtained, rather than whether targets exist.

## Masked-signal reconstruction

The slides separate four parts of this task:

- Observation: the original measured signal.
- Constructed input: the signal with a section deliberately hidden.
- Constructed target: the original values in the hidden section.
- Objective: reduce the disagreement between reconstructed and original hidden values.

The original signal supplies the reference for training. The model receives the constructed input and estimates the missing section; its estimates are compared with the retained original values. Manual annotation of each hidden value is not required for this target-generation procedure.

Representations learned through self-supervised tasks may later be adapted to labelled tasks. This does not make the reconstruction target a manually confirmed fault label.

## Architecture and feedback are different concepts

Architecture describes the structure of a model, such as a neural network [4]. The learning setup describes how training feedback is supplied. A neural network can use manually labelled targets, self-supervised targets or reinforcement feedback.

Therefore, identifying a neural network does not identify its learning setup. State the task, the target-generation or feedback rule, and the model family separately.

## Check your understanding

In masked-signal reconstruction, where does the target come from?

ANSWER: It comes from the original measured values in the section deliberately hidden from the model's input.

Does a dataset without manually supplied fault labels imply that training has no objective?

ANSWER: No. A self-supervised task constructs its own targets from observed data and evaluates a loss against those targets.

## Key takeaways

- Self-supervised targets are constructed from observed data.
- Masking changes the input while retaining original values as targets.
- Training still has an objective and feedback.
- Model architecture does not determine a unique learning setup.

Pause and explain: In masked-signal reconstruction, where does the target come from?

### Reinforcement learning uses interaction

## What you are expected to learn

You will identify the state, action, reward, environment and policy in reinforcement learning, then apply these terms to a simulated thermal controller.

## Learning through interaction

In reinforcement learning (RL), an agent observes state information, selects an action and receives reward feedback from an environment [30]. A policy is a rule or model that maps available information to actions.

The objective is usually cumulative reward over time. An action can affect later conditions as well as its immediate reward, so the learning problem includes the consequences of successive actions. Labelled input-output examples alone do not establish this interactive reward-learning setup.

## Simulated thermal controller

The lesson resources map the RL terms to a thermal-control example:

- State: information about current temperature and target temperature.
- Action: the heater command.
- Environment: the simulated thermal system responding to the command.
- Reward: feedback reflecting temperature tracking and energy consumption.
- Policy: the rule or model selecting heater commands from available state information.

Temperature is a dimensional quantity, shown in K in the thermal slide. Heater power, when used to express the command, is measured in W. The resources provide no numerical temperatures, reward coefficients or operating limits for this example; the illustration explains the roles of the quantities.

## Rewards and safety limits

Rewards express the intended performance goal. For a thermal controller, the resources describe tracking accuracy and penalties for energy consumption. Safety constraints separately limit allowable operation, including the temperature range.

A poorly specified reward can increase a numerical score while violating the intended purpose [31]. Reward improvement does not itself establish safe behaviour. Define the actions, reward feedback and interactive environment, and assess safety using separate constraints and evidence.

## Use bounded simulation for beginner exercises

Explore RL control in a bounded simulated environment. The course does not authorize experiments on machinery. Physical testing requires appropriate authorization and validated safeguards; the existence of an RL policy does not guarantee safe exploration.

## When to consider reinforcement learning

Consider RL when actions affect later states, the objective can be expressed through feedback over time, and a suitable environment or simulator allows safe evaluation. If the desired output is a known label or a fixed rule already captures the control task, supervised learning or conventional control may be simpler to evaluate. A reward is not a substitute for explicit safety limits, and exploration on physical machinery requires separate authorization and safeguards.

## Check your understanding

Name a state, an action and reward feedback for a simulated thermal controller.

ANSWER: The state can include current and target temperatures; the action is a heater command; reward feedback can evaluate tracking error and energy consumption.

Does a high cumulative reward guarantee safe operation?

ANSWER: No. Rewards express objectives, while safety requires separately defined constraints and supporting evidence.

## Key takeaways

- RL learns decisions through interaction and reward feedback.
- A policy selects actions from available information.
- Cumulative reward accounts for consequences over time.
- Keep performance rewards and safety constraints distinct.
- Use bounded simulation for beginner control exploration.

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

## What you are expected to learn

You will investigate unusual and missing readings before changing them, explain what imputation does, and document changes without removing useful fault evidence.

## Screen measurements in context

Inspect distributions, timestamps, missing values and physical plausibility. A negative absolute pressure, duplicated timestamp or mixed W and kW values can indicate a data problem. Check what was measured and how it was recorded before selecting a correction.

An outlier is unusual relative to a comparison population [27]. It is not automatically an error. A high temperature may be the event that a fault detector needs to recognize. Removing every high-temperature reading could remove important fault examples. Noise, by contrast, describes variation or error that obscures the quantity of interest.

## Investigate missingness

A missing reading can carry information about the system [32]. A sensor may drop out during vibration or communication overload. Investigate the operating and measurement context rather than assuming that missingness is unrelated to the event of interest.

Imputation fills a missing value according to a declared rule [32]. It supplies a replacement for processing; it does not recover the original physical measurement. Record which values were changed, the rule used and the reason for the change.

## Mean-imputation example

The supplied example contains readings [20, 22, missing, 24]. The observed-value mean is:

(20 + 22 + 24) / 3 = 22

Mean imputation produces [20, 22, 22, 24]. It fills the gap but artificially reduces visible variability. The source does not specify the physical unit of these readings; interpret them as an arithmetic illustration rather than assigning a sensor quantity.

For a predictive pipeline, estimate a learned replacement from training data. Do not calculate it from the full dataset or refit it using final-test inputs.

## Choose and document the response

- Missing reading: investigate dropout or communication loss and declare the replacement rule if needed.
- High temperature: retain the operating context and investigate its significance.
- Mixed W and kW values: convert to consistent units before comparing values.
- Imputed reading: mark the changed value and record the applied rule.

## Imputation depends on why values are missing

The mean is only one replacement rule. A median can be less affected by extreme observed values, and a mode can be used for a categorical field. Forward-filling or interpolation may be appropriate for some short time-series gaps only when the measurement process justifies it; they can be misleading across a state change or a long outage. If a field is mostly missing, compare a documented feature-exclusion option with imputation. Fit any learned replacement using training data only, and retain a record of what was missing.

## Check your understanding

Why can removing all high-temperature readings damage a fault-detection dataset?

ANSWER: Some readings may represent genuine fault events. Deleting them can remove the evidence the model is intended to recognize.

Does replacing the missing value with 22 recover the original measurement?

ANSWER: No. It applies a mean-imputation rule; the original missing measurement remains unknown.

## Key takeaways

- Investigate context before deleting unusual readings.
- Missingness can itself be informative.
- Imputation estimates replacements and can change visible variability.
- Learn replacement parameters from training data and document every change.

Pause and explain: Why can removing all high-temperature readings damage a fault-detection dataset?

### Scaling and encoding

## What you are expected to learn

You will calculate min-max scaling and standardization, distinguish transformed values from original measurements, and represent categories without inventing numerical order.

## State the scaling rule

Some methods, including distance-based methods and neural training, are sensitive to feature scale [16]. Scaling transforms numerical magnitudes using a stated mathematical rule. Specify that rule rather than relying on an ambiguous term such as “normalization”.

Min-max scaling is:

x_scaled = (x − x_min) / (x_max − x_min)

Here x is the observation and x_min and x_max are the stated bounds. All three use the same physical unit; x_scaled is dimensionless. For bounds 0–100 °C and x = 25 °C, x_scaled = 25 / 100 = 0.25. This transform maps those bounds to 0 and 1.

## Standardization uses training statistics

Standardization is:

z = (x − μ_train) / σ_train

μ_train is the training mean and σ_train is the training standard deviation. The observation and mean share a unit; the standard deviation has the corresponding difference unit. The resulting z-score is dimensionless.

For x = 60 °C, μ_train = 40 °C and σ_train = 10 °C, z = (60 − 40) / 10 = 2. For the original course example x = 25 °C with the same training statistics, z = −1.5.

Keep the original measurements and units for physical interpretation. A dimensionless transformed value does not replace that record. Apply stored training statistics to validation and test inputs; do not recalculate them from those sets. A constant feature gives a zero denominator and requires an explicit handling rule.

## Encode categories without false magnitude

Encoding represents categories numerically. Assigning types A, B and C the values 1, 2 and 3 can impose an unsupported order and distance between categories.

One-hot encoding instead uses separate binary indicator columns [33]. For three known categories, the slide example uses A: [1, 0, 0], B: [0, 1, 0] and C: [0, 0, 1]. These indicators are dimensionless and identify membership rather than physical magnitude.

Fit category handling on training data and declare how an unseen category will be treated. Do not invent an ordering merely because a model needs numerical inputs.

## Choose scaling for the method and data

Scaling is most important when a method uses feature distances or optimization sensitive to feature magnitudes; tree splits are generally not changed just by a consistent monotonic rescaling. Min-max scaling maps stated training bounds to a chosen range but does not make future values stay inside that range. Standardization expresses values relative to training mean and standard deviation; it is not a general outlier remedy. Select the transformation for the model and data, fit it on training examples, and check its effect on validation data rather than treating one method as universally best.

In scikit-learn, StandardScaler is a common implementation of standardization and OneHotEncoder is a common implementation of one-hot encoding. These names identify tools, not a reason to apply a transformation blindly. Fit learned transformations on training data only, then apply the fitted transformation consistently to later data.

## Check your understanding

Standardize 60 °C using a training mean of 40 °C and standard deviation of 10 °C.

ANSWER: z = (60 − 40) / 10 = 2, a dimensionless value. Reuse the training statistics when transforming test inputs.

## Key takeaways

- State the exact scaling equation.
- Retain original units and interpret transformed outputs as dimensionless.
- Apply fitted training statistics consistently.
- Declare handling rules for constant features and unseen categories.
- One-hot indicators avoid unsupported numerical ordering.

Pause and explain: Standardize 60°C using training mean 40°C and standard deviation 10°C.

### Features and repeatable pipelines

## What you are expected to learn

You will construct meaningful engineering features, enforce their availability at prediction time, and use a repeatable pipeline with documented input requirements.

## Build features from engineering knowledge

Feature engineering constructs useful inputs using knowledge of the problem [10]. The course examples include pressure rise, hydraulic power, vibration RMS, frequency-band energy and temperature above ambient. The feature must be meaningful for the task and available when the prediction is made.

The slides illustrate a hydraulic-power feature:

P_h = Δp × Q

Pressure rise Δp is measured in Pa, volumetric flow rate Q in m³/s and hydraulic power P_h in W. This combines measured quantities using a physical relationship rather than treating the columns as unrelated numbers.

## Generate feature ideas systematically

Start from the decision and ask what physical relationship could matter. Consider derived quantities such as products or ratios when their units and assumptions are clear, changes over time when a trend is available at decision time, and window statistics when the signal history is relevant. Each feature must use only available information, preserve interpretable units where possible, and be evaluated for added value rather than included solely because it can be calculated.

## Respect signal-window boundaries

A windowed feature uses measurements from a specified time interval. For an earlier alarm, the interval must exclude future samples. Including measurements after prediction time leaks information that would not be available during use.

Document the window and the decision time alongside the feature. A physically plausible feature can still be invalid for prediction if it uses information obtained too late.

## Split, fit and apply consistently

A pipeline bundles preprocessing and modelling into a repeatable sequence [33]. The resources distinguish learning preprocessing parameters from applying them:

- Split examples before fitting learned preprocessing.
- Fit scalers, imputers and learned feature selection within the training folds.
- Store the fitted parameters and rules.
- Apply the stored transformations to validation and test inputs without refitting on those sets.

Fitting estimates parameters such as a mean or a replacement value. Applying uses the stored parameters on later inputs. Recomputing a scaler from final-test data crosses the evaluation boundary even if no test target is used.

A scikit-learn Pipeline can keep learned preprocessing and an estimator together so that fitting and prediction use the same sequence of steps. The pipeline still must be fitted inside the training portion of each evaluation split; wrapping a leaky workflow in a pipeline does not fix an invalid split.

## Record the input contract

An input contract states what the stored model expects, including units and missing-value rules. If power values change from W to kW, the stored numerical model will not necessarily interpret the new values correctly unless the expected conversion is applied.

Keep original units, the missing-value rule, modified values and the physical justification for derived features in the evidence record. Cleaning and transformations influence the model's inputs and must remain traceable.

## Check your understanding

Which statistics should a scaler use when transforming the final test set?

ANSWER: Use the stored statistics fitted on training data. Apply them unchanged rather than fitting the scaler on the final test set.

Can a signal feature include measurements taken after the intended alarm time?

ANSWER: No. That would introduce future information unavailable when the alarm had to be issued.

## Key takeaways

- Construct meaningful features using available engineering information.
- Exclude future measurements from earlier prediction windows.
- Separate training-only fitting from later application.
- Document expected units, missing-value rules and modified values.

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

## What you are expected to learn

You will distinguish a model from its learning algorithm and explain what changes during training, inference and retraining.

## A model represents a relationship

A model maps inputs to outputs. A simple linear model is:

ŷ = b_0 + b_1 x

Here x is the input, ŷ is the predicted output, b_0 is the intercept and b_1 is the slope. The equation describes the mapping; it does not describe how the coefficients were obtained.

A learning algorithm is the procedure that obtains or updates parameters from data [2]. Least squares, the example in the resources, estimates coefficients by minimizing the sum of squared residuals. A residual is the difference between a measured output and its prediction. Different fitting procedures can be used for related model structures.

## Training fits; inference applies

Training, also called fitting, uses examples to determine parameter values. For a linear model, those fitted values are the intercept and slope.

Inference applies the fitted mapping to an input. Routine prediction changes the input and calculated output without automatically changing the coefficients. Retraining is a separate fitting operation with its own data and validation requirements.

## Worked linear example

The supplied model is:

ŷ = 2 + 3x

Its intercept is 2 and its slope is 3. At x = 4, inference gives ŷ = 2 + 3 × 4 = 14. Changing x changes the prediction; fitting again may change the intercept or slope.

The resources do not assign a physical input quantity or SI units to this arithmetic example. In a physical application, the input and output units must be specified: the intercept has the output unit and the slope has output units per input unit. Do not interpret 14 as a particular engineering quantity without that information.

For a one-input linear model, the intercept is the predicted output at x = 0, and the slope describes the predicted change per unit change in x. The slope's units are output units divided by input units. Whether either coefficient has a useful physical interpretation depends on the measurement range and model assumptions; Module 7 works through these units in detail.

A compact code example shows the distinction between fitting and inference:

```python
model.fit(X_train, y_train)
predictions = model.predict(X_new)
```

The fit method learns parameters from the training examples. The predict method applies the fitted model to new inputs; it does not retrain the model.

## Check your understanding

In the example at x = 4, which operation produces 14, and which values remain fixed?

ANSWER: Inference produces the output 14. The fitted intercept 2 and slope 3 remain fixed during that prediction.

Does generating another prediction automatically retrain the model?

ANSWER: No. Retraining is a separate parameter-fitting operation that requires data and validation.

## Key takeaways

- A model describes the input-output mapping; a learning algorithm fits its parameters.
- Training determines fitted values.
- Inference applies those values to inputs.
- Retraining requires a separately evaluated fit.

Pause and explain: Predict ŷ for x=5 with ŷ=2+3x. Which numbers are parameters?

### Parameters and hyperparameters

## What you are expected to learn

You will distinguish learned parameters, hyperparameters and supplied engineering assumptions, then separate the training loss from engineering acceptance criteria.

## Parameters are fitted values

Parameters are values obtained within model fitting. Examples include regression coefficients, neural weights and biases, and tree split values. Their role follows how they are obtained and used, rather than simply whether they appear as numbers in software.

For the linear model from Lesson 6.1, the fitted intercept and slope are parameters. They describe the fitted relationship and remain fixed during routine inference.

## Hyperparameters control structure or training

Hyperparameters are settings that govern model structure or training [4]. Examples in the resources include maximum tree depth, learning rate and batch size. They are usually selected through validation rather than fitted by the same operation that learns the model parameters.

A fitted regression slope and a chosen tree-depth limit therefore have different roles: the slope is learned within fitting, while the depth limit governs the permitted tree structure. The distinction depends on the method and the acquisition of the value.

## Supplied physical values have another role

A fixed pump efficiency supplied to an engineering calculation is a model assumption or supplied engineering parameter. It is not a learned ML parameter unless it is estimated during fitting. Calling a value a parameter in a physical model does not establish that an ML algorithm learned it.

## Loss and acceptance answer different questions

A training loss quantifies disagreement with the chosen training objective or another penalty. Mean squared error is an example. It guides fitting, but it is not a universal quality or safety score.

An aggregate error can conceal rare large failures. Reducing the loss does not by itself show that every operating condition is acceptable. Evaluation metrics describe assessed performance, while engineering acceptance criteria state the requirements that performance must satisfy. These can differ from the training objective.

## Mean absolute and squared error emphasize different things

Mean absolute error averages absolute residual magnitudes, while mean squared error squares them before averaging [34]. Squaring gives large residuals more influence, so the chosen loss changes what fitting emphasizes. Select an objective that matches the task and inspect errors in engineering units; neither loss by itself encodes asymmetric consequences or defines an acceptance limit.

## Check your understanding

Which is a hyperparameter: a fitted slope or a chosen maximum tree depth?

ANSWER: The chosen maximum tree depth is a hyperparameter. The slope obtained during fitting is a parameter.

Does a low training loss establish safe engineering use?

ANSWER: No. Engineering acceptance needs its own criteria and supporting evaluation; the training objective alone does not establish safety.

## Key takeaways

- Learned parameters and chosen training settings serve different roles.
- Supplied physical assumptions are not automatically learned ML parameters.
- State the chosen loss and its purpose.
- Evaluate engineering acceptance separately from training loss.

Pause and explain: Is a fitted slope or a chosen maximum tree depth a hyperparameter?

### Baselines prevent empty success claims

## What you are expected to learn

You will interpret a performance result using a fair baseline, identify the context needed for an error metric, and explain what a random seed helps reproduce.

## Select a simple comparison

A baseline is a simple comparison approach. For regression, the resources suggest predicting the training mean or using a trusted physical relationship. For classification, a majority-class rule provides a comparison, together with suitable fault-sensitive metrics.

Evaluate the proposed model and baseline on the same evaluation examples with comparable information available at prediction time. State the metric. A model's training score alone is not a fair held-out comparison.

## Interpret the supplied MAE example

Mean absolute error (MAE) measures the average absolute difference between predictions and reference outputs. It has the same unit as the output being predicted.

On the same held-out tests, the supplied ML model has MAE 1.2 kW and the physical baseline has MAE 0.8 kW. These are 1,200 W and 800 W respectively. The baseline has the lower MAE, so the more elaborate model has not demonstrated an improvement on that metric.

This comparison does not settle every engineering consideration. Cost, interpretability and evidence for the operating range also matter. Merely stating that a system uses AI is not evidence of a performance benefit.

## Supply the context behind the score

To interpret an isolated error value, record:

- The target quantity and unit.
- The evaluated population and operating conditions.
- The data split and which examples informed each stage.
- The reference measurement uncertainty.
- The baseline error on the same evaluation examples.

Keep preprocessing and model-version records as well. This evidence allows the result to be assessed within the conditions actually tested.

## Repeatability and validity

A random seed initializes a pseudorandom procedure [35]. Under stated conditions, it helps repeat a random split or training procedure. It does not prove accuracy, eliminate uncertainty or make a biased dataset representative.

Record the seed along with the data split, preprocessing and version. Repeating the same procedure is useful for checking a result, but it does not establish that the procedure or data are suitable for the engineering decision.

If a more complex ML model performs worse than a fair baseline, report that result rather than forcing a case for ML. First check units, split integrity, preprocessing, implementation and the evaluation population. If the comparison is sound and the baseline remains better for the stated purpose, using the baseline is a valid engineering decision. A more complex model should earn its extra maintenance and validation burden with evidence of a real benefit.

Before sharing a trained model, record its intended task and operating domain, data source and date range, split procedure, preprocessing steps, model settings, evaluation results, known limitations, software versions and random seed where applicable. A seed helps repeat a randomized procedure under stated conditions; it does not guarantee identical results across different software, hardware or parallel execution environments.

## Check your understanding

What information is needed to interpret “our MAE is 1.2 kW”?

ANSWER: Identify the target, evaluated examples and conditions, data split, reference uncertainty, and a fair baseline result. The supplied baseline has MAE 0.8 kW on the same tests.

Does using a random seed guarantee a representative dataset?

ANSWER: No. It helps repeat the specified random procedure under stated conditions; representativeness needs separate evidence.

## Key takeaways

- Compare with a simple baseline using common examples, available information and stated metrics.
- Interpret error magnitudes with units and evaluation context.
- Document the data split, preprocessing and model version.
- A random seed supports repeatability, not a guarantee of validity.

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

## What you are expected to learn

You will interpret a linear regression equation, identify coefficient units, and calculate a prediction and an observation-minus-prediction residual.

## Model a numerical response

Linear regression models a numerical response using fitted coefficients [16]. The heater example relates temperature rise to power:

ΔT = b_0 + b_1 P

- ΔT: temperature rise in K.
- P: heater power in W.
- b_0: intercept in K.
- b_1: slope in K/W.

The intercept is the model's predicted rise at zero input power. The slope describes the change in predicted rise per unit change in power. Multiplying a slope in K/W by power in W gives K, so both terms have the same unit as the output.

A fitted coefficient is not automatically a verified physical property. Physical interpretation requires appropriate assumptions and measurement design.

## Fit coefficients using least squares

Least squares selects coefficients by minimizing the sum of squared residuals [16]. This is different from applying a fitted equation to a new input.

“Linear” here means linear in the fitted coefficients. A polynomial fitted by least squares can also be linear in its coefficients even though its response is curved. This course begins with a straight line so that predictions and discrepancies are easy to inspect.

## Calculate the supplied prediction

The example uses b_0 = 1 K and b_1 = 0.6 K/W. At P = 10 W:

ΔT_predicted = 1 K + (0.6 K/W × 10 W) = 7 K

The measured rise is 8 K. Using the course's residual convention:

r = y − ŷ = 8 K − 7 K = +1 K

Here y is the measured rise, ŷ is its prediction and r is the residual, all in K. The positive sign means that the prediction is below the measurement.

Adjusting the line in the course activity changes the proposed model. It does not collect a new measurement or perform a physical experiment. The illustrative calculation is teaching evidence rather than a validated industrial recommendation.

With several inputs, the same idea extends to a model such as `y_hat = b_0 + b_1 x_1 + b_2 x_2`. Each coefficient describes the model's change per unit of its feature when the other inputs are held fixed. Its units are output units divided by that feature's units; the fitted association is not automatically a causal or physical law.

## Check your understanding

What units must the slope have when predicting temperature rise in K from heater power in W?

ANSWER: K/W. Multiplying by the input power in W produces a temperature-rise term in K.

What does the residual +1 K mean in the supplied example?

ANSWER: The measured rise exceeds the prediction by 1 K, so the model underpredicts that observation.

## Key takeaways

- Interpret coefficients together with their units and assumptions.
- Least squares fits coefficients; inference applies the fitted equation.
- A residual is measured output minus predicted output in this course.
- Adjusting a model does not create new experimental evidence.

Pause and explain: What units must the slope have when predicting K from W?

### Three useful metrics and their limits

## What you are expected to learn

You will calculate MAE and RMSE, interpret R², and explain why aggregate metrics should be accompanied by residual inspection.

## Begin with signed residuals

For each evaluated observation, r_i = y_i − ŷ_i. Here y_i is the measured output, ŷ_i is its prediction and i identifies the observation. A positive residual indicates underprediction; a negative residual indicates overprediction.

The supplied temperature-rise example has measurements [5, 8, 10] K and predictions [4, 10, 7] K. The residuals are [1, −2, 3] K.

## MAE and RMSE retain target units

Mean absolute error (MAE) averages the residual magnitudes:

MAE = (1/n) Σ |r_i|

Root mean squared error (RMSE) takes the square root of the mean squared residual:

RMSE = √((1/n) Σ r_i²)

n is the number of evaluated observations, a dimensionless count. Both metrics have the target unit, here K. MAE removes the signs before averaging; RMSE squares the errors and gives larger magnitudes more influence.

For the three supplied residuals:

MAE = (1 + 2 + 3) K / 3 = 2 K

RMSE = √((1 + 4 + 9) K² / 3) ≈ 2.160 K

RMSE is at least as large as MAE for the same errors [34]. They are equal when all absolute residual magnitudes are equal.

## R² is a relative score

R² = 1 − SSE/SST

SSE is the sum of squared prediction residuals. SST is the sum of squared deviations of the evaluated targets from their evaluation-set mean. Both have squared target units, which cancel; R² is dimensionless.

The comparison is with predictions equal to the evaluation-set mean. R² can be negative when the model's squared error exceeds that comparison. The supplied example gives approximately −0.1053.

If the evaluation target is constant, SST is zero and the usual formula requires explicit handling. A high R² does not establish causation, a small physical error or safe engineering operation.

MAE averages absolute errors, while RMSE squares errors before averaging and then takes a square root. RMSE therefore gives large residuals more influence than MAE. Neither metric is universally best: compare them with the cost of large errors in the application, and inspect residuals by operating condition rather than relying on one aggregate value.

## Inspect where errors occur

Plot signed residuals against load, time and operating regime, keeping their physical units. An aggregate score can hide a narrow region with severe errors. Inspect the distribution and operating conditions alongside the overall metrics.

A residual plot can reveal patterns hidden by one aggregate score [36]. For example, residuals that curve with load may indicate that a straight-line relationship misses structure, while a step change may point to a different operating regime or omitted input. A pattern is a diagnostic clue, not a unique explanation; inspect data quality, operating context and model assumptions before choosing a correction.

R-squared compares the model's squared error with the error from predicting the mean target on the evaluated data. A value below zero means the model performed worse than that mean-prediction baseline on that evaluation set. It is a comparison, not a safety threshold; interpret it alongside errors in engineering units and the intended use.

## Check your understanding

For residuals −2 K and +2 K, are MAE and RMSE equal?

ANSWER: Yes. Both are 2 K because the absolute magnitudes are equal. Averaging signed residuals to get zero would not calculate either metric.

## Key takeaways

- Preserve residual signs for interpretation.
- MAE and RMSE report error in target units.
- R² is dimensionless, can be negative and requires care for constant targets.
- Inspect errors across operating conditions, not only the aggregate score.

Pause and explain: For errors −2 and +2 K, are MAE and RMSE equal?

### A minimal, honest regression workflow

## What you are expected to learn

You will follow a regression workflow that separates fitting, model selection and final evaluation, then report the evidence and limitations of the result.

## Define the prediction problem

State the output and the inputs available when the prediction is made. Inspect the measurements, their units and their provenance. Set aside relevant unseen examples before fitting learned preprocessing and the model.

Data provenance identifies the origin of the examples, including whether they are synthetic or measured [37]. The evaluation should address the intended use rather than merely the examples easiest to divide.

## Use three distinct stages

- Training: fit model parameters and learned preprocessing on training data.
- Validation: compare choices, such as model configurations and input features.
- Final test: evaluate the locked model after selection is complete.

The final test estimates performance on data withheld from the fitting and selection stages. Use stored preprocessing on those examples without refitting it from their values.

Compare with a training-mean baseline and, where available, a physical baseline on the same evaluation examples. Report MAE and RMSE in the target units; treat R² as a relative dimensionless score rather than an error in W or K.

There is no universally correct train-validation-test percentage [38]. Choose boundaries that leave enough relevant examples for fitting and assessment while respecting time, machine, event and class structure. With limited data, cross-validation can support development, but it does not justify repeatedly tuning against a final test. Once test results guide changes, the test has become part of development and needs new independent evidence for an unbiased final assessment.

## Understand the pump laboratory's scope

Lab 2 uses independent synthetic pump operating designs. It compares ordinary inputs with hydraulic power as a physically derived feature. The random split is appropriate for this stated independent-design teaching problem; forecasting needs a different split that respects time.

The reference reports final-test metrics only after validation selection. Synthetic teaching data demonstrate the procedure but do not validate physical equipment safety. A model trained on one laboratory pump also does not automatically transfer to every pump.

## Report the result with its limits

A regression report should state:

- The predicted quantity and its units.
- Data provenance and the split strategy.
- Held-out metrics and fair baseline performance.
- The evaluated operating range and limitations on transfer.

Explain what the evaluation supports. A high R² alone cannot support a global safety claim, and an overall average can conceal poor performance within part of the operating range.

## Check your understanding

What is the difference between validation and the locked final test?

ANSWER: Validation supports choices among models or features. The locked final test estimates performance after those choices are complete.

State two limitations to include alongside a regression score.

ANSWER: State whether the data are synthetic or measured and identify the operating range or machine population evaluated. Evidence from one laboratory pump does not establish performance on every pump.

## Key takeaways

- Define available inputs and inspect measurement evidence.
- Separate training, validation and final testing.
- Compare against baselines and retain metric units.
- Match the split strategy to the learning problem.
- Report provenance, domain limits and the scope of the evidence.

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

## What you are expected to learn

You will distinguish classes from scores, interpret the four confusion-matrix outcomes, and explain how a threshold affects fault alerts.

## Convert a score into a decision

A classifier predicts a category or a score associated with a class. A binary detector distinguishes two classes. In the supplied example, a decision threshold converts a score into a fault prediction: label fault when score ≥ threshold.

Some outputs are probabilities; others are decision values [12]. A value between zero and one does not automatically establish a calibrated probability. Check the score's definition and calibration evidence before interpreting it as a probability. Selecting a cutoff and demonstrating probability calibration are distinct questions.

## Declare the positive class

In this course, fault is positive and healthy is negative. These are evaluation labels, not judgements about whether an outcome is desirable. Compare the prediction with the actual reference class:

- True positive (TP): an actual fault is predicted as a fault.
- False negative (FN): an actual fault is predicted as healthy; the fault is missed.
- False positive (FP): an actual healthy example is predicted as a fault; this is a false alarm.
- True negative (TN): an actual healthy example is predicted as healthy.

A confusion matrix records these counts for a stated threshold and evaluation dataset [39]. Read its actual-class and predicted-class headings explicitly; their positions can differ between diagrams. The meanings of TP, FN, FP and TN remain the same.

## Select a threshold using validation

Changing the threshold changes decisions even when the scores stay fixed. Lowering it makes more examples eligible for a positive prediction. This generally catches more faults but can also produce more false alarms; a threshold change need not change every count.

Choose the threshold on validation examples in light of missed-fault and false-alarm consequences. Then evaluate the selected threshold on the final test without repeatedly tuning it using test labels.

## Check your understanding

If fault is positive, what does a false negative represent?

ANSWER: An actual fault predicted as healthy: a missed fault.

Does a score of 0.9 alone establish a fault probability?

ANSWER: No. Its definition and calibration evidence are still needed before treating it as a probability.

## Key takeaways

- Distinguish a score, a probability and a thresholded decision.
- Declare the positive class before reading counts.
- FN means a missed fault; FP means a false alarm.
- Select thresholds using validation evidence and error consequences.

Pause and explain: If fault is positive, what does a false negative represent?

### Read metrics by their question

## What you are expected to learn

You will calculate accuracy, precision, recall and F1, connect each metric to its question, and interpret the supplied fault-detection example.

## Choose a metric by its question

With fault as the positive class:

Accuracy = (TP + TN) / N

This asks what fraction of all examples were correctly classified. N is the total number evaluated.

Precision = TP / (TP + FP)

This asks what fraction of predicted fault alerts were actual faults.

Recall = TP / (TP + FN)

This asks what fraction of actual faults were detected.

F1 = 2TP / (2TP + FP + FN)

F1 combines precision and recall through their harmonic mean when defined [40]. It is not a universal engineering safety objective. TP, TN, FP, FN and N are dimensionless counts; the metric ratios are dimensionless and may be reported as percentages.

The harmonic mean used by F1 is pulled toward the smaller of precision and recall. This prevents a high value on one from fully hiding a very low value on the other. F1 is still only a summary: it does not encode the relative engineering cost of missed faults and false alarms.

## Calculate the supplied example

The resources give TP = 8, FP = 2, FN = 4 and TN = 86, for N = 100 evaluated examples:

- Accuracy = (8 + 86) / 100 = 94%.
- Precision = 8 / (8 + 2) = 80%.
- Recall = 8 / (8 + 4) ≈ 66.7%.
- F1 = 16 / (16 + 2 + 4) ≈ 72.7%.

There are ten alerts, eight of which correspond to faults. There are twelve actual faults, of which eight were detected and four missed. The high overall accuracy therefore does not describe fault detection adequately on its own.

## Report undefined cases explicitly

A zero denominator requires an explicit reporting rule. If there are no positive predictions, precision's denominator is zero. No alerts do not supply evidence of useful positive-class precision. Record the counts and the rule rather than silently presenting an undefined quantity as an established result.

## Recognize ROC-AUC and its limits

ROC-AUC summarizes ranking behaviour through a receiver operating characteristic curve across thresholds [39]. Recognize it here as a dimensionless discrimination measure. For rare faults, also inspect precision-recall performance and the class counts [41].

Performance at the selected operating threshold still matters. No single metric replaces evidence about the operating domain or the consequences of errors.

## Check your understanding

For TP = 8, FP = 2 and FN = 4, what are precision and recall?

ANSWER: Precision is 80%; recall is approximately 66.7%. They use different denominators: predicted alerts and actual faults respectively.

## Key takeaways

- Accuracy, precision and recall answer different questions.
- Include counts so missed faults remain visible.
- F1 is a combined score rather than a safety requirement.
- Declare zero-denominator handling and assess relevant operating metrics.

Pause and explain: Calculate precision and recall for TP=8, FP=2, FN=4.

### Imbalance and deployment consequences

## What you are expected to learn

You will explain why class imbalance can make accuracy misleading, evaluate a threshold on separate data, and identify the evidence needed before acting on alerts.

## Compare with the majority-class baseline

Class imbalance means that some classes are much more frequent than others [42]. Fault examples may be rare compared with healthy operation.

In the supplied dataset of 99 healthy examples and one fault, always predicting healthy gives 99% accuracy. It detects none of the actual faults, so fault recall is 0%. The impressive accuracy belongs to a rule that never identifies the event of interest.

Compare the proposed detector with this majority-class baseline and inspect positive-class performance. Accuracy alone does not establish useful rare-fault detection.

Possible responses to imbalance include collecting more representative fault examples, using class-weighted fitting, or resampling the training data. These are development choices, not guaranteed fixes. Apply resampling only within training folds, keep validation and test populations representative of intended use, and check that any synthetic examples remain physically plausible. Threshold choice is a separate decision that should reflect the consequences of false alarms and missed faults.

## Separate threshold selection from testing

Lab 3 uses synthetic scores and labels to demonstrate threshold selection. It is not a trained or calibrated machinery detector. Record TP, FP, FN and TN for the decisions produced.

Use validation examples to select the threshold, considering false alarms and missed faults. Evaluate the chosen threshold on a separate fixed test population. Report the class counts and selected threshold alongside the metrics so that the result's meaning is clear.

## Connect alerts to an engineering procedure

Missed alarms and false alarms have different consequences. Their physical and economic costs depend on the machinery and intended use. A false alarm may consume inspection resources; a missed fault may leave damage undetected. The classroom example does not assign universal costs to these outcomes.

Before acting on a detector output, state who receives the alert, when an inspection is required and what evidence is needed for a maintenance decision. The supplied workflow connects an alert with evidence review, inspection and a subsequent action.

Synthetic demonstrations illustrate these decisions; they do not authorize deployment or validate equipment safety. A threshold that performs well in the exercise requires further operating-domain evidence before it can support a real application.

## Report more than aggregate accuracy

- Identify the positive class and the evaluated class counts.
- State the selected threshold and how it was chosen.
- Report missed faults and false alarms as well as precision and recall.
- Describe the evaluated population, alert recipients and required evidence before action.

## Accountability before acting on an alert

For a safety-relevant fault detector, define who receives an alert, who checks the evidence, who may stop equipment and who records the final decision [9]. A model score alone should not silently trigger a consequential action unless that use has been separately justified, tested and authorized. False alarms can cause avoidable downtime; missed faults can leave hazards undetected. Thresholds and procedures should reflect both consequences and be reviewed with the people responsible for the equipment.

## Check your understanding

Why can a detector with 99% accuracy be useless for rare faults?

ANSWER: In the supplied example, predicting all 100 examples as healthy correctly labels 99 healthy cases but misses the only fault. Its fault recall is 0%.

Does a successful synthetic threshold exercise approve machinery deployment?

ANSWER: No. The exercise demonstrates evaluation, while real use needs appropriate evidence, inspection procedures and authorization.

## Key takeaways

- Compare rare-fault detection against the majority-class baseline.
- Select thresholds on validation data and evaluate a separate fixed test.
- Report counts and error consequences alongside metrics.
- Define the alert-to-inspection procedure and the evidence required for action.

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

## What you are expected to learn

You will distinguish weighted predictive models from distance and margin-based models, and explain why method choice depends on the output, data structure and evaluation evidence.

## Parametric predictive models

Linear regression predicts a numerical value from a weighted combination of input features. In a schematic form, feature values x₁ and x₂ pass through weights w₁ and w₂ and are combined to produce a numerical prediction ŷ. The model name does not establish that the prediction is accurate; performance must be checked on appropriate unseen data.

Read the slide diagram from left to right: input feature values enter the model, weights determine their contributions, and the combined contributions produce the prediction. The predicted continuous pressure in the method-comparison table is a numerical output. It differs from a category such as fault or healthy. The diagram is schematic and supplies no numerical coefficients or physical units for its generic symbols.

Logistic regression is commonly used for binary classification [16]. It combines features and weights, then applies a mathematical link function to estimate a class probability. For example, it can estimate the probability of a binary fault. The word regression in the method name does not mean that the output must be a continuous engineering measurement.

The link function is the additional mathematical mapping between the combined input contributions and the probability output. When reading the slides, distinguish the weighted combination from this final mapping. Linear and logistic regression can therefore use similar input-combination diagrams while serving different output tasks. Their names describe model construction; neither name proves useful performance on the available data.

## Geometric boundary models

k-nearest neighbours, or kNN, estimates an output using spatially nearby examples under a defined distance rule [43]. For an engineering use, nearby operating points can support an estimate of power generation. Because the method depends on distances, the selected features, their units and their scaling affect which examples count as neighbours.

Here, nearby refers to positions in feature space: the coordinates represent input features describing operating points. It does not mean that two machines must be physically close to one another. Read the diagram by identifying the point requiring a prediction, its neighbouring examples and the distance rule that makes them neighbours. The course introduces this mechanism without specifying a numerical neighbour count or a complete implementation.

A support vector machine, or SVM, learns a separating boundary for data classification [44]. It uses a geometric margin between classes. Kernel methods allow some support-vector techniques to express nonlinear relations, and related support-vector methods can also perform numerical regression. These are geometric representations; they do not by themselves establish a physical limit.

In the slide diagram, the two groups of markers represent different classes, the central line represents the separating boundary, and the flanking lines illustrate the margin. The kernel is a mathematical means of expressing nonlinear relationships within the method. This lesson requires you to recognize these roles rather than derive a kernel equation or implement the training procedure.

## Unit scaling and method selection

Changing a length from metres to millimetres leaves the physical separation unchanged but multiplies its numerical value by 1,000. A distance-based algorithm can therefore change its neighbour rankings when feature units change. Feature scaling must match the physical task and its units.

Select a method by the required output format, dataset size, data structure and performance checks. Small tabular data may suit parametric or geometric methods, whereas raw images may require other architectures. The choice must be justified by evidence for the intended engineering task.

Use the source's selection questions in order: What output is required? What structure does the method assume? How much data are available? How will performance on unseen examples be checked? The tabular-data and raw-image distinction is a consideration in selection, rather than a guarantee that one method always succeeds for a particular data format.

In scikit-learn, common implementation names include LogisticRegression, KNeighborsClassifier and SVC for a support-vector classifier. Check each method's assumptions and scaling needs, and compare candidates with the same valid split and preprocessing. These names are useful when moving from the lesson to a lab; no one algorithm is best for every engineering dataset.

## Check your understanding

Why can a distance-based method change after switching a length feature from metres to millimetres?

ANSWER: The physical length is unchanged, but its numerical coordinate is multiplied by 1,000. This changes that feature's contribution to a distance calculation and can alter neighbour rankings when compared with other features. It does not imply that every multifeature distance increases by exactly 1,000.

How do linear and logistic regression differ in their typical outputs?

ANSWER: Linear regression predicts a numerical value, such as continuous pressure. Logistic regression commonly estimates a class probability, such as a binary fault probability, through a link function.

## Key takeaways

- Linear regression predicts numbers; logistic regression estimates class probabilities through a link function.
- kNN uses nearby examples, while SVM uses a separating margin and may use a kernel.
- Distance-based methods require careful unit scaling.
- Choose methods by output, data structure, dataset size and verified performance.

Pause and explain: Why could a distance-based method change after switching a length feature from m to mm?

### Trees and ensembles

## What you are expected to learn

You will explain how decision trees partition inputs, how random forests and boosting combine models, and why learned boundaries require machine- and regime-specific validation.

## Decision trees partition input space

A decision tree divides input examples through feature tests [45]. Tests on variables such as load or vibration create piecewise prediction regions, and a terminal region produces the corresponding prediction. A small tree permits direct engineering inspection. A deep tree uses many partitions and can fit training-specific patterns, so its complexity requires validation.

Follow the construction diagram in three stages. First, the root input enters the tree. Next, successive feature tests determine the applicable branch. Finally, the input reaches a terminal region and receives that region's prediction. Partitioning means dividing the input space into these regions. Piecewise means that the prediction is determined separately within each region.

The load-and-vibration example explains why the regions matter: operating examples are separated by tests on their feature values. The resources provide no numerical split threshold for this example, so the diagram cannot supply an equipment setting. A small tree's inspectability means its tests can be examined; it does not establish that those tests are physically valid.

Tree predictions are piecewise outputs. They differ from a smooth response equation, even when both are used to estimate the same engineering quantity. A learned threshold is an empirical rule produced by the data and training procedure; it is not automatically a physical fault limit or a manufacturer specification.

## Random forests aggregate randomized trees

A random forest combines multiple individual models into one ensemble [46]. It uses randomized trees constructed in parallel and aggregates their predictions, for example by averaging or voting. Aggregation reduces reliance on any one decision tree and can reduce variance, but it adds computational cost and can reduce interpretability.

An ensemble is a combination of multiple models. In the forest diagram, several trees each supply a prediction to a common aggregation block. Read parallel as the construction contrast with sequential boosting: the diagram does not claim that the software must execute every tree simultaneously. The final output combines the tree predictions rather than simply selecting one tree's output.

## Boosting corrects errors sequentially

Boosting constructs models sequentially rather than in parallel [47]. Each later stage targets remaining objective errors from earlier stages, so the final output is a sequence of error-correcting additions. Boosting is therefore mechanically different from randomized parallel aggregation. Its model complexity must be checked with strict validation.

Read the boosting diagram as an initial model, an assessment of its remaining error, and a subsequent model stage that addresses that error. The dependence on earlier stages is the defining distinction in this lesson. A forest aggregation diagram and a boosting sequence both contain several models, but they describe different ways of constructing and combining them.

## Engineering limits and validation scope

An algorithm can learn a prediction rule from load and vibration without proving that the rule is a causal physical limit. Validate a model explicitly across the target operating regimes and relevant equipment. A model validated for one regime or equipment unit does not automatically apply to another.

Educational examples and synthetic data demonstrate construction and evaluation ideas. They do not constitute validation for operational industrial hardware. Operational validation requires relevant machine data and evidence appropriate to the intended use.

The method-limitations table connects each construction with a practical concern: a small tree has restricted representation; a deep tree risks training-specific fitting; a forest adds cost and makes interpretation more difficult; boosting requires validation of complexity. Use these concerns alongside performance evidence when comparing methods. Adding models alone does not establish a better engineering decision.

In scikit-learn, RandomForestClassifier and GradientBoostingClassifier are common classifier interfaces for two tree-ensemble families. Their availability does not make one automatically preferable: compare them with a simple baseline, inspect error consequences and consider whether the result can be validated for the intended machines.

## Check your understanding

Explain one difference between a random forest and boosting.

ANSWER: A random forest aggregates randomized trees constructed in parallel, whereas boosting adds models sequentially to reduce remaining objective errors.

Does a tree split involving vibration establish a manufacturer-approved fault limit?

ANSWER: No. It is a learned prediction rule. Its use requires validation on relevant machines and regimes, and its numerical boundary must not be read as a manufacturer specification.

## Key takeaways

- Decision trees partition inputs with feature tests and produce piecewise predictions.
- Random forests aggregate randomized parallel trees; boosting adds sequential error-correcting stages.
- Learned thresholds support prediction but do not establish causal or manufacturer limits.
- Validate on the relevant machines and operating regimes; synthetic examples are insufficient for operational hardware.

Pause and explain: Explain one difference between a random forest and boosting.

### Grouping, compression and fair selection

## What you are expected to learn

You will describe k-means and principal component analysis, explain the effect of feature scaling, and apply a fair protocol for comparing candidate models.

## Unsupervised grouping and compression

k-means groups unlabelled data points around selected mathematical centres by minimizing a within-cluster distance objective [48]. The number of clusters is a user-selected algorithmic setting. A cluster count does not prove the number of physical faults or guarantee distinct physical fault classes; engineering interpretation and independent evidence are still required.

The engineering example groups unlabelled mechanical operating profiles. A centre represents the mathematical reference for a group in feature space. The distance objective describes the grouping criterion; it supplies no fault diagnosis by itself. Choosing a cluster count tells the algorithm how many groups to form, while identifying what those groups mean physically remains a separate interpretation task.

The number of k-means clusters must be chosen. One exploratory aid is to compare within-cluster variation across several candidate values of k and look for a point where further increases give diminishing improvement. This elbow method is not guaranteed to be clear or objectively correct. Check cluster stability and physical meaning; do not interpret k as a known number of machine states or faults.

Principal component analysis, or PCA, projects data vectors onto directions of high mathematical variance [49]. It can compress correlated sensor feature inputs and ranks principal components by captured variance. High variance is not necessarily task relevance: normal ambient-load variation may dominate, while a rare mechanical fault may occupy a low-variance direction. PCA does not filter components according to actual fault relevance.

A projection represents the data along selected directions, and the resulting representations are principal components. In the source diagram, the broad distribution associated with normal ambient load shows the direction of greatest variation, while the rare-fault example illustrates a different direction. The distinction concerns the criterion: capturing variation and identifying diagnostically useful information are different questions. The illustration does not establish that every rare fault follows the same geometric pattern.

## Feature scaling implications

Distance-based methods require scaling that respects physical units. An unscaled large-magnitude variable can dominate geometric distance calculations, making a smaller but task-relevant vibration feature mathematically negligible. Changing feature units can alter distances without changing the physical system. Select preprocessing that matches the physical task and record the units used.

## Fair candidate comparison

Compare candidate methods on common development data [50]. Fit preprocessing transformations strictly inside each training fold, including scalers and other learned transformations. Use validation folds for hyperparameter tuning and candidate selection. After the choice is fixed, evaluate it once on an isolated locked test set.

Read the validation diagram as a sequence of information boundaries:

- Common development data supply the candidate comparisons.
- Training folds contain the examples used to fit each model and its preprocessing.
- Validation folds provide performance evidence for tuning and choosing candidates.
- The locked final test evaluates the selected choice after development decisions are fixed.

A fold is a subset used within this development procedure. A hyperparameter is a setting selected during tuning. Preprocessing isolation means that the transformations are fitted using the training part of each comparison, rather than using the validation or final-test examples to determine them.

The same boundary must apply to every candidate. A candidate that receives preprocessing fitted using validation or test information has an unfair information advantage. Report the split, transformations, selection rule and locked-test result so that the comparison is repeatable.

## Interpretability, cost and limits

Candidate selection includes the required output, the data structure, performance evidence and operational cost. A complex architecture must demonstrate performance gains that justify added maintenance and operational burden. Algorithmic variance, cluster structure or a learned boundary does not by itself establish a mechanical fault or an approved operating limit. Use validation and physical evidence before making such claims.

Common implementation names include KMeans for clustering and PCA for principal component analysis. These tools can expose structure or support visualization, but clusters and components are mathematical summaries. They do not establish that a group is a real fault state or that a compressed feature has engineering meaning.

## Check your understanding

Could the direction of greatest variance be unrelated to a rare fault? Explain.

ANSWER: Yes. PCA maximizes mathematical variance, while a rare fault can occupy a low-variance direction and therefore may not align with the principal component of greatest variance.

Does choosing a cluster count establish the number of mechanical fault types?

ANSWER: No. The count is an algorithmic setting. Mathematical grouping still requires engineering interpretation and does not guarantee distinct physical fault classes.

Where should preprocessing be fitted when comparing candidates across folds?

ANSWER: Inside each training fold. Validation supports tuning and selection; an isolated locked test evaluates the final choice.

## Key takeaways

- k-means minimizes within-cluster distance; its cluster count is a selected setting, not a proven fault count.
- PCA captures high-variance directions, which may not be task-relevant.
- Isolate preprocessing inside training folds, tune on validation data and lock the final test.
- Justify complexity with task-relevant validation evidence and operational cost.

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

## What you are expected to learn

You will distinguish training, validation and final-test data, explain cross-validation, and choose an evaluation boundary that matches the intended engineering use. The central question is whether the evaluation uses examples that are appropriately separate from model development.

## 1. Generalization means performance on relevant unseen examples

Generalization concerns performance on examples outside the data used to develop the model. In an engineering application, unseen must be defined in relation to the deployment question. Predicting later observations and transferring to a machine absent from development are different questions. They require different evaluation boundaries.

Read the development-data and unseen-machine diagram in the slides as a separation between model development and assessment. The held-out examples provide evidence about the stated use only when the development procedure has respected that separation. A large number of rows does not establish that the examples are independent or relevant to deployment.

## 2. Three datasets have different functions

The training set supplies examples for fitting model parameters, such as regression coefficients. Fitting changes the model using those examples. This is the training set's role in the data-split table.

The validation set supports development choices. These include selecting a model family, choosing tree depth, or setting an alert threshold. Validation therefore influences the chosen procedure, even though it is separate from fitting that procedure's parameters. Distinguish parameter fitting from deciding which model and settings to retain.

The final test set evaluates the model after development choices are fixed. It provides a performance estimate for the locked procedure. If the procedure is repeatedly changed in response to test results, those results have influenced development. The test set then functions as development data rather than an independent final assessment.

The distinction is about how information is used. Calling a file a test set does not protect it if its results guide further tuning. The model, preprocessing and development choices must be fixed before the final evaluation.

## 3. Cross-validation stays inside development data

Cross-validation repeats training and validation over different folds within the development dataset [38]. In each iteration, a portion is held out for validation and the remaining portion is used for training. The repeated assessments support development choices; they do not replace the role of a reserved final test set.

The slides give a mathematical example with 100 independent examples divided equally into five folds. Each fold contains 20 examples. In one iteration, 80 examples are used for training and 20 are held out for validation. These are counts of examples, not dimensional quantities requiring SI units. The example explicitly assumes independence and equal fold sizes.

Learned preprocessing must be fitted separately within each iteration's training fold. For example, a scaler or imputer obtains its fitted values from that training portion. The validation portion is transformed using those fitted values. Fitting preprocessing on all development examples before forming the folds allows each held-out portion to influence its own assessment.

For classification folds where examples are otherwise exchangeable, stratification can preserve approximate class proportions in each fold. It does not replace machine- or event-level grouping, chronological ordering, or other boundaries required by the deployment question. Choose the split design first; then preserve class balance within those valid boundaries where feasible.

## 4. Match the split to the deployment question

There is no universal split rule for every engineering dataset [51]. The slides distinguish three situations:

- Forecasting requires splits that respect chronological order.
- Transfer to new equipment requires holding out whole machines when the question concerns machines absent from development.
- Independent experimental designs may justify randomized row splits.

Use the intended engineering question to select the boundary. Randomly splitting rows from every machine into both training and test sets does not test transfer to entirely unseen machines: those machines are already represented in development.

## 5. Overlapping windows can compromise separation

Vibration data may be represented as measurement windows. If overlapping windows from the same event occur in both training and test sets, the sets share event information. The apparent performance can be optimistic because the assessment does not represent the intended independent evidence.

The slides illustrate this issue with 5,000 overlapping windows from ten machines and a goal of transfer to unseen equipment. Random row splitting distributes each machine's windows across both sets. The corrected arrangement holds out whole machines, keeps related overlapping events within consistent boundaries, fits preprocessing on the training portion, and locks the procedure before evaluating the held-out equipment. The numbers describe a teaching example, not a required dataset size.

For exchangeable classification examples, scikit-learn provides train_test_split and StratifiedKFold as common split tools. These do not replace time-ordered or group-based holdouts when examples from the same machine, event or future period must stay together. Choose the evaluation boundary for the deployment question before selecting an API.

## Check your understanding

Which split would assess transfer to a machine never used in development?

ANSWER: Hold out whole machines from development and evaluate the locked procedure on those machines. Mixing each machine's rows across development and test sets would assess a different question.

In the five-fold example, why does each iteration use 80 training examples?

ANSWER: The 100 independent examples are divided into five equal groups of 20. One group is held out for validation and the remaining four groups provide 80 training examples.

## Key takeaways

- Training fits parameters; validation guides development choices; final testing evaluates the locked procedure.
- Cross-validation and learned preprocessing remain within the appropriate development and training-fold boundaries.
- Define unseen examples through the intended deployment question.
- Row counts do not establish independence; machine and event overlap require attention.

Pause and explain: Which split would test transfer to a machine never used in training?

### Underfitting, overfitting and regularization

## What you are expected to learn

You will distinguish underfitting from overfitting, interpret training and validation errors, and explain regularization and early stopping. You will also identify why poor performance requires checking the data and features before changing model complexity.

## 1. Underfitting misses relevant relationships

Underfitting means that the model does not adequately represent or learn the relationship needed for the task. The slide diagram shows a straight-line fit applied to a strongly nonlinear response. The line cannot represent the response shown, so increasing confidence in that line would not correct the representation.

High training and validation errors, relative to a useful baseline and with sufficiently reliable data, can suggest underfitting. Possible issues include insufficient model capacity, weak features or inadequate training. Read the diagram as an illustration of a model missing a relationship; the plotted markers do not supply a measured equipment response or a fitted physical equation.

## 2. High error has other possible causes

High error on both datasets does not, by itself, prove that the model is too simple. The resources also identify measurement noise, incorrect target labels and missing input features. These issues can limit prediction even when model complexity increases.

The diagnostic flowchart begins with high training and validation error, then asks whether the data and baseline have been checked. Investigate target quality, available features and noise before treating complexity as the sole explanation. If the supplied inputs omit relevant information, a more flexible model still receives those same incomplete inputs.

The practical distinction is between inadequate representation and inadequate evidence. Both can produce poor results, but the appropriate investigation differs. Compare errors with a meaningful baseline and inspect the data used to calculate them.

## 3. Overfitting captures training-specific variation

Overfitting occurs when a learned relationship captures variation specific to the training examples and performs poorly on relevant unseen examples [4]. In the slides, an irregular fitted curve follows incidental noise rather than representing a relationship that transfers. Deep decision trees are given as an example of models whose complexity can increase this risk.

A common diagnostic pattern is training error substantially below validation error. The training examples are fitted closely, but the improvement does not carry over to the validation examples. Some difference between the two errors is normal, so the lesson does not prescribe a universal numerical gap that proves overfitting.

Read training and validation results together. High error on both calls for investigation of the relationship, data and baseline. Low training error with substantially poorer validation performance calls for investigation of training-specific fitting. The terms underfitting and overfitting describe learning behaviour, rather than conclusions obtained from a single score.

## 4. Regularization controls certain complex fits

Regularization discourages selected kinds of complex fitting through penalties or constraints. The supplied example is a penalty on large fitted coefficients. The slides also discuss structural constraints on model complexity. These controls change which fitted relationships the training procedure favours.

The purpose is to reduce excessive fitting to training-specific variation and improve generalization. Restricting a model too strongly can also leave it unable to represent relevant relationships. The resources therefore discuss reducing variance without introducing excessive bias. Here, bias and variance concern prediction error; they are distinct from the ethical meaning of fairness bias.

The regularization block diagram is schematic. It identifies a control on fitting, but supplies no penalty equation, coefficient value or universally recommended setting. Assess development choices using validation evidence.

## Relate complexity to bias and variance

Increasing model flexibility can reduce systematic errors from an overly simple fit, but can also make the fitted model more sensitive to the particular training examples [52]. This is the bias-variance trade-off. Use validation evidence to choose complexity; do not assume that lower training error means better performance on relevant unseen data.

## 5. Early stopping uses validation performance

Early stopping selects a training checkpoint using validation performance [53]. The slides show training progressing through epochs and a checkpoint being selected along that progression. The key distinction is between continuing to improve the training fit and retaining a model that performs well on validation examples.

In the loss-versus-epochs diagram, training loss continues to decrease while validation loss decreases and then increases. Lower training loss alone would favour continuing. Validation behaviour indicates that further training is no longer improving the chosen validation measure, so a checkpoint is selected within development.

The plotted minimum illustrates checkpoint selection; it does not guarantee optimal performance on every future example. The resources provide no numerical patience setting or stopping tolerance. The final-test score must not select the epoch, because doing so would use the final test for development.

L1 regularization penalizes the absolute sizes of selected model coefficients and can drive some coefficients to zero [54]. This can produce a sparse linear model, but a zero coefficient does not prove that a sensor is physically irrelevant: correlated inputs, scaling and the training sample can affect which coefficient remains. Fit and compare such choices within the development data.

In scikit-learn, Lasso is a common regression estimator using L1 regularization. As with any API, check its current documentation and fit it only within the development data; its selected coefficients are not proof of physical relevance.

## Check your understanding

Why does high error on both training and validation sets not always prove underfitting?

ANSWER: Noise, incorrect labels and missing features can also produce high errors. Investigate the data and compare with a useful baseline before concluding that model capacity is insufficient.

Why should an early-stopping checkpoint be chosen using validation rather than final-test results?

ANSWER: Checkpoint selection is a development choice. Using final-test results for that choice would compromise the independent evaluation of the locked procedure.

## Key takeaways

- Underfitting misses relevant relationships; overfitting captures training-specific variation.
- Interpret training and validation errors together with data quality and baseline evidence.
- Regularization controls selected kinds of complex fitting through penalties or constraints.
- Early stopping selects a checkpoint within development; final testing remains separate.

Pause and explain: Why does high error on both sets not always prove underfitting?

### Leakage is information crossing the wrong boundary

## What you are expected to learn

You will identify preprocessing, temporal, target-derived and duplicate-event leakage. You will explain how training-fold pipelines protect evaluation and which records are needed to reproduce the procedure actually performed.

## 1. Leakage violates an information boundary

Data leakage occurs when information unavailable for the intended prediction or reserved for evaluation improperly influences training or selection [25], [55]. The boundary can concern datasets, machines, events or prediction time. A credible assessment must respect the boundary required by the engineering question.

The slides' boundary diagram shows evaluation information influencing development. This compromises the assessment because the procedure has benefited from evidence that was supposed to remain separate. Leakage is therefore about the information used and when it becomes available, rather than only the filenames assigned to datasets.

## 2. Preprocessing can leak without using target labels

Consider fitting a scaler on all data before dividing the examples for cross-validation. Each held-out fold has already influenced the scaler's fitted values. Although its examples are subsequently labelled as validation data, their information has entered the preprocessing used during training.

The same issue applies to an imputer fitted using combined training and evaluation data. Learned preprocessing is part of the procedure being assessed. Evaluating a globally fitted transformation does not assess the intended procedure that would learn its transformation from training data alone.

Read the two preprocessing diagrams in order. The incorrect sequence fits a global transformation and then forms the evaluation folds. The correct sequence forms the folds first, fits the transformation on the training fold, and applies those fitted values to the evaluation portion.

## 3. A pipeline must preserve fitting boundaries

A pipeline groups feature transformations and model processing into a repeatable sequence. In this lesson, its purpose is to keep learned transformations inside the appropriate training boundary. The scaler or imputer is fitted on the training portion and its stored parameters are used to transform evaluation examples.

During cross-validation, repeat this fitting separately within each training fold. Calling a sequence a pipeline is insufficient if it is fitted on all examples before evaluation. The important evidence is which examples contributed to each fitted transformation.

The infographic shows training folds passing through feature transformations and fitted pipelines before application to training and evaluation data. Interpret the evaluation branch as applying the training-fitted parameters, not refitting them on held-out examples.

## 4. Future observations can leak through time windows

At prediction time t, a live alarm must use information available at that time. A centered moving-average feature can combine readings from t−1, t and t+1. The reading at t+1 occurs after the intended prediction and is unavailable when the alarm must operate.

The source timeline uses these symbols to indicate observation order. It does not specify a sampling interval or numerical time unit. The problem is the inclusion of future information, regardless of the unspecified interval.

A chronological dataset split alone does not repair that feature. Even if training rows precede evaluation rows, a feature for an earlier prediction can still contain a later observation. Check feature construction as well as dataset order.

## 5. Target-derived and duplicate-event information also matter

A post-failure repair code is an example of information that becomes available after the event a warning system is intended to predict. Using that code as a pre-failure input gives the model information it would not have when making the intended prediction. The input can encode the outcome instead of providing valid earlier evidence.

Duplicate events across development and evaluation sets create another route. The two sets share event information, so evaluation no longer supplies the intended separate evidence. Check event identity and measurement-window overlap, in addition to checking individual row assignments.

These routes require different inspections: preprocessing leakage concerns fitting data; temporal leakage concerns availability at prediction time; target-derived leakage concerns outcome information; duplicate-event leakage concerns separation of related examples.

A result that is unexpectedly strong, or that changes sharply after adding one feature, is a reason to audit the information boundary, not proof that leakage occurred. Trace each feature to its source and ask whether it would exist at prediction time. Target-derived transformations such as target encoding must also be learned only within the relevant training fold.

After deployment, changing machines, sensors or operating regimes can shift the data and degrade performance without any train-test leakage [56]. Module 15 discusses distribution shift and drift; monitor inputs and outcomes and define when to investigate, defer or retrain.

## 6. Final testing follows completed development

Complete development, fix the procedure, and then evaluate the reserved final test. Report the procedure actually executed. If final-test results guide further changes, disclose that reuse and the resulting limitation; obtain new independent evidence where possible.

The single-evaluation sequence protects the test from repeated development decisions. It does not make an otherwise flawed split or leaking feature valid. Honest reporting includes the split, transformations and any departure from the intended assessment.

## 7. Record enough detail to reproduce the result

The resources specify split identifiers, transformation sequences, random seeds, code versions and software dependencies. Split identifiers record which examples belonged to each portion. Transformation records identify the processing sequence. Seeds record the random initialization or selection used. Code and dependency versions identify the implementation and environment.

These records allow the stated procedure to be repeated and inspected [35]. Reproducing a score does not, by itself, prove that the procedure respected its information boundary. Reproducibility and leakage prevention are complementary requirements.

## Check your understanding

Why might a centered moving-average feature leak in a real-time alarm?

ANSWER: It can include a reading after the alarm's prediction time. That information is unavailable when the alarm is intended to operate, even if the dataset was split chronologically.

Why must a scaler be fitted again inside each cross-validation training fold?

ANSWER: Each iteration has a different held-out portion. Fitting only on that iteration's training examples prevents the held-out portion from influencing the learned transformation.

## Key takeaways

- Inspect both dataset separation and information availability at prediction time.
- Fit learned preprocessing inside training folds and apply its stored parameters to evaluation examples.
- Exclude unavailable future and outcome-derived information from predictive inputs.
- Disclose final-test reuse and document the procedure sufficiently for reproduction.

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

## What you are expected to learn

You will explain the roles of inputs, weights, a bias term and an activation in a neuron. You will calculate a ReLU output and explain why a network needs nonlinear operations between layers to represent more than a single affine mapping.

## 1. Follow the computation through a neuron

An artificial neuron is a mathematical computation [4]. It receives numerical inputs, multiplies each input by a corresponding weight, adds the weighted contributions and a bias, and applies an activation function. The supplied block diagram represents these operations in their calculation order.

The weighted sum is z = Σᵢ wᵢxᵢ + b. Here, xᵢ is input i, wᵢ is its weight, b is the bias term, and z is the value before activation. The summation symbol means to add the weighted contributions from the inputs. The activated output is a = f(z), where f is the chosen activation function.

For two inputs, read the same calculation as z = w₁x₁ + w₂x₂ + b. First calculate the two products, then add them and the bias. Applying the activation is a further operation. Keeping these stages separate makes the numerical example easier to check.

The supplied examples treat the inputs, weights, bias, weighted sum and activated output as dimensionless quantities. Their numbers do not represent a measured equipment response or establish performance in a physical application.

## 2. Distinguish fitted parameters from structure

A weight is a learned multiplier that scales an input's contribution. The bias term is an additive parameter that shifts the weighted sum. In this context, bias names that additive term; it has a different meaning from statistical bias or fairness bias.

Weights, bias terms and fitted connection coefficients are learned parameters. A neuron and a layer describe the computational structure: a neuron performs a computation, while a layer is a collection or stage of neural computations. A network combines layers into a mapping from inputs to outputs.

The slides' parameter-versus-structure table separates what training adjusts from how the computation is arranged. Identifying a weight is therefore different from identifying a layer. The later discussion of learning rate adds another distinction: a chosen training setting is not a fitted weight.

## Why identical zero weights are a problem

If identical neurons in a layer start with identical weights, they receive the same inputs and can compute the same outputs and gradients. They then have no reason to learn different features. Common neural-network initializers use small, varied values to break this symmetry. Initialization is a training choice; it does not guarantee that the resulting network will learn a useful representation.

## 3. Apply the ReLU activation

The Rectified Linear Unit, ReLU, is defined by a = max(0, z) [57]. Compare z with zero and select the larger value. Negative values produce zero, positive values pass through unchanged, and z = 0 produces zero.

In the ReLU graph, the output stays on zero for negative z. To the right of zero, the output equals z. This piecewise behaviour introduces nonlinearity into the computation. The graph shows exact values of the activation function, rather than the measured results of training a network.

The infographic gives three examples: z = −3 produces a = 0, z = 0.2 produces a = 0.2, and z = 2 produces a = 2. Each value is dimensionless. Check which branch of the rule applies before performing further calculations.

## 4. Work through the supplied forward calculation

Use x₁ = 2, x₂ = 1, w₁ = 0.5, w₂ = −1 and b = 0.2. All values in this teaching example are dimensionless.

- First contribution: w₁x₁ = 0.5 × 2 = 1.
- Second contribution: w₂x₂ = −1 × 1 = −1.
- Add the contributions and bias: z = 1 + (−1) + 0.2 = 0.2.
- Apply the activation: a = max(0, 0.2) = 0.2.

The two weighted input contributions cancel in this example, leaving the bias as the weighted-sum value. Because that value is positive, ReLU leaves it unchanged. This is a forward computation using the stated parameters; it does not calculate a gradient or change a weight.

## 5. Explain why nonlinear operations matter between layers

Combining several affine transformations without nonlinear operations still produces an affine transformation [4]. The slides show three successive weight mappings as W₃(W₂(W₁x)), which can be written as one equivalent mapping. Including additive bias terms preserves the affine character of the composition.

Consequently, adding affine layers alone does not automatically create a useful nonlinear model. An activation such as ReLU between layers changes the mathematical mapping and prevents this simple collapse. Read the equivalent-layer diagram as a statement about the composition of operations, rather than a guarantee that any particular network will predict an engineering quantity accurately.

ReLU is not the only activation. Sigmoid maps values into the interval from 0 to 1 and is often used to produce a binary-classification output; tanh maps values into the interval from -1 to 1. These functions have different mathematical properties and uses. The course focuses on ReLU for its simple calculation, not because it is best for every layer or task.

## Check your understanding

What are the outputs of ReLU for z = −3 and z = 2?

ANSWER: The outputs are 0 and 2, respectively. ReLU selects the larger of zero and z. These values are dimensionless.

Why is calculating z = 0.2 in the worked example different from training the neuron?

ANSWER: The calculation uses specified inputs, weights and bias to produce an output. Training also requires an objective, gradient calculation and a parameter update. Those stages are developed in the next lesson.

## Key takeaways

- A neuron computes a weighted sum plus bias, then applies an activation.
- Weights and bias terms are fitted parameters; neurons and layers describe computational structure.
- ReLU maps negative values to zero and leaves positive values unchanged.
- Stacked affine layers remain affine unless nonlinear operations are introduced.

Pause and explain: Compute ReLU for z=−3 and z=2.

### Loss, gradients and updates

## What you are expected to learn

You will distinguish a loss from its gradient, explain the separate roles of backpropagation and an optimizer, and calculate the supplied gradient-descent update. You will also explain what the learning rate controls and what a single update cannot establish.

## 1. A loss specifies the training objective

Training needs a numerical objective against which model predictions can be assessed. A loss function, denoted L, measures discrepancy between predictions and the reference targets used for training. In the supplied pipeline diagram, model prediction and ground truth enter the loss calculation.

The reference target supplies the value against which the prediction is compared. Defining a loss identifies the objective being fitted. The resources do not specify a particular loss formula in this lesson, so the pipeline should be read as a general sequence rather than as an implementation of an unstated loss function.

For a numerical target, mean squared error is one possible loss: it averages squared differences between predictions and targets. For classification, cross-entropy losses are commonly used to compare predicted class probabilities with reference labels. The choice changes the training objective; a loss value is not itself an engineering acceptance criterion. Module 6 distinguishes training loss from evaluation and acceptance.

## 2. A gradient describes local change in the loss

A gradient collects derivatives of the loss with respect to model parameters. It describes how the loss changes locally as those parameters change. Write this collection as ∇L, with the derivatives taken with respect to the parameters being updated.

Keep the symbols distinct: L is the loss; ∇L is its gradient. Calculating the loss and calculating its derivatives are related stages, but they produce different information. The gradient is also distinct from the new parameter values that an optimizer will calculate.

In a network with multiple parameters, the derivatives concern their respective parameters. The worked example later in the lesson isolates one parameter and its gradient value so that the update arithmetic can be inspected directly.

## 3. Backpropagation computes derivatives through the network

Backpropagation uses the chain rule to compute loss derivatives efficiently through the layers [58]. Follow the derivative-computation block in the slides as a calculation through the existing network. Its result provides gradients for the update stage.

The distinction in the pipeline is functional: backpropagation calculates the gradients, and an optimizer uses them to change parameters. Treating both stages as one unexplained operation would hide which part computes derivatives and which part applies an update rule.

The complete sequence is to compute predictions, evaluate the loss, calculate gradients by backpropagation, and apply an optimizer update. A software interface may group these operations, but their mathematical roles remain separate.

## 4. Gradient descent applies a parameter update

The supplied gradient-descent rule is θ_new = θ_old − η∇L. Here, θ_old is the parameter value before the update, θ_new is the value afterward, η is the learning rate, and ∇L is the loss gradient for the parameter being updated. The infographic also writes g for the gradient in the same rule.

The learning rate scales the gradient contribution before it is subtracted from the old value. A large learning rate can overshoot, while a small learning rate can make progress slow. The effects depend on the problem; the lesson provides no universally recommended setting.

The learning rate is a training setting, whereas weights and bias terms are fitted parameters. In the supplied numerical example, the parameter, gradient and learning rate are treated as dimensionless. Keep that stated convention when checking the arithmetic.

## 5. Calculate the supplied numerical step

The example begins with θ_old = 2, gradient = 0.5 and η = 0.1. These values are supplied for an illustrative update; the example does not derive the gradient from a specified loss function.

- Calculate the adjustment: η∇L = 0.1 × 0.5 = 0.05.
- Subtract it from the old parameter: θ_new = 2 − 0.05 = 1.95.

The new parameter is 1.95, dimensionless. The example demonstrates how a provided gradient is used. It should not be read as evidence that backpropagation itself has applied the update, or that the gradient has been verified from a loss formula absent from the example.

## 6. Interpret the result within its limits

One correctly calculated update does not prove that a complete training run reaches a global optimum [4]. It also does not validate a physical machine or establish that the model respects engineering operating limits. Those conclusions require evidence beyond this isolated teaching calculation.

Keep the forward calculation from Lesson 1 separate from this update. The forward example produces an activated output of 0.2. The update example produces a parameter value of 1.95. They demonstrate different stages and are not presented as one fully specified training experiment.

## Check your understanding

Which stage computes gradients, and which stage changes the weights?

ANSWER: Backpropagation computes gradients using the chain rule. An optimizer uses the gradients to apply a parameter update.

Why is the change in the supplied parameter 0.05 rather than 0.5?

ANSWER: The learning rate scales the supplied gradient. The adjustment is 0.1 × 0.5 = 0.05, giving a new parameter of 2 − 0.05 = 1.95.

## Key takeaways

- Loss L defines the objective; gradient ∇L describes local change with respect to parameters.
- Backpropagation calculates gradients; the optimizer applies an update rule.
- The learning rate controls update scale and is a training setting.
- A single update establishes neither global convergence nor physical equipment validation.

Pause and explain: Which operation computes gradients, and which operation uses them to change weights?

### Batches, epochs and realistic expectations

## What you are expected to learn

You will distinguish a batch, an update and an epoch; calculate the number of updates in the supplied example; and explain why more training does not guarantee better performance on unseen data. You will connect validation-based checkpoint selection with a separate final test.

## 1. A batch supplies examples for an update

A batch is a group of training examples used for a parameter update in a typical mini-batch procedure [4]. Read the batch diagram as selecting a subset from the training dataset for the computation that leads to one update.

The calculation still involves the stages introduced in Lesson 2: predictions, loss, gradients and a parameter update. Batch size states how many examples are processed together for that update. It is a count of examples, rather than a physical quantity with an SI unit.

The batch diagram therefore connects dataset organization with training operations. A batch is a group of examples; an update is the operation that changes parameters using the calculated gradient information.

## 2. An epoch is a complete pass through training data

An epoch is one pass through the training set. In the supplied diagram, the complete dataset pass contains the batches used along that pass. One epoch can therefore contain several parameter updates.

Distinguish the two counts. Counting epochs tells you how many complete training-data passes have occurred. Counting updates tells you how often parameters have been adjusted. These counts answer different questions even though both describe progress through training.

The resource illustration identifies a batch as a subset and an epoch as the full pass. It does not imply that each batch is a new independent dataset or that completing an epoch demonstrates improved unseen performance.

## 3. Calculate updates per epoch

The teaching example has 1,000 training examples and a batch size of 50. For the stated standard pass, divide the number of examples by the number in each batch:

Updates per epoch = 1,000 ÷ 50 = 20.

The slides write this as U = N_total / N_batch, where U is the number of updates, N_total is the total number of training examples, and N_batch is the number of examples per batch. All are counts, with no physical units. Here the division is exact, so the pass contains 20 batches and 20 updates.

The exact-divisibility condition matters. If a dataset does not divide evenly into batches, the treatment of the final partial batch must be stated. The supplied example does not require such a choice and does not prescribe one for every training procedure.

## 4. More epochs can improve training fit without improving generalization

Deep networks can learn representations useful for complex data, but require appropriate data, computation and validation [3]. Training duration alone does not establish whether those representations perform well on relevant unseen examples.

The training-loss diagram shows loss decreasing as training continues. The validation-loss diagram shows an initial decrease followed by an increase. Together, they illustrate how an improving training fit can occur alongside worsening validation performance.

Additional epochs can fit training-specific variation. Consequently, a lower training loss or a larger epoch count does not guarantee improved test performance. The curves illustrate this distinction; they do not report measured machinery performance, specify a numerical stopping epoch, or guarantee the same curve shape for every run.

## 5. Use validation to select a checkpoint

A checkpoint records a model state during training [53]. The supplied selection diagram connects monitoring validation performance with choosing the model state to retain. Checkpoint selection is part of development because it determines which trained model will be used.

Use the validation evidence to guide that choice rather than assuming that the last epoch is best. A validation minimum is evidence for a development choice; it is not a guarantee of the best result on every future observation. The resources supply no numerical stopping tolerance or patience setting to apply universally.

After model selection is complete, the locked final test estimates performance on its held-out examples. Final-test results should remain separate from checkpoint selection. Choosing an epoch using those results would allow the final test to influence development.

## 6. Keep expectations aligned with this introductory module

The beginner goal is to understand neural computations and training vocabulary. No GPU is required for this course. Full architecture design, automatic differentiation software and large-scale model training are identified as later study.

The arithmetic and diagrams support understanding of computation, updates and evaluation. Synthetic numerical examples do not substitute for physical equipment validation. Completing more epochs does not establish that engineering constraints are satisfied.

Batch size changes how many examples contribute to each parameter update. A larger batch usually gives a less noisy estimate of the training gradient and makes fewer updates per epoch; a smaller batch gives noisier updates and more updates per epoch. The effect on speed and generalization depends on the model, data and optimizer, so treat batch size as a setting to evaluate rather than a guaranteed improvement.

## Check your understanding

How many updates occur in one standard epoch with 1,000 examples and batches of 50?

ANSWER: There are 20 updates, because 1,000 ÷ 50 = 20. The example assumes an exact division into full batches.

Would 100 additional epochs guarantee better test performance?

ANSWER: No. Extra training can fit training-specific variation. Validation guides checkpoint selection, and a locked final test estimates performance afterward.

## Key takeaways

- A batch supplies examples for an update; an epoch is one complete training-data pass.
- Updates per epoch depend on dataset size, batch size and any stated partial-batch treatment.
- More epochs do not guarantee better generalization.
- Select checkpoints using validation evidence, then assess the selected model with the locked final test.

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

## What you are expected to learn

This lesson explains why data representation should be defined before selecting a neural-network architecture. You are expected to distinguish tabular features, image pixels and channels, and time-indexed signals; relate feature vectors to multilayer perceptrons and local spatial patterns to convolutional networks; and design an evaluation split that answers a new-component inspection question.

## 1. Represent the data structure explicitly

Tabular data describe each example through named feature values. An image is represented numerically through pixels and channels. A signal is a sequence of measured values with timestamps, sampling information and physical units. Converting any of these forms into a numerical array is a representation step; it does not establish that a model understands the engineering meaning of the values.

Before training, document the feature definitions, units, sampling or image-acquisition conditions, target, and the information available at the intended decision time. The representation must preserve the structure relevant to the engineering question.

## 2. Match representation to architecture

A multilayer perceptron, or MLP, commonly processes a feature vector through fully connected layers. A convolutional neural network, or CNN, applies shared filters over local regions and can represent local spatial patterns in images or some signals. A filter response is a numerical pattern response; it is not by itself evidence that a crack or other physical defect has been identified. Labels, inspection evidence and suitable validation are still required.

Architecture selection therefore follows the data structure and the required output. The supplied comparison maps tabular feature vectors to an MLP and image pixels and channels to a CNN. This mapping is a starting design choice, not a guarantee of performance.

A convolution applies the same learned filter to local image neighborhoods and combines nearby pixel values into a feature map [59]. Reusing the filter across locations can help a CNN detect spatial patterns such as edges or texture. A filter response is a numerical feature, not proof that a crack or defect is present; inspection labels and validation remain necessary.

## 3. Prevent identity leakage in image evaluation

Randomly splitting images can overestimate performance when several views of the same component appear in both training and testing data [55]. Shared surface patterns, lighting, acquisition settings or component identity can allow the model to recognise the component rather than generalise to an unseen component.

If the intended use is inspection of new hardware, hold out complete components or appropriate batches. Keep the test components unseen during development. Annotation quality, lighting and camera changes must also be considered when interpreting results.

A mechanical image task might use a camera image to flag a suspected weld crack or a thermogram to identify an unusual hot region for inspection. The model output is a candidate finding, not a confirmed defect: image conditions, labels and the inspection procedure still need validation.

## Check your understanding

Why can random image splitting overstate performance on new components? Images from one component can share patterns and lighting across splits. A component-level holdout better represents the stated new-component question.

## Key takeaways

- Represent tabular data as feature vectors, images as pixels and channels, and signals as timed values with units.
- Use an MLP for feature vectors and a CNN when local spatial patterns are relevant.
- A numerical filter response does not by itself prove a physical defect.
- Match the evaluation split to deployment; hold out whole components for new-component inspection.

Pause and explain: Why might random image splitting overstate performance on new components?

### Sequence architectures are different mechanisms

## What you are expected to learn

This lesson compares recurrent and attention-based sequence mechanisms and defines the information boundary for operational forecasting. You are expected to distinguish hidden-state recurrence from attention across positions, explain why attention is not proof of causal importance, and separate information available at forecast issue time from future measured data.

## 1. Recurrent sequence mechanisms

A recurrent neural network, or RNN, carries a hidden state from one sequence step to the next [4]. The state provides a mechanism for retaining information from earlier observations while processing later observations. An LSTM is a recurrent architecture with mechanisms for retaining and updating information over sequence steps. These descriptions concern information handling; they do not establish a particular engineering accuracy.

A simplified RNN update can be written as `h_t = f(W_x x_t + W_h h_(t-1) + b)`. Here, `x_t` is the current input, `h_(t-1)` is the previous hidden state, and `h_t` is the updated state. The equation illustrates how earlier information can be carried forward; it is not a guarantee that the network will retain every useful detail over a long sequence.

## 2. Attention and transformers

A transformer uses attention to weight and combine representations across sequence positions without carrying a recurrent hidden state in the same manner [60]. When order matters, the sequence requires a suitable positional representation. Attention weights describe how representations contribute to the model computation. They are not human attention and do not prove that a variable is a physical cause.

RNNs, LSTMs and transformers are different mechanisms [60], [61]. The appropriate choice depends on the data, constraints, available evidence and a fair baseline. A simple lagged-feature model can be a useful comparison before adopting a more complex architecture.

## 3. Define the forecast issue time

An operational forecast must specify when the prediction is issued and what target time or horizon it addresses [18]. Inputs must physically exist at the declared issue time. Observed load before issue may be available. A published weather forecast may be available if it was issued earlier, but its uncertainty must be recorded. Tomorrow's measured weather is unavailable at today's issue time and must not be used as an operational input. Using it evaluates a different information scenario.

Do not report performance using future measured inputs as though they were available during deployment. Distinguish operational forecasts from future measurements and state the information contract before evaluating the model.

## Inspect missing signal values before sequence modelling

Sensor dropout, communication loss and calibration work can create gaps in a signal. Inspect timestamps and missingness first, then choose a treatment that fits the sampling process and gap length. Forward fill or interpolation is not automatically safe, particularly across operating-state changes or long gaps. Follow the investigation and training-only preprocessing principles from Module 5, and record any imputation or excluded interval.

## Check your understanding

Recurrence carries a hidden state through steps. Attention combines representations across positions. Both require an appropriate representation of time or order, and neither mechanism alone establishes causation.

## Key takeaways

- RNNs and LSTMs carry sequential hidden states; transformers use attention across positions.
- Attention is a computational weighting mechanism, not proof of causal importance.
- Define issue time, target time and forecast horizon explicitly.
- Use only inputs available at issue time; future measured data cannot be operational inputs.

Pause and explain: Compare information passed through recurrence with information combined by attention.

### Windows and horizons

## What you are expected to learn

This lesson explains signal windowing, timestamp integrity and forecast horizons. You are expected to distinguish row positions from actual time, define sampling rate and window bounds, calculate when a row shift represents a time interval, and prevent temporal leakage from future or overlapping windows.

## 1. Use timestamps rather than filtered row positions

Signal features are often calculated over a specified window. Root-mean-square, or RMS, summarises signal magnitude over that window; spectral features summarise frequency content. Each feature requires documented window length, alignment and sampling rate.

For complete regular data sampled every 15 minutes, 96 samples correspond to 24 hours because 24 hours multiplied by 60 minutes per hour, divided by 15 minutes per sample, equals 96 samples. This relationship fails after rows are removed or intervals are missing. A filtered row index is not a clock. Use actual timestamps to align lagged features and targets, and record missing intervals and changes in sampling.

## 2. Define horizon and information availability

A forecast horizon is the time between the issue time and the target time [18]. At the issue time, features may use observations already available and forecasts that have already been issued. They must not use future measured readings or information generated after the decision. Draw an information-availability timeline before fitting a sequence predictor.

For a next-day load forecast issued at 18:00, observed load up to 18:00 may be available. A previously published weather forecast may be available, with its forecast uncertainty. Tomorrow's measured weather is not available and must be excluded.

## 3. Handle overlapping windows and temporal gaps

Adjacent windows can share many raw samples [51]. If windows are randomly assigned to training and testing sets, shared samples can destroy independence and produce optimistic performance. Use chronological splits, suitable temporal gaps, or event- or equipment-level holdouts when the evaluation question requires independent information.

State how missing intervals, changed sampling rates and incomplete windows are treated. The resource does not prescribe one universal imputation or split rule; the treatment must be justified for the task.

## Check your understanding

Does shifting 96 rows after deleting night-time rows still mean one day? No. After filtering, 96 rows may span several calendar days. Align by timestamps and the required time offset.

## Key takeaways

- Define sampling rate, window length, alignment, issue time and forecast horizon.
- Use timestamps rather than row positions after filtering or missing intervals.
- Exclude future readings and post-issue information from operational inputs.
- Use temporal gaps or other appropriate holdouts when overlapping windows threaten independence.

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

## What you are expected to learn

You are expected to explain what a language model produces, distinguish large language models, foundation models and multimodal models, and recognise diffusion models and generative adversarial networks. You are also expected to explain why generated text, code and concept drawings need independent engineering verification.

## 1. A language model produces sequences of tokens

A language model learns patterns over sequences of tokens and can generate or transform text [62]. A token is a unit processed by the model; Lesson 2 explains why it is not necessarily a complete word. An LLM is a large language model, typically with many parameters and broad training.

Read the language-model diagram as a sequence of computational operations: the model processes token patterns and produces a plausible continuation. That output can take the form of an explanation or source code. Producing a continuation does not, by itself, verify the statements in the explanation, execute the code, or consult an engineering standard.

Keep the output and the evidence for it separate. A fluent explanation shows that text has been produced coherently. Its equations, references and assumptions still need to be checked before they support an engineering conclusion.

## 2. Distinguish foundation and multimodal models

A foundation model is pretrained on broad data for reuse across downstream tasks [63]. A downstream task is a task addressed using that previously trained model, including through adaptation or prompting. Broad pretraining provides a basis for reuse; it does not establish accuracy for every engineering application.

A multimodal model processes or generates more than one information type, such as text and images. In the supplied diagram, text and image information enter a model that can work with those different forms. The term describes the kinds of information handled, rather than a guarantee that every detail has been interpreted correctly.

These names answer different questions. LLM identifies a large language model; foundation model describes broad pretraining and reuse; multimodal describes handling multiple information types. When reading the reference table, connect each capability with its evidence limit: task-specific evaluation remains necessary, and capabilities can vary by task.

## 3. Recognise other generative model families

Generative systems also include diffusion models and generative adversarial networks, or GANs [64], [65]. A diffusion model learns a reverse process from noised examples. The slides illustrate a progression from noised data toward a structured output. A GAN involves training a generator and a discriminator. These are different generative approaches.

At this stage, recognise the names and the broad mechanisms shown in the diagrams. Detailed mathematical derivations are outside the lesson. An image produced by either approach remains generated content; identifying the model family does not validate the dimensions or physical properties depicted.

## 4. Recognise the limits of generated explanations and drawings

A generated explanation may contain an incorrect mathematical equation, invent a reference, or omit an essential engineering assumption [66]. Polished wording does not resolve any of those problems. Check the actual equation, the existence and relevance of the cited source, and the assumptions required for the intended calculation.

A generated concept drawing can suggest an idea while failing dimensional, manufacturing or safety requirements. Its usefulness as an illustration is therefore a different question from whether it satisfies those requirements. The factual and dimensional constraints slide places these textual and visual failure routes alongside one another.

Generated text cannot substitute for consulting an applicable engineering standard. Likewise, an illustrative or synthetic result does not validate real equipment. The evidence must support the specific engineering claim being made.

## 5. Separate code generation, execution and checking

Generating source code creates text. Successful execution requires an execution tool, and a correct engineering result requires further checks. Follow the supplied sequence: generated source text, external execution, and independent testing of the assumptions and numerical result.

Do not treat the presence of a code block as evidence that it ran. Equally, execution alone does not establish that the code used the correct physical assumptions or produced the required numerical answer. The lesson's exercise asks about these distinct stages so that a generated program is assessed using evidence from execution and testing.

## Check your understanding

Does generating code mean that the code was executed successfully?

ANSWER: No. Generation produces source text. A tool must execute it, and independent tests must check the numerical result and assumptions. The source text alone supplies no execution evidence.

Why does calling a model multimodal not establish that a generated concept drawing is suitable for manufacture?

ANSWER: Multimodal describes the information types handled. A generated drawing may still fail dimensional, manufacturing or safety requirements; those require independent engineering checks.

## Key takeaways

- A language model learns token-sequence patterns and can generate or transform text.
- Foundation models support reuse after broad pretraining; multimodal models handle multiple information types.
- Diffusion models and GANs are other generative families whose detailed derivations are outside this lesson.
- Fluent explanations and concept drawings require checks of facts, assumptions and engineering requirements.
- Generated code must be executed and independently tested before its result can be assessed.

Pause and explain: Does generating code mean that the code was executed successfully?

### Tokens, context and embeddings

## What you are expected to learn

You are expected to distinguish tokens, context windows and embeddings; explain how context helps disambiguate a technical term; and identify the limits of long context and vector similarity. You are also expected to explain why these mechanisms do not remove the need to supply the intended system, units and assumptions.

## 1. Tokens are model-specific processing units

A token is an encoded unit processed by a model [67]. It may be a word fragment, punctuation or another encoded item. Tokenization is the process that converts input into those units, and its rules depend on the model.

The tokenization diagram separates the input string, the tokenizer and the resulting encoded units. A count of words describes the written text; an exact token count depends on how the particular model divides and encodes it. One word may produce several tokens.

Consequently, counting words does not provide an exact model-specific token count. This lesson does not imitate a particular provider's tokenizer or supply a universal conversion between words and tokens. Use the distinction to interpret a token limit without assuming that each word occupies exactly one token.

## 2. A context window bounds the information available

The context window is the finite content available within a model interaction. In the slide diagram, the boundary distinguishes information supplied within the interaction from information outside it. A technical datasheet that is omitted cannot be assumed to have been consulted.

A larger context window permits more content to be available, but does not guarantee perfect recall, correct use of every detail, or factual correctness [68]. There are two separate questions: was the relevant information supplied, and did the answer use it accurately? Increasing the available capacity does not answer the second question automatically.

Check that relevant technical material was actually used. A long response or a long input does not demonstrate that definitions, units and assumptions were handled correctly. The context-window comparison in the resources makes this limitation explicit.

## 3. Supply context to disambiguate technical terms

The source example is the word “cell”. It can refer to a photovoltaic cell, a battery cell or a spreadsheet cell. The same word therefore needs surrounding technical context before its intended meaning is clear.

State which system is being discussed and supply the relevant units and assumptions. Do not expect a model to infer missing operating assumptions correctly. Context helps identify the intended subject, but the supplied information still needs to be accurate and sufficient for the question.

Attention combines representations according to learned computations [60]. In the disambiguation diagram, the ambiguous term and explicit technical context are inputs to that computation. Read it as a computational mechanism for combining representations, rather than evidence that the model has independently established the correct physical interpretation.

## 4. An embedding represents an item as a numerical vector

An embedding is a numerical vector representation of an item [69]. The vector diagram shows an encoded item represented through numerical coordinates. This representation allows numerical comparison between items.

Keep the roles distinct. A token is a processed unit; the context window bounds the information available in an interaction; an embedding is a vector representation. These concepts describe different parts of the processing system, even though they can contribute to the same interaction.

The lesson introduces the role of a vector representation without requiring an embedding-training derivation, a particular vector size or a specific similarity formula. The coordinate illustration explains the form of the representation; it does not report measured engineering performance.

## 5. Similarity can retrieve a passage without proving a claim

Vector similarity can help locate related passages, such as passages in a manual. In the proximity diagram, numerical relatedness helps identify material to examine. Finding related material is useful, but it is a different operation from checking whether the passage actually supports an engineering claim.

Read the retrieved passage and verify the support it provides. Vector proximity alone does not establish factual correctness or validate a real-equipment safety specification. Likewise, having a relevant passage somewhere in a long context does not guarantee that the answer used it accurately.

The component comparison table therefore pairs each function with its limit: tokenization supplies encoded units, context bounds available information, embeddings provide numerical representations, and similarity assists retrieval. Independent verification of the resulting claim remains necessary.

## Check your understanding

Why is counting words not a reliable exact token count?

ANSWER: Tokens may be word fragments, punctuation or other encoded units, and tokenization depends on the model. A word count does not identify that model's exact token boundaries.

If a retrieved manual passage has a nearby embedding vector, has the engineering claim been verified?

ANSWER: No. The similarity indicates relatedness and helps retrieve material. The actual passage must be checked to determine whether it supports the claim. Long context also supplies no guarantee of correct use.

## Key takeaways

- Tokens are model-specific encoded units; exact token counts cannot be inferred from word counts.
- A context window limits available content, and greater capacity does not guarantee accurate use.
- State the intended technical system, units and assumptions to reduce ambiguity.
- Embeddings represent items numerically; similarity can help retrieve related passages.
- Relatedness and available context do not by themselves verify engineering claims.

Pause and explain: Why is counting words not a reliable exact token count?

### What changes weights and what does not

## What you are expected to learn

You are expected to distinguish pretraining, fine-tuning, transfer learning, prompting and retrieval. You are also expected to identify which operations update model weights, classify zero-shot and few-shot prompting, and explain why a computational distinction about weight updates does not establish a service provider's data-retention policy.

## 1. Pretraining learns parameters from broad data

Model weights are learned parameters used in the model's computation. Pretraining learns broadly useful patterns from a corpus, meaning a collection of data used for training. The supplied diagram shows broad data entering a training process that updates internal model weights before downstream use.

Pretraining is therefore a parameter-learning operation. When describing an assistant, distinguish the patterns learned during that training from the instructions or documents supplied during a later interaction. Both can influence the eventual output, but they do so through different mechanisms.

## 2. Fine-tuning updates parameters using additional examples

Fine-tuning uses additional training examples to update parameters for a task, domain or behaviour [29]. In the fine-tuning diagram, the additional task data are connected to a weight-update operation. This is why fine-tuning belongs in the parameter-changing category of the comparison table.

Transfer learning is the broader idea of reusing knowledge from earlier training for another task [70]. Fine-tuning is one form of transfer learning. Reusing a frozen feature extractor is another: the previously learned representation is used without updating that extractor's weights.

The distinction matters when reading the infographic. Reuse of earlier training does not always imply that the reused weights change. Identify whether the stated operation includes further parameter training or uses a frozen component.

## 3. Prompting supplies information during inference

Inference uses the existing model to produce an output. Prompting supplies instructions, context and possibly demonstration examples during that use. It does not by itself update the model's weights.

Zero-shot prompting supplies no demonstration examples [62]. Few-shot prompting includes some examples to guide the response. The difference concerns what is placed in the prompt, rather than whether training has occurred.

For the supplied lab-summary case, placing two example lab summaries in the prompt is few-shot prompting. Those summaries provide information for the current inference operation. Their presence does not turn that operation into fine-tuning: the source distinguishes examples supplied as context from examples used in parameter training.

## 4. Retrieval supplies source passages as context

Retrieval locates external material, such as a passage from an engineering manual, and supplies it within the model's context. The retrieval diagram shows the manual passage entering the context before the existing model produces an output.

In retrieval-augmented generation, or RAG, retrieved material is used to support generation [71]. Supplying that material does not inherently retrain the model. As with prompting, identify the provision of inference context separately from a weight-update operation.

First check that the source manual and its revision are correct, then evaluate the resulting answer. An answer can remain incorrect despite access to a relevant document. Retrieval provides material for the response; it does not establish that the material was selected or used correctly.

## 5. Classify the three adaptation actions

The worked case describes three actions: providing two example lab summaries in a prompt, retrieving a manual passage, and separately training on additional labelled examples. Classify each action by what it changes.

- The example lab summaries supply few-shot inference context. They do not by themselves update weights.
- The retrieved manual passage supplies source material in context. Retrieval does not inherently update weights.
- Fine-tuning on the additional labelled examples updates model parameters through training.

Each route still needs evaluation. Good examples, a relevant manual and changed weights can all be associated with incorrect engineering claims. Keep the mechanism and the quality of its result as separate questions.

## 6. Separate computational behaviour from data policy

The statement that prompting does not itself update weights describes the computation in that interaction. It does not establish what a service provider retains or whether separate training policies apply to submitted material.

Do not infer privacy from the weight-update distinction. The source explicitly identifies data-retention and training policies as separate matters. This lesson supplies no provider-specific policy claim; it explains how to distinguish inference context from parameter learning.

## Check your understanding

Which changes weights: fine-tuning, adding examples to a prompt, or retrieving a manual?

ANSWER: Fine-tuning updates weights through training. Adding examples to a prompt and retrieving a manual supply inference context without inherently updating the model's weights.

Can using a frozen feature extractor for another task count as transfer learning?

ANSWER: Yes. Transfer learning reuses knowledge from earlier training. It can use a frozen representation without updating that component's weights, as well as include fine-tuning that changes parameters.

Does an absence of weight updates during prompting prove that submitted data are not retained?

ANSWER: No. The computational operation and the provider's data-retention or separate training policy are different matters.

## Key takeaways

- Pretraining and fine-tuning learn or update model parameters.
- Transfer learning can include fine-tuning or reuse of a frozen feature extractor.
- Zero-shot prompting has no demonstrations; few-shot prompting includes some.
- Prompting and retrieval supply inference context without inherently retraining the model.
- Every route needs output evaluation, and weight-update behaviour does not determine data-retention policy.

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

## What you are expected to learn

You are expected to specify an engineering prompt with a task, audience, physical system, given values, units, assumptions and requested output. You are also expected to verify a simple photovoltaic calculation and distinguish instantaneous power from energy accumulated over time.

## 1. Structure an engineering prompt

Begin with the decision or calculation required. Name the intended audience and the physical system, then list every supplied value with its unit. State assumptions such as ignoring temperature effects or treating power as constant over a stated interval. Finally, define the output format: equations, units, intermediate steps, uncertainty or a table. Ask the assistant to separate supplied facts from assumptions and to identify missing information. A well-structured prompt makes checking easier; it does not make the response true.

## 2. Verify a photovoltaic power estimate

For the illustrative array, area A is 20 m², irradiance G is 800 W/m² and module efficiency eta is 0.20 [72]. The simplified direct-current power is P_DC = eta A G. Substitution gives 0.20 × 20 m² × 800 W/m² = 3,200 W, or 3.2 kW. If inverter efficiency eta_inv is 0.96, the simplified alternating-current estimate is P_AC = eta_inv P_DC = 0.96 × 3,200 W = 3,072 W, or 3.072 kW. Check the dimensions: m² multiplied by W/m² gives W, while efficiencies are dimensionless.

These values are an authored teaching case. They do not establish real equipment performance. A claim of 3,200 kW contains a factor-of-1,000 unit error. Fluency and correct engineering units are separate properties, so calculate independently.

## 3. Keep power and energy distinct

Power is an instantaneous rate in watts. Energy is the time integral of power and is commonly reported in kilowatt-hours. One irradiance or power observation cannot determine daily energy. A valid estimate requires a time profile, a stated duration and assumptions about variation and relevant losses. Under an explicitly illustrative constant-power assumption for two hours only, 3.072 kW × 2 h = 6.144 kWh. That calculation must not be presented as a daily yield without a justified time profile.

## 4. Zero-shot and few-shot prompts

Zero-shot prompting gives a task without demonstration examples [62]. Few-shot prompting includes examples of the desired input or output format. Examples can make the requested structure clearer, but they do not verify equations or supply missing physical evidence.

## Check your understanding

What is missing when one instantaneous power value is converted into daily energy? The answer is time information and relevant losses; use a time profile or a stated duration with valid constant-power assumptions. In the PV case, P_DC is 3,200 W and P_AC is 3,072 W.

## Key takeaways

- State task, system, values, units, assumptions and output format.
- Check equations and units independently of the assistant.
- Power is a rate; energy requires integration over time.
- Treat numerical examples as illustrative unless physical evidence supports them.

Pause and explain: What is missing if an assistant turns one instantaneous power value into daily energy?

### Retrieval supplies evidence at inference time

## What you are expected to learn

You are expected to explain retrieval-augmented generation and check whether a retrieved passage supports an engineering claim.

## 1. Retrieval-augmented generation

Retrieval-augmented generation, or RAG, searches a collection for material relevant to a query, appends selected passages to the model context and generates a response using that context [71]. Retrieval may use keywords, embeddings or both. The retrieved passage is supplied at inference time; RAG does not inherently update model parameters or retrain the model.

## 2. Treat retrieval as evidence that must be checked

For a maintenance question, an approved manual may contain an operating limit. Before relying on a retrieved passage, confirm that it exists, applies to the target equipment and part number, and belongs to the active revision. Then check that the actual wording supports the specific claim. A paragraph about a different inverter can look relevant while being invalid evidence for the target inverter.

Grounding connects a response to supplied evidence and can make review more direct. It does not eliminate misreading, irrelevant retrieval or unsupported generation. A citation label is not proof by itself. Open the original document and inspect the passage, units, scope and revision.

## 3. Engineering verification checkpoints

At the retrieve stage, check the equipment identity and source document. When context is added, check the document revision and passage alignment. During generation and review, open the original source and confirm that it directly supports the claim. Preserve the source location so another engineer can reproduce the check.

## 4. Vocabulary

Retrieval is searching for material relevant to a query. Grounding is connecting an output to relevant supplied evidence. RAG is retrieval followed by adding that evidence to model context for generation. These terms describe information flow; none guarantees that the answer is correct.

## Check your understanding

RAG does not inherently retrain model weights. For a retrieved operating limit, check the correct equipment, the correct revision and actual support for the claim. Confident wording alone is not evidence.

## Key takeaways

- Retrieval supplies context at inference time.
- Check equipment identity, document revision and direct claim support.
- Open original sources rather than trusting citation labels.
- Grounding reduces review risk but does not remove model error.

Pause and explain: What three checks should you make on a retrieved operating limit?

### Tools act; agents coordinate

## What you are expected to learn

You are expected to distinguish an assistant, tool, API and agent, and to separate code generation, execution and engineering verification.

## 1. Separate system components

An assistant is an interface that supports a user's task. A tool performs a defined operation, such as executing Python or searching a local document collection. An API is the software interface through which another program requests an operation. An agent system can select and coordinate actions across several steps toward a stated goal, with a defined degree of autonomy. A responsible person defines permissions, input limits and approval requirements and verifies the final engineering output.

## 2. Separate drafting, execution and correctness

Generated code is a draft [73]. Executing code is a separate operation, and execution without a software error is not proof of an engineering-correct result. Before a tool applies an action to a real system, check syntax and tests, equations and units, input limits, operating domain, permissions and logs. Independently verify numerical results and obtain approval from the responsible person for real-system actions.

## 3. The course prompt builder

The prompt builder in this course operates locally. It builds text for review and optional use elsewhere; it does not call an external language-model service, send course data or train a model. A local check can verify a supplied illustrative draft, but it cannot establish that a real machine, equation or operating decision is safe.

## 4. Vocabulary and boundaries

A tool carries out an operation. An API defines how software requests that operation. An assistant helps a user formulate or inspect work. An agent coordinates bounded actions across steps. These roles should be documented with permissions, limits, logs and an escalation path. More autonomy increases the need for explicit controls; it does not transfer engineering responsibility to the software.

## Check your understanding

An API is a defined software interface for requesting operations. Code that runs without errors still requires numerical, unit and physics checks. The course prompt builder builds text locally without a network call. For real-system action, verify the result independently and obtain responsible approval.

## Key takeaways

- Assistants, tools, APIs and agents have different roles.
- Keep code generation, execution and verification as separate stages.
- Successful execution does not prove engineering correctness.
- Define permissions, logs, operating limits and human approval before deployment.

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

Aleatoric uncertainty is variation in observations or unresolved processes, such as sensor measurement noise [74]. Repeating measurements may characterize this variation, but it cannot remove the underlying variability. Epistemic uncertainty comes from limited knowledge: sparse measurements in an operating regime, incomplete training examples or assumptions that may not represent the equipment. More informative observations can reduce some epistemic uncertainty. They cannot repair an inadequate model structure; a confidently estimated answer from a flawed model may still be wrong.

## Operating coverage is more than input bounds

Interpolation estimates within conditions represented by relevant observations. Extrapolation estimates beyond the covered operating domain, where behavior is less well supported. A point can fall between the minimum and maximum of each input and still be unrepresentative: combinations of inputs, plant configurations or operating regimes may be missing. Define the domain using the conditions relevant to the intended use, not just convenient rectangular limits, and evaluate performance on evidence from that domain.

## Calibration and confidence

Calibration checks whether stated probabilities agree with observed frequencies under defined conditions [12]. For example, among a sufficiently large set of comparable cases assigned about 80% probability, a calibrated model should be correct about 80% of the time. This is a group-level property, not a promise about an individual prediction and not an explanation of why the model made it. Assess calibration on independent data representative of the intended operating conditions. High model confidence is not proof of calibration, accuracy or permission to extrapolate.

## Distribution shift and drift

Distribution shift occurs when the deployment population differs from the development population, such as transferring a model from one plant type to another [21]. Drift describes gradual change in data or relationships over time, for example sensor ageing, wear or a changing control regime. A random seed only controls aspects of randomized computation; it cannot correct either kind of mismatch.

Monitor input ranges, missingness, output and alert patterns, and compare them with development conditions [56]. Input changes are warning signals, not proof by themselves that accuracy has degraded; check outcomes when trustworthy labels become available. Define action rules in advance: investigate, obtain new validation evidence, recalibrate where justified, retrain only with appropriate data, or defer predictions when conditions fall outside the validated domain.

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

Verification checks whether the intended equations, code or algorithm were implemented correctly [13]. Use known cases, dimensional analysis, bounds, limiting cases and sign conventions, and confirm that the workflow can be repeated. For a pump power model, the product of pressure drop and volumetric flow, delta-p x Q, has units Pa x m^3/s = W. A unit check and a test against a known calculation can catch implementation errors; they do not establish that the model represents a real pump.

## Validation: does it represent the real system?

Validation asks whether the model is adequate for its intended purpose on the physical system [13]. Compare predictions with appropriate independent, calibrated measurements across relevant operating conditions. A synthetic dataset or simulator can test whether code runs and the evaluation workflow behaves as expected, but agreement with synthetic data alone provides no physical validation of real hardware. Keep evidence used for final validation independent of fitting and model selection, and preserve the final test boundary until development decisions are complete.

## Provenance and reproducibility

Record how and when data were acquired, sensor and calibration context, units, transformations, split identifiers, code and environment versions, model settings, and material manual decisions [35], [37]. This lets another person regenerate the stated procedure and understand which evidence supports each result. Reproducibility is not correctness: the same bug can produce the same wrong answer repeatedly. A random seed can make randomized steps more repeatable under stated conditions, but does not guarantee identical results across environments or validate a model.

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

Hallucination or confabulation is plausible but false or unsupported output [66]. In engineering, it may appear as an invented standard citation, incorrect material property or flawed equation. Trace claims to original, authoritative sources and independently check equations with known numerical cases, units and assumptions. A fluent response or citation label is not evidence. Pass outputs through a verification gate before using them in a report, calculation or system action.

Use precise language for different kinds of bias [75]. Data-coverage bias means relevant machines, people or operating conditions are missing or underrepresented in the examples. Social fairness concerns unequal performance or impact across people or groups when relevant to the application. The bias term in a neural network is an additive model parameter. These are distinct meanings and need different analyses; do not treat one as evidence about another.

## Protect information and systems

Do not share restricted personal, assessment or proprietary data without permission and appropriate safeguards. Follow institutional disclosure and information-handling policies. Generated code and connected tools can introduce security risks; review their behavior, permissions, inputs and outputs before integrating them with engineering systems. Use source control and logging so changes and actions can be examined.

## Make human oversight operational

“Human in the loop” is not a control unless responsibility is specific [9]. Name the reviewer and decision owner, state which outputs require review, define what evidence must be checked, and give an authorized person explicit ability to pause or stop an action. Keep an audit trail of data provenance, assumptions, units, baseline comparisons and decisions. For an unsupported claim, restricted information or sensor shift, specify the corrective action rather than relying on a general warning.

## Account for resources and disclosure

AI computation consumes physical resources [76]. Choose methods scaled to the engineering task and balance analytical needs against available compute and resource constraints; avoid unsupported numerical claims about a tool's footprint. Disclose AI assistance as required by institutional policy and retain a verifiable reasoning trail so a reviewer can distinguish supplied evidence, generated suggestions and the engineer's final decisions.

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

A high-fidelity simulation can be expensive to run for every design [20]. A surrogate learns an approximation from evaluated designs or operating cases and can screen additional candidates at lower cost. For example, it can help compare pump or geometry candidates without rerunning an expensive flow simulation for every option. Its accuracy is supported only where the underlying evidence represents the inputs and conditions being considered.

Re-evaluate promising candidates with the original simulation or experiment. Verification checks that the intended model or calculation was implemented correctly; physical validation checks its adequacy against appropriate evidence from the real system. A surrogate helps explore the design space but does not replace either check or authorize a hardware claim.

An uncertainty-aware search method such as Bayesian optimization can use a surrogate to prioritize which candidate to evaluate next [77]. It can make expensive searches more efficient, but it does not verify the implementation, prove constraint satisfaction or establish physical validity.

## Objectives and constraints answer different questions

An objective states the performance goal, such as reducing a pump's electrical power demand [19]. Constraints and bounds define which designs or outcomes are permitted—for example, a minimum required flow or a maximum allowable stress. The feasible design space contains only candidates that satisfy all stated constraints.

A candidate can have an attractive predicted objective and still be infeasible: a design that predicts low power but violates a stress or flow limit is not acceptable. Check constraint values and their units separately from the objective; do not treat a good score as evidence that a design meets its bounds.

## Connected twins and physics-informed learning

An isolated CAD model has no active data connection to the physical equipment [78]. A digital twin maintains a data linkage with its physical counterpart—for example, a digital representation that receives ongoing pressure, flow or temperature measurements for monitoring and state estimation. The connection, not visual similarity, is the key distinction.

An active sensor connection also creates data-integrity and cybersecurity responsibilities. Check that the measurements and data path are trustworthy, and investigate disagreement between the model and independent physical readings before acting on a prediction.

Physics-informed learning incorporates physical equations or constraints into a learning approach, for example by adding a penalty when a predicted state violates a governing equation or conservation relationship [79], [80]. A physics-informed neural network (PINN) is one particular architectural family; it is not a synonym for every hybrid or physics-informed model. Examples of physical structure include a force relationship such as F = ma or thermodynamic constraints.

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

Choose a split that reflects intended use [51]. When examples share a machine, event, design or time sequence, keep related records together or hold out an appropriate group or later period; random row splitting can make evaluation too optimistic.

Fit preprocessing using training data only. Use validation data to make development choices, then lock the final test set and use it only for the final evaluation. This keeps information from the evaluation examples out of preprocessing and model selection.

## Compare baselines and report quantitative errors

Compare the model with a training-mean predictor and, when appropriate, a known physical calculation on the same evaluation cases. For pump power, the training-mean predictor is a simple reference; an appropriate physical calculation supplies a second comparison. A baseline helps show whether the model adds value beyond a simple or established approach.

On the locked test set, report task-appropriate measures with units. For regression, show MAE and RMSE in the target's unit and residuals in consistent SI units; residuals show signed prediction errors and can reveal systematic under- or over-prediction, such as errors that grow at high pressure. For classification, report the relevant class counts and measures such as precision and recall. Interpret the results in engineering terms rather than presenting a score alone.

Add an independent physical check or known case, and state domain limits and assumptions. Model metrics summarize performance on selected examples; they do not establish physical validity outside the evaluated conditions.

Retain evidence for each stage: the decision, inputs and provenance for problem framing; the split, baseline and fitted preprocessing for development; locked-test errors and limitations for evaluation; and known-case or independent physical checks for verification. This record lets a reviewer distinguish a repeatable method from an unsupported conclusion.

## Keep the project reproducible and your own

The four starter notebooks cover data inspection, pump-power modelling, fault detection and verification of an AI-assisted engineering draft. Begin with the relevant starter, inspect its assumptions, and explain any changes in your own words. A complete reference is an example of a route, not a substitute for your own work.

Keep the notebook runnable from a clean kernel and record the data, environment, split, baseline, modelling choices, checks, limitations and failure modes [35]. Follow institutional policy for AI assistance, disclose permitted use and checks, and do not submit private or restricted information to an external service without authorization.

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

## References

[1] S. Russell and P. Norvig, *Artificial Intelligence: A Modern Approach*, 4th ed. Hoboken, NJ, USA: Pearson, 2021. (Cited in Lesson 1.1)

[2] T. M. Mitchell, *Machine Learning*. Boston, MA, USA: McGraw-Hill, 1997. (Cited in Lessons 1.1, 6.1)

[3] Y. LeCun, Y. Bengio, and G. Hinton, “Deep learning,” *Nature*, vol. 521, no. 7553, pp. 436–444, 2015. doi: 10.1038/nature14539 (Cited in Lessons 1.1, 11.3)

[4] I. Goodfellow, Y. Bengio, and A. Courville, *Deep Learning*. Cambridge, MA, USA: MIT Press, 2016. (Cited in Lessons 1.1, 2.2, 4.2, 6.2, 10.2, 11.1, 11.2, 11.3, 12.2)

[5] F. Provost and T. Fawcett, “Data science and its relationship to big data and data-driven decision making,” *Big Data*, vol. 1, no. 1, pp. 51–59, 2013. doi: 10.1089/big.2013.1508 (Cited in Lesson 1.1)

[6] R. Parasuraman, T. B. Sheridan, and C. D. Wickens, “A model for types and levels of human interaction with automation,” *IEEE Trans. Syst., Man, Cybern. A, Syst. Humans*, vol. 30, no. 3, pp. 286–297, 2000. doi: 10.1109/3468.844354 (Cited in Lesson 1.2)

[7] K. J. Åström and R. M. Murray, *Feedback Systems: An Introduction for Scientists and Engineers*, 2nd ed. Princeton, NJ, USA: Princeton Univ. Press, 2021. (Cited in Lessons 1.2, 2.2)

[8] M. R. Morris et al., “Position: Levels of AGI for operationalizing progress on the path to AGI,” in *Proc. 41st Int. Conf. Mach. Learn. (ICML)*, PMLR, vol. 235, 2024, pp. 36308–36321. (Cited in Lesson 1.2)

[9] National Institute of Standards and Technology, “Artificial Intelligence Risk Management Framework (AI RMF 1.0),” NIST AI 100-1, Gaithersburg, MD, USA, 2023. doi: 10.6028/NIST.AI.100-1 (Cited in Lessons 1.2, 1.3, 8.3, 15.3)

[10] Y. Lei, B. Yang, X. Jiang, F. Jia, N. Li, and A. K. Nandi, “Applications of machine learning to machine fault diagnosis: A review and roadmap,” *Mech. Syst. Signal Process.*, vol. 138, Art. no. 106587, 2020. doi: 10.1016/j.ymssp.2019.106587 (Cited in Lessons 1.2, 2.2, 5.3)

[11] Y. Lei, N. Li, L. Guo, N. Li, T. Yan, and J. Lin, “Machinery health prognostics: A systematic review from data acquisition to RUL prediction,” *Mech. Syst. Signal Process.*, vol. 104, pp. 799–834, 2018. doi: 10.1016/j.ymssp.2017.11.016 (Cited in Lesson 1.3)

[12] C. Guo, G. Pleiss, Y. Sun, and K. Q. Weinberger, “On calibration of modern neural networks,” in *Proc. 34th Int. Conf. Mach. Learn. (ICML)*, PMLR, vol. 70, 2017, pp. 1321–1330. (Cited in Lessons 1.3, 8.1, 15.1)

[13] W. L. Oberkampf and C. J. Roy, *Verification and Validation in Scientific Computing*. Cambridge, U.K.: Cambridge Univ. Press, 2010. doi: 10.1017/CBO9780511760396 (Cited in Lessons 1.3, 15.2)

[14] J. Willard, X. Jia, S. Xu, M. Steinbach, and V. Kumar, “Integrating scientific knowledge with machine learning for engineering and environmental systems,” *ACM Comput. Surv.*, vol. 55, no. 4, pp. 1–37, 2023. doi: 10.1145/3514228 (Cited in Lessons 2.1, 2.3)

[15] J. F. Gülich, *Centrifugal Pumps*, 3rd ed. Berlin, Germany: Springer, 2014. doi: 10.1007/978-3-642-40114-5 (Cited in Lesson 2.1)

[16] G. James, D. Witten, T. Hastie, and R. Tibshirani, *An Introduction to Statistical Learning: With Applications in R*, 2nd ed. New York, NY, USA: Springer, 2021. doi: 10.1007/978-1-0716-1418-1 (Cited in Lessons 2.1, 2.3, 3.1, 4.1, 5.2, 7.1, 9.1)

[17] A. Karpatne et al., “Theory-guided data science: A new paradigm for scientific discovery from data,” *IEEE Trans. Knowl. Data Eng.*, vol. 29, no. 10, pp. 2318–2331, 2017. doi: 10.1109/TKDE.2017.2720168 (Cited in Lesson 2.1)

[18] R. J. Hyndman and G. Athanasopoulos, *Forecasting: Principles and Practice*, 3rd ed. Melbourne, Australia: OTexts, 2021. [Online]. Available: https://otexts.com/fpp3/ (Cited in Lessons 2.2, 3.1, 12.2, 12.3)

[19] S. Boyd and L. Vandenberghe, *Convex Optimization*. Cambridge, U.K.: Cambridge Univ. Press, 2004. doi: 10.1017/CBO9780511804441 (Cited in Lessons 2.2, 16.1)

[20] A. I. J. Forrester, A. Sóbester, and A. J. Keane, *Engineering Design via Surrogate Modelling: A Practical Guide*. Chichester, U.K.: Wiley, 2008. doi: 10.1002/9780470770801 (Cited in Lessons 2.3, 16.1)

[21] J. Quiñonero-Candela, M. Sugiyama, A. Schwaighofer, and N. D. Lawrence, Eds., *Dataset Shift in Machine Learning*. Cambridge, MA, USA: MIT Press, 2009. doi: 10.7551/mitpress/9780262170055.001.0001 (Cited in Lessons 2.3, 15.1)

[22] M. D. Wilkinson et al., “The FAIR Guiding Principles for scientific data management and stewardship,” *Sci. Data*, vol. 3, Art. no. 160018, 2016. doi: 10.1038/sdata.2016.18 (Cited in Lesson 3.2)

[23] S. S. Stevens, “On the theory of scales of measurement,” *Science*, vol. 103, no. 2684, pp. 677–680, 1946. doi: 10.1126/science.103.2684.677 (Cited in Lesson 3.2)

[24] Joint Committee for Guides in Metrology, “Evaluation of measurement data—Guide to the expression of uncertainty in measurement,” JCGM 100:2008, BIPM, Sèvres, France, 2008. doi: 10.59161/JCGM100-2008E (Cited in Lesson 3.2)

[25] S. Kaufman, S. Rosset, C. Perlich, and O. Stitelman, “Leakage in data mining: Formulation, detection, and avoidance,” *ACM Trans. Knowl. Discov. Data*, vol. 6, no. 4, pp. 1–21, 2012. doi: 10.1145/2382577.2382579 (Cited in Lessons 3.3, 10.3)

[26] J. Pearl, *Causality: Models, Reasoning, and Inference*, 2nd ed. Cambridge, U.K.: Cambridge Univ. Press, 2009. doi: 10.1017/CBO9780511803161 (Cited in Lesson 3.3)

[27] V. Chandola, A. Banerjee, and V. Kumar, “Anomaly detection: A survey,” *ACM Comput. Surv.*, vol. 41, no. 3, pp. 1–58, 2009. doi: 10.1145/1541880.1541882 (Cited in Lessons 4.1, 5.1)

[28] O. Chapelle, B. Schölkopf, and A. Zien, Eds., *Semi-Supervised Learning*. Cambridge, MA, USA: MIT Press, 2006. doi: 10.7551/mitpress/9780262033589.001.0001 (Cited in Lesson 4.1)

[29] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “BERT: Pre-training of deep bidirectional transformers for language understanding,” in *Proc. 2019 Conf. North Amer. Chapter Assoc. Comput. Linguistics: Human Lang. Technol. (NAACL-HLT)*, 2019, pp. 4171–4186. doi: 10.18653/v1/N19-1423 (Cited in Lessons 4.2, 13.3)

[30] R. S. Sutton and A. G. Barto, *Reinforcement Learning: An Introduction*, 2nd ed. Cambridge, MA, USA: MIT Press, 2018. (Cited in Lesson 4.3)

[31] D. Amodei, C. Olah, J. Steinhardt, P. Christiano, J. Schulman, and D. Mané, “Concrete problems in AI safety,” 2016, arXiv:1606.06565. doi: 10.48550/arXiv.1606.06565 (Cited in Lesson 4.3)

[32] R. J. A. Little and D. B. Rubin, *Statistical Analysis With Missing Data*, 3rd ed. Hoboken, NJ, USA: Wiley, 2019. doi: 10.1002/9781119482260 (Cited in Lesson 5.1)

[33] F. Pedregosa et al., “Scikit-learn: Machine learning in Python,” *J. Mach. Learn. Res.*, vol. 12, pp. 2825–2830, 2011. (Cited in Lessons 5.2, 5.3)

[34] C. J. Willmott and K. Matsuura, “Advantages of the mean absolute error (MAE) over the root mean square error (RMSE) in assessing average model performance,” *Clim. Res.*, vol. 30, pp. 79–82, 2005. doi: 10.3354/cr030079 (Cited in Lessons 6.2, 7.2)

[35] J. Pineau et al., “Improving reproducibility in machine learning research (A report from the NeurIPS 2019 reproducibility program),” *J. Mach. Learn. Res.*, vol. 22, no. 164, pp. 1–20, 2021. (Cited in Lessons 6.3, 10.3, 15.2, 16.2)

[36] F. J. Anscombe, “Graphs in statistical analysis,” *Amer. Statistician*, vol. 27, no. 1, pp. 17–21, 1973. doi: 10.1080/00031305.1973.10478966 (Cited in Lesson 7.2)

[37] T. Gebru et al., “Datasheets for datasets,” *Commun. ACM*, vol. 64, no. 12, pp. 86–92, 2021. doi: 10.1145/3458723 (Cited in Lessons 7.3, 15.2)

[38] S. Arlot and A. Celisse, “A survey of cross-validation procedures for model selection,” *Statist. Surv.*, vol. 4, pp. 40–79, 2010. doi: 10.1214/09-SS054 (Cited in Lessons 7.3, 10.1)

[39] T. Fawcett, “An introduction to ROC analysis,” *Pattern Recognit. Lett.*, vol. 27, no. 8, pp. 861–874, 2006. doi: 10.1016/j.patrec.2005.10.010 (Cited in Lessons 8.1, 8.2)

[40] M. Sokolova and G. Lapalme, “A systematic analysis of performance measures for classification tasks,” *Inf. Process. Manage.*, vol. 45, no. 4, pp. 427–437, 2009. doi: 10.1016/j.ipm.2009.03.002 (Cited in Lesson 8.2)

[41] T. Saito and M. Rehmsmeier, “The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets,” *PLoS ONE*, vol. 10, no. 3, Art. no. e0118432, 2015. doi: 10.1371/journal.pone.0118432 (Cited in Lesson 8.2)

[42] H. He and E. A. Garcia, “Learning from imbalanced data,” *IEEE Trans. Knowl. Data Eng.*, vol. 21, no. 9, pp. 1263–1284, 2009. doi: 10.1109/TKDE.2008.239 (Cited in Lesson 8.3)

[43] T. M. Cover and P. E. Hart, “Nearest neighbor pattern classification,” *IEEE Trans. Inf. Theory*, vol. 13, no. 1, pp. 21–27, 1967. doi: 10.1109/TIT.1967.1053964 (Cited in Lesson 9.1)

[44] C. Cortes and V. Vapnik, “Support-vector networks,” *Mach. Learn.*, vol. 20, no. 3, pp. 273–297, 1995. doi: 10.1007/BF00994018 (Cited in Lesson 9.1)

[45] L. Breiman, J. H. Friedman, R. A. Olshen, and C. J. Stone, *Classification and Regression Trees*. Belmont, CA, USA: Wadsworth, 1984. (Cited in Lesson 9.2)

[46] L. Breiman, “Random forests,” *Mach. Learn.*, vol. 45, no. 1, pp. 5–32, 2001. doi: 10.1023/A:1010933404324 (Cited in Lesson 9.2)

[47] J. H. Friedman, “Greedy function approximation: A gradient boosting machine,” *Ann. Statist.*, vol. 29, no. 5, pp. 1189–1232, 2001. doi: 10.1214/aos/1013203451 (Cited in Lesson 9.2)

[48] S. P. Lloyd, “Least squares quantization in PCM,” *IEEE Trans. Inf. Theory*, vol. 28, no. 2, pp. 129–137, 1982. doi: 10.1109/TIT.1982.1056489 (Cited in Lesson 9.3)

[49] I. T. Jolliffe and J. Cadima, “Principal component analysis: A review and recent developments,” *Philos. Trans. R. Soc. A*, vol. 374, no. 2065, Art. no. 20150202, 2016. doi: 10.1098/rsta.2015.0202 (Cited in Lesson 9.3)

[50] G. C. Cawley and N. L. C. Talbot, “On over-fitting in model selection and subsequent selection bias in performance evaluation,” *J. Mach. Learn. Res.*, vol. 11, pp. 2079–2107, 2010. (Cited in Lesson 9.3)

[51] D. R. Roberts et al., “Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure,” *Ecography*, vol. 40, no. 8, pp. 913–929, 2017. doi: 10.1111/ecog.02881 (Cited in Lessons 10.1, 12.3, 16.2)

[52] S. Geman, E. Bienenstock, and R. Doursat, “Neural networks and the bias/variance dilemma,” *Neural Comput.*, vol. 4, no. 1, pp. 1–58, 1992. doi: 10.1162/neco.1992.4.1.1 (Cited in Lesson 10.2)

[53] L. Prechelt, “Early stopping—But when?,” in *Neural Networks: Tricks of the Trade* (Lecture Notes in Computer Science, vol. 1524), G. B. Orr and K.-R. Müller, Eds. Berlin, Germany: Springer, 1998, pp. 55–69. doi: 10.1007/3-540-49430-8_3 (Cited in Lessons 10.2, 11.3)

[54] R. Tibshirani, “Regression shrinkage and selection via the lasso,” *J. Roy. Statist. Soc. B*, vol. 58, no. 1, pp. 267–288, 1996. doi: 10.1111/j.2517-6161.1996.tb02080.x (Cited in Lesson 10.2)

[55] S. Kapoor and A. Narayanan, “Leakage and the reproducibility crisis in machine-learning-based science,” *Patterns*, vol. 4, no. 9, Art. no. 100804, 2023. doi: 10.1016/j.patter.2023.100804 (Cited in Lessons 10.3, 12.1)

[56] J. Gama, I. Žliobaitė, A. Bifet, M. Pechenizkiy, and A. Bouchachia, “A survey on concept drift adaptation,” *ACM Comput. Surv.*, vol. 46, no. 4, pp. 1–37, 2014. doi: 10.1145/2523813 (Cited in Lessons 10.3, 15.1)

[57] V. Nair and G. E. Hinton, “Rectified linear units improve restricted Boltzmann machines,” in *Proc. 27th Int. Conf. Mach. Learn. (ICML)*, 2010, pp. 807–814. (Cited in Lesson 11.1)

[58] D. E. Rumelhart, G. E. Hinton, and R. J. Williams, “Learning representations by back-propagating errors,” *Nature*, vol. 323, no. 6088, pp. 533–536, 1986. doi: 10.1038/323533a0 (Cited in Lesson 11.2)

[59] Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner, “Gradient-based learning applied to document recognition,” *Proc. IEEE*, vol. 86, no. 11, pp. 2278–2324, 1998. doi: 10.1109/5.726791 (Cited in Lesson 12.1)

[60] A. Vaswani et al., “Attention is all you need,” in *Adv. Neural Inf. Process. Syst. (NeurIPS)*, vol. 30, 2017, pp. 5998–6008. (Cited in Lessons 12.2, 13.2)

[61] S. Hochreiter and J. Schmidhuber, “Long short-term memory,” *Neural Comput.*, vol. 9, no. 8, pp. 1735–1780, 1997. doi: 10.1162/neco.1997.9.8.1735 (Cited in Lesson 12.2)

[62] T. B. Brown et al., “Language models are few-shot learners,” in *Adv. Neural Inf. Process. Syst. (NeurIPS)*, vol. 33, 2020. (Cited in Lessons 13.1, 13.3, 14.1)

[63] R. Bommasani et al., “On the opportunities and risks of foundation models,” 2021, arXiv:2108.07258. doi: 10.48550/arXiv.2108.07258 (Cited in Lesson 13.1)

[64] J. Ho, A. Jain, and P. Abbeel, “Denoising diffusion probabilistic models,” in *Adv. Neural Inf. Process. Syst. (NeurIPS)*, vol. 33, 2020, pp. 6840–6851. (Cited in Lesson 13.1)

[65] I. J. Goodfellow et al., “Generative adversarial nets,” in *Adv. Neural Inf. Process. Syst. (NIPS)*, vol. 27, 2014, pp. 2672–2680. (Cited in Lesson 13.1)

[66] Z. Ji et al., “Survey of hallucination in natural language generation,” *ACM Comput. Surv.*, vol. 55, no. 12, pp. 1–38, 2023. doi: 10.1145/3571730 (Cited in Lessons 13.1, 15.3)

[67] R. Sennrich, B. Haddow, and A. Birch, “Neural machine translation of rare words with subword units,” in *Proc. 54th Annu. Meeting Assoc. Comput. Linguistics (ACL)*, 2016, pp. 1715–1725. doi: 10.18653/v1/P16-1162 (Cited in Lesson 13.2)

[68] N. F. Liu et al., “Lost in the middle: How language models use long contexts,” *Trans. Assoc. Comput. Linguistics*, vol. 12, pp. 157–173, 2024. doi: 10.1162/tacl_a_00638 (Cited in Lesson 13.2)

[69] T. Mikolov, K. Chen, G. Corrado, and J. Dean, “Efficient estimation of word representations in vector space,” 2013, arXiv:1301.3781. doi: 10.48550/arXiv.1301.3781 (Cited in Lesson 13.2)

[70] S. J. Pan and Q. Yang, “A survey on transfer learning,” *IEEE Trans. Knowl. Data Eng.*, vol. 22, no. 10, pp. 1345–1359, 2010. doi: 10.1109/TKDE.2009.191 (Cited in Lesson 13.3)

[71] P. Lewis et al., “Retrieval-augmented generation for knowledge-intensive NLP tasks,” in *Adv. Neural Inf. Process. Syst. (NeurIPS)*, vol. 33, 2020. (Cited in Lessons 13.3, 14.2)

[72] J. A. Duffie, W. A. Beckman, and N. Blair, *Solar Engineering of Thermal Processes, Photovoltaics and Wind*, 5th ed. Hoboken, NJ, USA: Wiley, 2020. doi: 10.1002/9781119540328 (Cited in Lesson 14.1)

[73] M. Chen et al., “Evaluating large language models trained on code,” 2021, arXiv:2107.03374. doi: 10.48550/arXiv.2107.03374 (Cited in Lesson 14.3)

[74] E. Hüllermeier and W. Waegeman, “Aleatoric and epistemic uncertainty in machine learning: An introduction to concepts and methods,” *Mach. Learn.*, vol. 110, no. 3, pp. 457–506, 2021. doi: 10.1007/s10994-021-05946-3 (Cited in Lesson 15.1)

[75] N. Mehrabi, F. Morstatter, N. Saxena, K. Lerman, and A. Galstyan, “A survey on bias and fairness in machine learning,” *ACM Comput. Surv.*, vol. 54, no. 6, pp. 1–35, 2022. doi: 10.1145/3457607 (Cited in Lesson 15.3)

[76] E. Strubell, A. Ganesh, and A. McCallum, “Energy and policy considerations for deep learning in NLP,” in *Proc. 57th Annu. Meeting Assoc. Comput. Linguistics (ACL)*, 2019, pp. 3645–3650. doi: 10.18653/v1/P19-1355 (Cited in Lesson 15.3)

[77] B. Shahriari, K. Swersky, Z. Wang, R. P. Adams, and N. de Freitas, “Taking the human out of the loop: A review of Bayesian optimization,” *Proc. IEEE*, vol. 104, no. 1, pp. 148–175, 2016. doi: 10.1109/JPROC.2015.2494218 (Cited in Lesson 16.1)

[78] W. Kritzinger, M. Karner, G. Traar, J. Henjes, and W. Sihn, “Digital twin in manufacturing: A categorical literature review and classification,” *IFAC-PapersOnLine*, vol. 51, no. 11, pp. 1016–1022, 2018. doi: 10.1016/j.ifacol.2018.08.474 (Cited in Lesson 16.1)

[79] M. Raissi, P. Perdikaris, and G. E. Karniadakis, “Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations,” *J. Comput. Phys.*, vol. 378, pp. 686–707, 2019. doi: 10.1016/j.jcp.2018.10.045 (Cited in Lesson 16.1)

[80] G. E. Karniadakis, I. G. Kevrekidis, L. Lu, P. Perdikaris, S. Wang, and L. Yang, “Physics-informed machine learning,” *Nat. Rev. Phys.*, vol. 3, no. 6, pp. 422–440, 2021. doi: 10.1038/s42254-021-00314-5 (Cited in Lesson 16.1)

