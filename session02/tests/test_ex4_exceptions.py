import pytest

from session02.ex4_exceptions import (
    DocumentError, DocumentNotFound, ExtractionFailed, load_document, parse_page_count, process_batch, safe_extract,
)


def test_hierarchy():
    assert issubclass(DocumentNotFound, DocumentError)
    assert issubclass(ExtractionFailed, DocumentError)
    assert issubclass(DocumentError, Exception)


def test_document_not_found_message_and_attr():
    err = DocumentNotFound("d9")
    assert err.doc_id == "d9"
    assert str(err) == "document 'd9' not found"


class TestParsePageCount:
    def test_ok(self):
        assert parse_page_count(" 12 ") == 12

    def test_invalid_is_chained(self):
        with pytest.raises(ValueError, match="invalid page count: 'twelve'") as info:
            parse_page_count("twelve")
        assert isinstance(info.value.__cause__, ValueError)

    def test_negative(self):
        with pytest.raises(ValueError, match="cannot be negative"):
            parse_page_count("-3")


def test_load_document():
    assert load_document({"d1": "text"}, "d1") == "text"
    with pytest.raises(DocumentNotFound) as info:
        load_document({}, "d9")
    assert isinstance(info.value.__cause__, KeyError)


class TestSafeExtract:
    def test_success(self):
        assert safe_extract(str.upper, "abc") == ("ABC", None)

    def test_domain_error_is_captured(self):
        def bad(_doc):
            raise ExtractionFailed("no text layer")

        assert safe_extract(bad, "x") == (None, "ExtractionFailed: no text layer")

    def test_bugs_propagate(self):
        def buggy(_doc):
            raise TypeError("bug")

        with pytest.raises(TypeError):
            safe_extract(buggy, "x")


def test_process_batch():
    store = {"d1": "a", "d3": "c"}
    assert process_batch(store, ["d1", "d2", "d3", "d4"]) == {"ok": ["d1", "d3"], "missing": ["d2", "d4"]}
