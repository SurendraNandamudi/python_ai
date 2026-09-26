import pytest

from session01.ex2_strings import build_prompt, mask_email, normalize_chunk, parse_amount, parse_ocr_fields


class TestNormalizeChunk:
    def test_example(self):
        text = "The  quarterly\n\nrevenue grew   by 12% in the EMEA region"
        assert normalize_chunk(text, 30) == "The quarterly revenue grew by…"

    def test_short_text_untouched_except_whitespace(self):
        assert normalize_chunk("  hello \t\n world  ") == "hello world"

    def test_exact_length_is_not_cut(self):
        assert normalize_chunk("abcde", 5) == "abcde"

    def test_no_space_hard_cut(self):
        assert normalize_chunk("a" * 50, 10) == "a" * 10 + "…"

    def test_empty(self):
        assert normalize_chunk("   \n ") == ""


class TestParseOcrFields:
    def test_basic(self):
        raw = """  INVOICE   No: INV-2024-0042
Date:  12/03/2024

   Total Amount :  $1,250.00
"""
        assert parse_ocr_fields(raw) == {
            "invoice_no": "INV-2024-0042",
            "date": "12/03/2024",
            "total_amount": "$1,250.00",
        }

    def test_splits_on_first_colon_only(self):
        assert parse_ocr_fields("Time:  10:30:15") == {"time": "10:30:15"}

    def test_skips_lines_without_colon(self):
        assert parse_ocr_fields("HEADER LINE\nKey: v") == {"key": "v"}


@pytest.mark.parametrize(
    ("text", "expected"),
    [(" $1,250.00 ", 1250.0), ("€ 3,000", 3000.0), ("£12.5", 12.5), ("42", 42.0)],
)
def test_parse_amount(text, expected):
    assert parse_amount(text) == expected


def test_parse_amount_invalid_raises():
    with pytest.raises(ValueError):
        parse_amount("N/A")


@pytest.mark.parametrize(
    ("email", "expected"),
    [
        ("surendra@neurodocx.com", "s***@neurodocx.com"),
        ("a@b.io", "a***@b.io"),
        ("not-an-email", "not-an-email"),
    ],
)
def test_mask_email(email, expected):
    assert mask_email(email) == expected


def test_build_prompt():
    expected = (
        "Answer using ONLY the context below.\n"
        "\n"
        "Context:\n"
        "[1] Revenue grew 12%\n"
        "[2] EMEA led growth\n"
        "\n"
        "Question: Why did revenue grow?"
    )
    assert build_prompt("Why did revenue grow?", ["Revenue grew 12%", "EMEA led growth"]) == expected
