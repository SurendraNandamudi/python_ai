# Session 01 — Revision sheet

## Memory model (the one picture)
- **Names** are labels → they point at **objects** (every value is an object: int, None, functions).
- `y = x` → second arrow to the **same** object. Nothing copied.
- Assignment **moves an arrow**. Mutation (`append`, `d[k] = v`, `+=` on a list) **changes the box** — every arrow to it sees it.
- Mutable: `list dict set` · Immutable: `int float bool str tuple frozenset None`
- `+=` → in-place on mutable (`__iadd__`), new object + rebind on immutable.
- Copies copy **arrows**: `lst[:]`, `.copy()`, `list()`, `dict()`, `{**d}`, `[x] * n` are all SHALLOW. `copy.deepcopy` copies boxes all the way down.
- Traps: `[[0]*3]*2` · `dict.fromkeys(keys, [])` · `def f(x, acc=[])` (default evaluated ONCE at def time → use `None`).

## Types & operators
- Dynamic **and strong**: `"1" + 1` → TypeError; `1 == "1"` → False (no coercion).
- `bool` subclasses `int`: `True + True == 2`; `{1, 1.0, True}` → `{1}`.
- `7 // 2 = 3`, `-7 // 2 = -4` (floor), `-7 % 2 = 1`, `round(2.5) = 2` (banker's), `0.1 + 0.2 != 0.3` → `math.isclose`.
- Falsy: `None False 0 0.0 "" [] () {} set() range(0)`. **Unlike JS: `[]`/`{}` falsy, `NaN` truthy.**
- `and`/`or` return an operand. **No `??`** → `x if x is not None else default` (`x or default` breaks on 0/"").
- `==` value (`__eq__`, overridable) · `is` identity (same object). Use `is` only for `None`/singletons.
- Chained: `1 < x < 10`. `not a == b` = `not (a == b)`. `-2**2 == -4`.
- Missing key/attr → **KeyError / AttributeError** (Python fails loudly where JS gives `undefined`).

## Strings (immutable)
- Slicing `s[start:stop:step]`: stop excluded; negatives count from end; slices clamp (never raise), indexing raises.
- `s[::-1]` reverse. Every method returns a NEW string → rebind: `s = s.strip()`.
- `split()` (no arg) = any whitespace, drops empties · `split(",")` keeps empties.
- `partition(":")` → always 3 parts, splits at first. `find` → -1, `index` → ValueError.
- `strip(chars)` strips a character SET; `removeprefix` strips an exact prefix.
- Build big strings with `"".join(parts)`, never `+=` in a loop.
- f-strings: `f"{x:,.2f}"`, `f"{x!r}"`, `f"{x=}"`, `f"{p:.1%}"`. Raw strings `r"\d+"` for regex.

## Lists (dynamic array of pointers)
| O(1) | O(n) | O(n log n) |
|---|---|---|
| `lst[i]`, `append`, `pop()`, `len` | `insert(0,x)`, `pop(0)`, `x in lst`, `remove`, `index` | `sort`, `sorted` |
- In-place methods return **None** (`sort`, `reverse`, `append`, `extend`). `lst = lst.sort()` → None.
- `sorted()` → new list, any iterable. `key=` can return a tuple → multi-level sort; negate numbers for descending.
- Strings can't be negated → stable multi-pass sort (least important key first).
- `append([a,b])` adds ONE element; `extend([a,b])` adds two.
- Queue from the front → `collections.deque` (`popleft` O(1)).

## Tuples
- `(5,)` single element — the comma makes it. Unpacking: `a, *rest = xs`, swap `a, b = b, a`.
- Immutable (shallowly!) + hashable (if contents are) → dict keys / set members: `cache[(tenant, doc)]`.
- Records: `typing.NamedTuple` → `h.score` instead of `h[2]`.

## Sets (hash-based, unique, unordered)
- `set()` is empty set; `{}` is an empty DICT.
- `| & - ^` = union, intersection, difference, symmetric diff; `<=` subset.
- `x in s` O(1). `discard` (silent) vs `remove` (KeyError).
- Members must be hashable → use tuples for composite identity: `seen.add((tenant, doc))`, never `update([tenant, doc])`.
- Dedupe keeping order: `list(dict.fromkeys(xs))`.

## Dicts (compact hash table)
- `hash(key)` → slot → probe until key found or empty slot → O(1) average, O(n) worst.
- Resizes at 2/3 full (amortised O(1) insert). Insertion order preserved (dense entries array).
- Keys must be hashable (hash must never change) → no list keys.
- `get(k, default)`, `setdefault(k, []).append(x)`, `pop(k, None)`, `popitem()` (LIFO), `update()`.
- Views: `keys() values() items()` are live.
- Merge: `{**a, **b}` / `a | b` — right wins, SHALLOW.
- Nested safe access: `d.get("meta", {}).get("lang", "en")`.

## Open gaps to revisit
- [ ] `[row] * n` repetition copies references (P2)
- [ ] Composite set members need a tuple (T3)
- [ ] Exercises skipped in class: `normalize_chunk`, `top_k` (now in `session01/`)
