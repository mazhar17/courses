# AI 101 validation summary

Validation performed on 2026-10-06.

## Passed

- 16 modules, 48 lessons, 128 unique module quiz items, 154 glossary terms and eight notebook artifacts.
- All question answer keys achieve full credit; multiple-select penalties, duplicate/invalid selections and numeric tolerance boundaries tested.
- Final assessment: 24 unique questions covering all 16 modules for 1,000 tested seeds.
- Progress normalization preserves entered answers, profile, settings, lesson state, cards and project fields; canonical data round trips are stable.
- Imported attempt scores recomputed from answers; invalid course/schema rejected; unknown fields constrained; history truncation retains the old best and recent attempts.
- Best-attempt grading, 70/80/90 grade boundaries, all-module completion eligibility and storage-write failure behavior tested.
- Embedded JavaScript compiles. No external JavaScript, stylesheet or network API dependency detected. Static HTML parser ingestion and unique shell IDs pass.
- Eight notebook structures checked; all 32 code cells compile.
- All four reference notebooks executed top to bottom in fresh namespaces, with assertions passing. All four starters stop at their intended incomplete TODOs.

Automated JavaScript test groups: 12 passed.
Actual notebook environment: Python 3.12.14, NumPy 2.3.5.

## Example reference results

- Lab 1: flagged synthetic row IDs 4 and 6 for missing input and invalid pressure respectively.
- Lab 2: validation-selected hydraulic-feature model; locked test MAE 0.1033 kW, RMSE 0.1293 kW and R² 0.9913. Synthetic construction makes these illustrative results, not real-system performance claims.
- Lab 3: validation-selected threshold 0.4; test TP 6, FP 2, FN 0, TN 4. Rare-fault baseline has 99% accuracy and zero fault recall.
- Lab 4: DC power 3200 W, AC power 3072 W and illustrative constant-condition two-hour energy 6.144 kWh. Daily energy cannot be inferred from the instantaneous inputs.

## Unverified checks and limits

The browser automation service blocked opening a local `file:` URL. No visual browser preview, real-browser interaction, download/print behavior or screen-reader audit was completed. Static parsing and isolated JavaScript tests do not substitute for those checks.

Formal validation using the Python `nbformat` package was unavailable; explicit structural checks and code execution passed. Target Python/NumPy minimum versions were not separately tested.

## Suggested browser acceptance review before teaching

- Open the HTML locally in the browser students will use; check desktop and narrow-screen layout in both themes.
- Follow the skip link and navigate with the keyboard; verify visible focus, labels and confirmation dialogs.
- Try each activity, answer and submit a quiz, inspect feedback, retake it, and resume a partially answered quiz after reopening.
- Export/import progress, test with local storage disabled, and verify the storage warning and in-session behavior.
- Download and open a starter notebook, course text and checklist.
- Complete assessments and inspect the printable knowledge record; confirm that it is clearly self-reported and distinct from the practical rubric.

These checks are pending, not claimed as passed.
