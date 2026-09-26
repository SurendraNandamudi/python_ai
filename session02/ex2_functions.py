"""Session 02 · Exercise 2 — Functions, parameters, closures, higher-order functions.

Run:  uv run pytest session02/tests/test_ex2_functions.py -v
"""

from collections.abc import Callable
from typing import Any


def build_request(prompt, model="gpt-5-mini", temperature=0.2, **extra):
    """Build an LLM request payload dict: {"prompt", "model", "temperature", **extra}.

    CHANGE THE SIGNATURE so that:
      - `prompt` is POSITIONAL-ONLY          (build_request(prompt="x") -> TypeError)
      - model/temperature are KEYWORD-ONLY   (build_request("x", "m")   -> TypeError)
      - any extra keyword args (e.g. max_tokens=512) are passed through into the dict
    """
    raise NotImplementedError


def merge_all(*dicts: dict, **overrides: Any) -> dict:
    """Merge any number of dicts left to right, then apply keyword overrides last.

    merge_all({"a": 1}, {"a": 2, "b": 3}, b=9)  ->  {"a": 2, "b": 9}
    """
    raise NotImplementedError


def make_counter(start: int = 0) -> Callable[[], int]:
    """Return a function that returns start+1, start+2, ... on each call (closure + nonlocal).
    Two counters must be independent."""
    raise NotImplementedError


def make_multipliers(n: int) -> list[Callable[[int], int]]:
    """Return n functions where the i-th multiplies its argument by i.

    make_multipliers(3)[2](10) -> 20
    Beware the late-binding closure trap (see ex1 F4).
    """
    raise NotImplementedError


def pipeline(*steps: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Compose functions LEFT to RIGHT: pipeline(f, g, h)(x) == h(g(f(x))).
    pipeline() with no steps returns the identity function."""
    raise NotImplementedError


def retry(fn: Callable[[], Any], attempts: int = 3,
          exceptions: tuple[type[BaseException], ...] = (Exception,)) -> Any:
    """Call fn() up to `attempts` times. Return the first successful result.
    Only exceptions in `exceptions` trigger a retry; any other exception propagates immediately.
    If every attempt fails, re-raise the LAST exception.
    (No sleeping/backoff here — that comes with httpx in session 7.)"""
    raise NotImplementedError


def apply_to_all(fn: Callable[[Any], Any], items: list, **kwargs: Any) -> list:
    """Call fn(item, **kwargs) for every item and return the results (keyword forwarding).

    apply_to_all(round, [1.234, 5.678], ndigits=1) -> [1.2, 5.7]
    """
    raise NotImplementedError
