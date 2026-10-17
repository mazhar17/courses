# Phase 1 code walkthroughs: prerequisite conflict

Status: blocked before feature implementation. This draft PR records the conflict required by the implementation prompt's final instruction: "If anything in this prompt conflicts with what you find in the repository, stop and describe the conflict in the PR instead of guessing."

## Verified baseline

The feature branch starts at main commit `a77dd470e9d59747720292ce9943083ab997c234`.

I copied the five unmodified generator inputs from `AI101/source/` into an isolated temporary folder and executed `python build_ai101.py` there. I did not rebuild in the repository or replace any published file.

Build summary:

```text
Built 16 modules, 48 lessons, 128 questions, 154 terms and 8 notebooks.
```

Comparing its embedded DATA with `AI101/AI_101_for_Mechanical_Engineers.html` at the same main commit gives:

| Comparison | Result |
|---|---|
| Lesson objects | All 48 differ |
| Quiz question objects | All 128 differ |
| Source quiz types | 93 single-answer, 16 multiple-answer, 19 numerical |
| Published quiz types | 109 single-answer, zero multiple-answer, 19 numerical |
| Terms | Unchanged |
| Four project lab objects, including eight notebooks | Unchanged |
| Portable course text | Differs |
| Rebuilt HTML versus published HTML | Different |

Examples of lesson text regression if the existing source were rebuilt:

| Lesson | Source word count | Published word count |
|---|---:|---:|
| 1.1 | 153 | 827 |
| 1.2 | 123 | 796 |
| 1.3 | 121 | 719 |
| 2.1 | 135 | 465 |
| 2.2 | 130 | 324 |
| 2.3 | 134 | 446 |

The source contains older material. An ordinary rebuild would replace the enriched lesson texts and undo the recently published quiz-only revision. This conflicts with the hard requirements to leave lessons and quizzes unchanged and not edit `ai101_content.py`.

## Additional source-layout finding

The build script writes outputs relative to the current working directory. Running it inside `AI101/source/`, as the implementation prompt requests, creates a new HTML file and notebook folder inside `source/`; it does not update the published files in the parent `AI101/` folder. That output-location mismatch also needs an explicit resolution before build integration.

`AI_101_for_Mechanical_Engineers_Online.html` is not an output of this builder. It is a separate tracked variant and has been left untouched.

## Scope of this commit

Only this diagnostic Markdown file is added. No generated HTML, source code, lesson, quiz, term, review media, notebook, grading rule, progress schema, workflow, Pages setting or main-branch file is changed.

No walkthrough, route, tab, copy button or walkthrough notebook has been implemented. Phase 1 is not complete; Phase 2 has not started. Screenshots and walkthrough runtime tests are pending feature implementation.

## Maintainer decision needed

Please specify an approved prerequisite for reconciling the generator sources with the authoritative published course while preserving the published content exactly. That reconciliation would require instructions beyond the prompt's prohibition on editing `ai101_content.py`. After the source/build conflict is resolved or the constraints are explicitly revised, Phase 1 can continue on this same branch and draft PR.

## Preview plan after implementation

Check out `feature/code-walkthroughs` (or download its ZIP), open `AI101/AI_101_for_Mechanical_Engineers.html` in a browser, and navigate to `#/m/2/code`. That route is not implemented in this diagnostic commit.

The future branch-specific Colab preview URL is:

`https://colab.research.google.com/github/mazhar17/courses/blob/feature/code-walkthroughs/AI101/AI_101_notebooks/walkthrough_m02.ipynb`

The notebook does not exist yet. The eventual page will retain the required `main` Colab URL, which will work only after the maintainer merges the implementation. The live site remains unchanged.
