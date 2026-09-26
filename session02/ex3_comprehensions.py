"""Session 02 · Exercise 3 — Comprehensions. Every function body should be ONE comprehension
(a `return` statement), no explicit loops.

Run:  uv run pytest session02/tests/test_ex3_comprehensions.py -v
"""


def flatten(nested: list[list]) -> list:
    """[[1, 2], [3], []] -> [1, 2, 3]"""
    raise NotImplementedError


def long_chunk_lengths(chunks: dict[str, str], min_len: int) -> dict[str, int]:
    """{chunk_id: text} -> {chunk_id: len(text)} keeping only texts with len >= min_len."""
    raise NotImplementedError


def email_domains(emails: list[str]) -> set[str]:
    """Unique lower-cased domains of the emails that contain '@'."""
    raise NotImplementedError


def transpose(matrix: list[list]) -> list[list]:
    """[[1, 2, 3], [4, 5, 6]] -> [[1, 4], [2, 5], [3, 6]]  (nested comprehension; no zip)"""
    raise NotImplementedError


def label_scores(scores: list[float], threshold: float) -> list[str]:
    """Map each score to "relevant" if >= threshold else "noise" (conditional EXPRESSION
    inside the comprehension — not a filter)."""
    raise NotImplementedError


def tenant_doc_map(rows: list[tuple[str, str]]) -> dict[str, list[str]]:
    """[(tenant, doc), ...] -> {tenant: sorted unique docs}. One dict comprehension
    (a nested comprehension inside it is fine)."""
    raise NotImplementedError
