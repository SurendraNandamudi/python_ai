"""Session 01 · Exercise 1 — Memory model: names point to objects.

PREDICT-THEN-RUN. For each block:
  1. Draw the names → objects picture on paper.
  2. Write your prediction in the `# PREDICT:` comment.
  3. Only then run:  python -m session01.ex1_memory
  4. For every wrong prediction, write one line in `# WHY:` explaining the arrows.

The rule behind everything here:
  Assignment moves a name's arrow. Mutation changes the box. Copies copy arrows, not boxes.
"""

import copy


def block(title: str) -> None:
    print(f"\n--- {title} ---")


# ---------------------------------------------------------------- warm-up (seen in class)
block("A1 aliasing")
x = [1, 2]
y = x
y.append(3)
y = [7]
print(x, y)
# PREDICT:
# WHY:

block("A2 += on list vs int")
a = [1, 2]
b = a
b += [3]
n = 10
m = n
m += 1
print(a, n)
# PREDICT:
# WHY:

block("A3 list * repetition")
grid = [[0] * 3] * 2
grid[0][0] = 1
print(grid)
# PREDICT:
# WHY:


# ---------------------------------------------------------------- new ones
block("B1 b = b + [...] instead of +=")
a = [1, 2]
b = a
b = b + [3]
print(a, b, a is b)
# PREDICT:
# WHY:

block("B2 tuple holding a list")
t = ("d1", ["pdf"])
t[1].append("ocr")
print(t)
try:
    hash(t)
except TypeError as e:
    print("TypeError:", e)
# PREDICT:
# WHY:

block("B3 shallow dict copy of nested metadata")
meta = {"tags": ["pdf"], "pages": 3}
snap = meta.copy()
snap["pages"] = 99
snap["tags"].append("ocr")
print(meta)
# PREDICT:
# WHY:

block("B4 deepcopy")
meta = {"tags": ["pdf"], "pages": 3}
snap = copy.deepcopy(meta)
snap["tags"].append("ocr")
print(meta["tags"], snap["tags"])
# PREDICT:
# WHY:

block("B5 == vs is")
p = [1, 2]
q = [1, 2]
r = p
print(p == q, p is q, r is p)
# PREDICT:
# WHY:

block("B6 dict.fromkeys trap")
cache = dict.fromkeys(["t1", "t2"], [])
cache["t1"].append("doc-9")
print(cache)
# PREDICT:
# WHY:

block("B7 the `or` default bug")
payload = {"temperature": 0, "top_k": None}
temp = payload.get("temperature") or 0.7
top_k = payload.get("top_k") or 5
print(temp, top_k)
# PREDICT:
# WHY:


def add_chunk(chunk, batch=[]):  # noqa: B006 — intentional bug for the exercise
    batch.append(chunk)
    return batch


block("B8 mutable default argument")
r1 = add_chunk("a")
r2 = add_chunk("b")
print(r1, r2, r1 is r2)
# PREDICT:
# WHY:

block("B9 bool is an int")
print(True + True, {1: "int", True: "bool", 1.0: "float"})
# PREDICT:
# WHY:
