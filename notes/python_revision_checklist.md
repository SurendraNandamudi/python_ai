# Python revision checklist

Status as of 2026-10-11. Tick a box only when you can explain it out loud AND its exercise is green.

Legend: **Taught** = covered in a lesson with visuals · **Self** = you studied it yourself ·
**Not yet** = no lesson so far (exercises may exist).

---

## A. Covered together in lessons

### 1. Memory model — `session01/ex1_memory.py`
- [ ] Names are labels pointing at objects; everything is an object
- [ ] `y = x` is a second label on the same object (no copy)
- [ ] Assignment moves a label; mutation changes the object
- [ ] `+=` : in place on a list, new object + rebind on an int/str
- [ ] Shallow copy (`.copy()`, `[:]`, `dict()`, `{**d}`) vs `copy.deepcopy`
- [ ] `==` (value) vs `is` (identity); `x is None`
- [ ] `x or default` bug with `0` / `""`; use `x if x is not None else default`
- [ ] Mutable default argument `def f(a, items=[])` → use `None`
- [ ] ⚠️ GAP: `[[0] * 3] * 2` shares ONE inner list → use a comprehension
- [ ] `dict.fromkeys(keys, [])` shares one list

### 2. Types and operators
- [ ] Dynamic but strong typing (`"1" + 1` → TypeError)
- [ ] `//` floors, `%` sign follows divisor, `round(2.5) == 2`, `0.1 + 0.2 != 0.3`
- [ ] Falsy values; `[]` and `{}` are falsy (unlike JS); `bool` is an `int`
- [ ] `None` vs JS `null`/`undefined`; missing key → `KeyError`

### 3. Strings — `session01/ex2_strings.py`
- [ ] Slicing `s[start:stop:step]`, negative indices, slices never raise
- [ ] Strings are immutable; methods return a new string
- [ ] `split()` vs `split(",")`, `partition`, `strip` vs `removeprefix`, `find` vs `index`
- [ ] `"".join(parts)` instead of `+=` in a loop; f-string format specs

### 4. Lists — `session01/ex3_lists.py`
- [ ] A list is a dynamic array of pointers; append O(1), `insert(0)`/`pop(0)` O(n)
- [ ] `sort()` returns `None` (in place) vs `sorted()` returns a new list
- [ ] `append` vs `extend`
- [ ] `key=lambda h: (-h[2], h[1])` multi-level sort; stable multi-pass sort for strings
- [ ] `x in list` is O(n)

### 5. Tuples and sets — `session01/ex4_tuples_sets.py`
- [ ] `(5,)`, unpacking, `a, *rest = xs`, swap, returning several values
- [ ] Tuples are hashable → dict keys; `NamedTuple` for records
- [ ] Set operations `| & - ^ <=`; `set()` not `{}`; `discard` vs `remove`
- [ ] ⚠️ GAP: a composite member must be a tuple: `seen.add((tenant, doc))`, not `update([...])`

### 6. Dictionaries — `session01/ex5_dicts.py`
- [ ] Hash table: hash → slot → probe; O(1) average; resize at 2/3; insertion order kept
- [ ] Keys must be hashable (why a list can't be a key)
- [ ] `get`, `setdefault`, `pop`, `update`, `items()`; `{**a, **b}` / `a | b` (shallow)

### 7. Decorators (fast track)
- [ ] `@d` means `f = d(f)`; the name is rebound to the wrapper; closure keeps the original
- [ ] ⚠️ GAP (your version had 3 bugs): `*args, **kwargs` · `return func(...)` · `@functools.wraps(func)`
- [ ] What `wraps` copies and why FastAPI needs it (signature → 422 errors without it)

### 8. Async — `session06/ex1_async.py`
- [ ] One thread, one event loop; `await` yields to the loop
- [ ] Sequential awaits (3s) vs `asyncio.gather` (1s)
- [ ] Never block inside `async def` (`time.sleep`, `requests`) → `asyncio.to_thread`
- [ ] Calling a coroutine without `await` does nothing (differs from JS)
- [ ] `create_task`, `Semaphore`, `asyncio.timeout`, `async for`
- [ ] ⏳ Quick-check questions not answered yet

### 9. Concurrency (concept level only)
- [ ] I/O-bound → asyncio/threads · CPU-bound → processes / queue + workers
- [ ] The GIL in two sentences
- [ ] ⏳ Quick-check questions not answered yet

### 10. Classes, dataclasses, Pydantic — `session03/`
- [ ] `__init__`, `self`, instance vs class attributes (shared mutable class attribute trap)
- [ ] `@property`, `@classmethod`, `@staticmethod`, `__repr__`
- [ ] Composition + `Protocol` (swap LLM providers without changing callers)
- [ ] `@dataclass`, `field(default_factory=list)`, `frozen=True`, `__post_init__`
- [ ] Pydantic: validation at boundaries, coercion, `Field(ge=, le=)`, `extra="forbid"`,
      nested models, `field_validator`, `model_validator`,
      `model_validate`, `model_validate_json`, `model_dump`, `model_json_schema`
- [ ] Dataclass for internal data, Pydantic for external data
- [ ] ⏳ Quick-check questions not answered yet

---

## B. Studied on your own (not verified yet) — `session02/`
- [ ] Functions, arguments, default / keyword / positional-only / keyword-only
- [ ] `*args` / `**kwargs`, unpacking
- [ ] Scope (LEGB), `global`, `nonlocal`, closures, late binding
- [ ] Lambda, recursion
- [ ] Generators (`yield`) — readiness-check Q1 was correct

Prove it: `uv run pytest session02 -q` and `python -m session02.ex1_predict`

---

## C. Not covered yet

Needed soon (short lessons planned):
- [ ] Comprehensions (list / dict / set / nested) — exercises exist: `session02/ex3`
- [ ] Exceptions: try/except/else/finally, custom hierarchy, `raise ... from` — `session02/ex4`
- [ ] Context managers: `with`, `__enter__`/`__exit__`, `contextlib`
- [ ] Type hints in depth: `Optional`, `|`, `Literal`, `TypedDict`, `Callable`, generics
- [ ] Modules, packages, `if __name__ == "__main__":`, imports, project structure
- [ ] `pytest`: fixtures, parametrize, mocking (you run it, but it hasn't been taught)
- [ ] HTTP clients: `httpx`, timeouts, retries
- [ ] Config and secrets: environment variables, `.env`
- [ ] Logging

Lower priority (learn when needed):
- [ ] Iterator protocol (`__iter__` / `__next__`), `send()`, `yield from`
- [ ] Dunder methods (`__eq__`, `__lt__`, `__len__`, `__call__` ...), enums
- [ ] File handling, `pathlib`, JSON / CSV
- [ ] `collections`, `itertools`, `functools` (`lru_cache`, `partial`)
- [ ] Regular expressions, `match` / `case`, debugging with `pdb`

---

## D. Exercises: none completed in the repo yet

| Folder | Tests | State |
|---|---|---|
| `session01/` strings, lists, tuples/sets, dicts | 46 | not started |
| `session02/` functions, comprehensions, exceptions | 29 | not started |
| `session03/` classes, dataclasses, Pydantic | 33 | not started |
| `session06/` async | 6 | not started |

Run everything: `uv run pytest -q` · one folder: `uv run pytest session01 -q --tb=short`
