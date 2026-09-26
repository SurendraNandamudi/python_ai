"""Session 01 · Exercise 5 — Dictionaries.

Run:  uv run pytest session01/tests/test_ex5_dicts.py -v
Do NOT use collections (Counter/defaultdict) yet — that is session 7. Plain dicts only.
"""

from typing import Any

Chunk = dict[str, str]


def build_index(chunks: list[Chunk]) -> dict[tuple[str, str], list[str]]:
    """Group chunk texts by (tenant, doc), keeping input order. One loop + setdefault.

    index[("t1", "d1")] -> ["Revenue grew 12%", "EMEA led growth"]
    """
    raise NotImplementedError


def word_count(text: str) -> dict[str, int]:
    """Case-insensitive word frequency. Words = text.lower().split(). Use dict.get."""
    raise NotImplementedError


def top_words(counts: dict[str, int], n: int) -> list[tuple[str, int]]:
    """n most frequent (word, count) pairs; ties broken alphabetically."""
    raise NotImplementedError


def merge_config(defaults: dict, overrides: dict) -> dict:
    """Shallow merge, overrides win, inputs NOT modified. One expression."""
    raise NotImplementedError


def deep_merge(base: dict, override: dict) -> dict:
    """Like merge_config, but when BOTH values for a key are dicts, merge them recursively.
    Inputs must NOT be modified.

    >>> deep_merge({"llm": {"model": "a", "temp": 0.2}}, {"llm": {"temp": 0}})
    {'llm': {'model': 'a', 'temp': 0}}
    """
    raise NotImplementedError


def get_path(data: dict, path: str, default: Any = None) -> Any:
    """Safe nested lookup with a dotted path — Python's answer to JS `a?.b?.c ?? default`.

    get_path(doc, "meta.lang", "en")
    Return default if any level is missing or is not a dict.
    Careful: a stored value of 0 / "" / False must be returned, NOT replaced by default.
    """
    raise NotImplementedError


def invert(d: dict[str, str]) -> dict[str, list[str]]:
    """Invert a mapping; values become keys, collecting ALL original keys (sorted).

    >>> invert({"d1": "t1", "d2": "t2", "d3": "t1"})
    {'t1': ['d1', 'd3'], 't2': ['d2']}
    """
    raise NotImplementedError
