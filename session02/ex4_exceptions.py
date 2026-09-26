"""Session 02 · Exercise 4 — Exceptions: custom hierarchy, chaining, precise handling.

Run:  uv run pytest session02/tests/test_ex4_exceptions.py -v
"""


# 1. Build this hierarchy:
#    DocumentError(Exception)            — base for everything in our service
#    ├── DocumentNotFound(DocumentError) — has a `.doc_id` attribute;
#    │                                      str(err) == "document 'd9' not found"
#    └── ExtractionFailed(DocumentError) — plain subclass
class DocumentError(Exception):
    pass


class DocumentNotFound(DocumentError):
    pass  # TODO: __init__(self, doc_id) storing doc_id and setting the message


class ExtractionFailed(DocumentError):
    pass


def parse_page_count(value: str) -> int:
    """Parse a page count from OCR text like " 12 ".
    Non-integer text -> ValueError("invalid page count: '<original value>'") chained FROM
    the original error. Negative numbers -> ValueError("page count cannot be negative")."""
    raise NotImplementedError


def load_document(store: dict[str, str], doc_id: str) -> str:
    """Return store[doc_id]. A missing key must raise DocumentNotFound(doc_id)
    with the original KeyError as its __cause__ (use `raise ... from ...`)."""
    raise NotImplementedError


def safe_extract(extractor, doc: str) -> tuple[str | None, str | None]:
    """Call extractor(doc).
    - success                 -> (result, None)
    - any DocumentError       -> (None, "<ExceptionClassName>: <message>")
    - ANY OTHER exception     -> must propagate (do NOT swallow bugs like TypeError)"""
    raise NotImplementedError


def process_batch(store: dict[str, str], doc_ids: list[str]) -> dict[str, list[str]]:
    """Load every doc; never stop the batch because one doc is missing.
    Return {"ok": [ids loaded], "missing": [ids not found]} in input order."""
    raise NotImplementedError
