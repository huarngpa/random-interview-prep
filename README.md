# Anthropic Interview Prep

Lightweight Python interview practice harness built with `uv`.

## What This Repo Is For

Use this repo to:

- practice LeetCode-style problems quickly
- keep one solution per file
- attach focused test cases to each problem
- build repetition without maintaining a heavy framework

## Repo Layout

```text
anthropic-interview-prep/
├── docs/
│   └── anthropic/
├── interview_prep/
│   └── harness.py
├── problems/
├── tests/
├── pyproject.toml
└── uv.lock
```

## Setup

Make sure `uv` is installed, then from the repo root run:

```bash
uv sync
```

That creates the local virtual environment in `.venv/`.

## How To Run Tests

Run the full test suite:

```bash
uv run python -m unittest discover -s tests -p 'test_*.py' -v
```

Run one test file:

```bash
uv run python -m unittest tests.test_contains_duplicate -v
```

Run one specific test method:

```bash
uv run python -m unittest tests.test_contains_duplicate.ContainsDuplicateTests.test_cases -v
```

## How To Add A New Problem

1. Copy `problems/template.py` to `problems/<problem_name>.py`
2. Copy `tests/test_template.py` to `tests/test_<problem_name>.py`
3. Implement `solve(...)` in the problem file
4. Add `Case(...)` entries in the test file
5. Run the tests

Example:

```bash
cp problems/template.py problems/two_sum.py
cp tests/test_template.py tests/test_two_sum.py
```

## How The Harness Works

Shared helpers live in `interview_prep/harness.py`.

You mainly use:

- `Case(...)` to define inputs and expected outputs
- `assert_cases(...)` to run a batch of cases against `solve(...)`

## Current Example

Reference example:

- solution: `problems/contains_duplicate.py`
- test: `tests/test_contains_duplicate.py`

## Notes

- The template test is intentionally skipped until you copy it for a real problem.
- The docs for Anthropic prep live in `docs/anthropic/`.
