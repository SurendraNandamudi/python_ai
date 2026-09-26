"""Session 01 · Exercise 3 — Lists, sorting with key functions, slicing.

Run:  uv run pytest session01/tests/test_ex3_lists.py -v

A hit is a tuple: (doc_id: str, chunk_id: int, score: float)
"""

Hit = tuple[str, int, float]


def top_k(hits: list[Hit], k: int) -> list[Hit]:
    """Highest score first; ties broken by chunk_id ascending. Must NOT modify `hits`."""
    raise NotImplementedError


def rank_doc_then_chunk(hits: list[Hit]) -> list[Hit]:
    """Score descending; ties by doc_id A→Z; then chunk_id DESCENDING. Must NOT modify `hits`."""
    raise NotImplementedError


def rank_doc_desc(hits: list[Hit]) -> list[Hit]:
    """Score descending; ties by doc_id Z→A (strings can't be negated!); then chunk_id ascending.

    Hint: sort is STABLE — sort several times, least important key first.
    """
    raise NotImplementedError


def dedupe_keep_order(ids: list[str]) -> list[str]:
    """Remove duplicates, keep first-seen order. Must be O(n), not O(n²)."""
    raise NotImplementedError


def batched(items: list, size: int) -> list[list]:
    """Split into batches of `size` (last one may be shorter) — e.g. to send chunks to an
    embedding API that accepts max N inputs per call. Raise ValueError if size < 1.

    >>> batched([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]
    """
    raise NotImplementedError


def sliding_windows(tokens: list[str], size: int, overlap: int) -> list[list[str]]:
    """Chunking with overlap — the core of RAG chunkers.
    step = size - overlap. Windows start at 0, step, 2*step, ... and stop once a window
    reaches the end of the list (the last window may be shorter). Empty input -> [].
    Raise ValueError if not (0 <= overlap < size).

    >>> sliding_windows(list("abcdefg"), size=3, overlap=1)
    [['a', 'b', 'c'], ['c', 'd', 'e'], ['e', 'f', 'g']]
    """
    raise NotImplementedError
