"""Session 01 · Exercise 4 — Tuples, NamedTuple, sets (hybrid search + tenant safety).

Run:  uv run pytest session01/tests/test_ex4_tuples_sets.py -v
"""

from typing import NamedTuple


class Hit(NamedTuple):
    doc_id: str
    chunk_id: int
    score: float


def to_hits(rows: list[tuple[str, int, float]]) -> list[Hit]:
    """Convert raw tuples into Hit named tuples (use unpacking)."""
    raise NotImplementedError


def min_max_score(hits: list[Hit]) -> tuple[float, float]:
    """Return (lowest score, highest score). Raise ValueError on an empty list."""
    raise NotImplementedError


def hybrid_merge(vector_ids: set[str], keyword_ids: set[str]) -> dict[str, list[str]]:
    """Compare two retrievers. Return a dict with SORTED lists:
      "candidates"    -> in either
      "agreed"        -> in both
      "vector_only"   -> only in vector_ids
      "keyword_only"  -> only in keyword_ids
      "disagreement"  -> in exactly one of them
    """
    raise NotImplementedError


def mark_seen(seen: set[tuple[str, str]], tenant_id: str, doc_id: str) -> bool:
    """Record (tenant_id, doc_id) in `seen` (mutate it). Return True if it was NEW,
    False if already seen. The same doc_id under a different tenant is a DIFFERENT item."""
    raise NotImplementedError


def can_read(user_roles: set[str], allowed_roles: set[str]) -> bool:
    """True if the user has at least one allowed role."""
    raise NotImplementedError


def has_all_scopes(token_scopes: set[str], required: set[str]) -> bool:
    """True if the token has EVERY required scope. (One operator.)"""
    raise NotImplementedError
