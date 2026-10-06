# AI 101 for Mechanical Engineers

A beginner, self-paced course for undergraduate mechanical engineering students.

## Start the course

Open `AI_101_for_Mechanical_Engineers.html` in a modern browser. The course interface, lessons, interactive demonstrations, quizzes, glossary and notebook downloads are contained in this one file. No account, server, API key or internet connection is needed for the HTML course.

The course contains 16 modules, 48 lessons, 154 glossary terms, 128 module quiz questions, a 24-question final assessment and four practical labs. Examples include pumps, faults, sensors, energy calculations and engineering design. Planning estimate: 18–24 hours including practice; adjust to your class.

## Recommended learning sequence

1. Read the three lessons in each module and try its activity.
2. Review the glossary or flashcards and take the module quiz.
3. Complete Labs 1–4 at suitable points in the course, using the starter notebooks before consulting references.
4. Take the final assessment, covering all 16 modules.
5. Complete the mini-project and submit evidence using the checklist and rubric.

## Progress and assessment

Progress is stored in the browser when local storage is available. Export a progress backup regularly, especially before moving or replacing the HTML file or clearing browser data. Import the backup to restore progress. When storage is blocked, the course can retain progress only for the current session; export before closing it.

Knowledge grade = 70% mean best module quiz score + 30% best final score. Every module quiz and the final must achieve at least 70% to enable a printable knowledge completion record. Retakes are allowed. The final draws 24 distinct items from the module bank, including at least one from each module; it is a formative assessment, not a secure independent examination.

The printable record is self-reported and unauthenticated. Practical notebooks and the mini-project require separate instructor or peer review; their rubric does not feed into the browser grade. Answer keys are inspectable in this offline file.

## Notebook setup

Notebook code does not execute in the HTML page. Use local Python 3.10+ and NumPy 1.26+; JupyterLab is optional but convenient. Initial installation requires internet access unless packages are already available locally.

    python -m pip install -r AI_101_requirements.txt
    jupyter lab

All four labs use synthetic teaching data and make no external AI calls. Starter TODOs intentionally raise `NotImplementedError` until completed. Reference notebooks can run from top to bottom. Actual execution was verified with Python 3.12.14 and NumPy 2.3.5; compatibility with every target version has not been tested.

## Instructor preparation

Review examples and the rubric, set your AI-use policy, and adapt the workload to the cohort. Instructor details can be entered in course settings for the current browser profile. Change permanent defaults in `source/ai101_app.js`, curriculum in `source/ai101_content.py`, notebooks in `source/ai101_notebooks.py`, and layout in `source/ai101_shell.html`. From the extracted `source` folder run `python build_ai101.py` to generate a new course and companions there; copy the resulting HTML to your distribution folder.

Review `AI_101_validation.md` before distribution. Automated content/scoring tests and notebook executions passed, but a visual and interactive browser acceptance review remains necessary. A suggested acceptance checklist is included there.

## Package contents

- HTML course, readable Markdown course text, notebook requirements and submission checklist.
- Eight notebooks: four starters and four complete references, with reference execution logs.
- Validation summary and reproducible build source/tests in `source/`.

The supplied source decks and previous HTML course were reference material; the original files were preserved.
