# python_ai

Practice repo for the 30-day plan: **Python recap → FastAPI → LLMs → RAG → Agents → MCP → AI system design**,
with NeuroDocx as the running case study.

Learn on one laptop, code here on the other. New exercises get pushed after each lesson —
run `git pull` before you start.

## Setup (once, on the practice laptop)

```bash
git clone https://github.com/SurendraNandamudi/python_ai.git
cd python_ai

# Option A — uv (recommended, fast)
brew install uv            # or: curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync                    # creates .venv and installs pytest
uv run pytest              # run all tests

# Option B — plain venv
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
pytest
```

## How to practise

1. Open an exercise file, e.g. `session01/ex2_strings.py`.
2. Replace each `raise NotImplementedError` with your code. **Don't look up the solution first.**
3. Run only that file's tests:
   ```bash
   uv run pytest session01/tests/test_ex2_strings.py -v
   ```
4. All green → commit and push:
   ```bash
   git add -A && git commit -m "session01: strings done" && git push
   ```
5. Stuck for >15 min? Tell your mentor which test fails and what you tried.

`ex1_memory.py` is different — it is a **predict-then-run** file. Write your prediction in each
`# PREDICT:` comment *first*, then run `python -m session01.ex1_memory` and compare.

## Progress

| Session | Topic | Exercises | Status |
|---|---|---|---|
| 01 | Memory model · strings · lists · tuples · sets · dicts | `session01/` | ⬜ |
| 02 | Functions · comprehensions · scope · closures | — | ⬜ |
| 03 | OOP · dataclasses · dunder methods · enums | — | ⬜ |
| 04 | Iterators · generators · decorators · context managers | — | ⬜ |
| 05 | Type hints · modules · packages · project structure | — | ⬜ |
| 06 | Async · concurrency | — | ⬜ |
| 07 | Pydantic · HTTP · testing · logging | — | ⬜ |

Revision notes live in `notes/`.
