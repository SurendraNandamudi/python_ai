"""Session 02 · Exercise 1 — Functions, scope & exceptions: PREDICT-THEN-RUN.

Write your prediction in each `# PREDICT:` BEFORE running:
    uv run python -m session02.ex1_predict
For each miss, write one line in `# WHY:`.
"""


def block(title: str) -> None:
    print(f"\n--- {title} ---")


block("F1 LEGB")
x = "global"


def outer():
    x = "enclosing"

    def inner():
        return x

    return inner()


print(outer(), x)
# PREDICT:
# WHY:

block("F2 UnboundLocalError")
count = 0


def bump():
    try:
        count += 1  # noqa: F823 — intentional
    except UnboundLocalError as e:
        return f"UnboundLocalError: {e}"
    return count


print(bump())
# PREDICT:
# WHY:

block("F3 nonlocal counter")


def make_counter():
    n = 0

    def inc():
        nonlocal n
        n += 1
        return n

    return inc


c1, c2 = make_counter(), make_counter()
print(c1(), c1(), c2())
# PREDICT:
# WHY:

block("F4 late-binding closures")
fns = [lambda: i for i in range(3)]
print([f() for f in fns])
# PREDICT:
# WHY:

block("F5 *args / **kwargs")


def show(a, *args, b=2, **kwargs):
    return a, args, b, kwargs


print(show(1, 2, 3, b=4, c=5))
print(show(*[1, 2], **{"b": 9}))
# PREDICT:
# WHY:

block("F6 keyword-only")


def ask(question, *, top_k=5):
    return question, top_k


try:
    print(ask("q", 3))
except TypeError as e:
    print("TypeError:", e)
# PREDICT:
# WHY:

block("F7 functions are objects")


def greet(name):
    """Say hi."""
    return f"hi {name}"


alias = greet
print(alias("tenant"), alias.__name__, greet.__doc__, callable(greet))
# PREDICT:
# WHY:

block("F8 try / except / else / finally order")


def flow(n):
    out = []
    try:
        out.append("try")
        1 / n
    except ZeroDivisionError:
        out.append("except")
    else:
        out.append("else")
    finally:
        out.append("finally")
    return out


print(flow(1), flow(0))
# PREDICT:
# WHY:

block("F9 return inside finally")


def sneaky():
    try:
        return "from try"
    finally:
        return "from finally"  # noqa: B012 — intentional; Python 3.14 even warns about this (PEP 765)


print(sneaky())
# PREDICT:
# WHY:

block("F10 exception chaining")
try:
    try:
        {}["doc-9"]
    except KeyError as e:
        raise LookupError("document missing") from e
except LookupError as err:
    print(type(err).__name__, "| cause:", repr(err.__cause__))
# PREDICT:
# WHY:

block("F11 comprehension scope")
y = 10
squares = [y * y for y in range(3)]
print(squares, y)
# PREDICT:
# WHY:
