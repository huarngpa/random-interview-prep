# UV Test Harness

For interview prep, keep the harness simple.

## Recommendation

Use:

- one file per problem in `problems/`
- one test file per problem in `tests/`
- one tiny shared helper in `interview_prep/harness.py`

That gives you:

- fast repetition
- easy copy-paste workflow
- clean isolation between problems
- enough structure without building a framework you have to maintain

## Layout

```text
anthropic-interview-prep/
├── docs/
├── interview_prep/
│   └── harness.py
├── problems/
│   ├── contains_duplicate.py
│   └── template.py
├── tests/
│   ├── test_contains_duplicate.py
│   └── test_template.py
└── pyproject.toml
```

## Workflow

Create a new problem:

1. Copy `problems/template.py` to `problems/<problem_name>.py`
2. Copy `tests/test_template.py` to `tests/test_<problem_name>.py`
3. Implement `solve(...)`
4. Add cases using `Case(...)`
5. Run the tests

Run everything:

```bash
uv run python -m unittest discover -s tests -p 'test_*.py' -v
```

Run one file:

```bash
uv run python -m unittest tests.test_contains_duplicate -v
```

## Why Not Something More Complex?

At this stage, a heavier framework would mostly slow you down.

You do not need:

- dynamic problem registries
- code generation
- custom CLI commands
- benchmark suites

Those can wait until you have enough repetitions that the simple layout actually hurts.
