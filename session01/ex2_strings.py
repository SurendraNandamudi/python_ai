"""Session 01 · Exercise 2 — Strings and text processing (OCR clean-up for NeuroDocx).

Run:  uv run pytest session01/tests/test_ex2_strings.py -v
Replace every `raise NotImplementedError` with your implementation.
"""


def normalize_chunk(text: str, max_len: int = 40) -> str:
    """Collapse all whitespace (incl. newlines) to single spaces and strip the ends.

    If the result is longer than max_len, cut at the LAST space before max_len and append "…".
    If there is no space to cut at, hard-cut at max_len and append "…".

    >>> normalize_chunk("The  quarterly\\n\\nrevenue grew   by 12% in the EMEA region", 30)
    'The quarterly revenue grew by…'
    """
    raise NotImplementedError


def parse_ocr_fields(raw: str) -> dict[str, str]:
    """Turn messy OCR "Key: Value" lines into a dict with snake_case keys.

    - skip blank lines and lines without a ':'
    - split on the FIRST ':' only (values may contain ':' e.g. times)
    - key: stripped, internal whitespace collapsed, lower-cased, spaces -> '_'
    - value: stripped, internal whitespace collapsed

    >>> parse_ocr_fields("  Invoice   No: INV-7\\n\\nTime:  10:30 ")
    {'invoice_no': 'INV-7', 'time': '10:30'}
    """
    raise NotImplementedError


def parse_amount(text: str) -> float:
    """Parse a currency string into a float.

    Handles an optional leading currency symbol ($, €, £), thousands separators and spaces.
    >>> parse_amount(" $1,250.00 ")
    1250.0
    >>> parse_amount("€ 3,000")
    3000.0
    """
    raise NotImplementedError


def mask_email(email: str) -> str:
    """PII masking before text is sent to an LLM: keep the first char of the local part,
    replace the rest of the local part with '***', keep the domain.

    >>> mask_email("surendra@neurodocx.com")
    's***@neurodocx.com'
    If there is no '@', return the input unchanged.
    """
    raise NotImplementedError


def build_prompt(question: str, chunks: list[str]) -> str:
    """Build a grounded-RAG prompt. Exact format (note the numbering starts at 1):

    Answer using ONLY the context below.

    Context:
    [1] first chunk
    [2] second chunk

    Question: <question>

    Hint: build a list of lines and "\\n".join() them — do not += strings in a loop.
    """
    raise NotImplementedError
