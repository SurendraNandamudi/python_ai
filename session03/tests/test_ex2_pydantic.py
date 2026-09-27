import json

import pytest
from pydantic import ValidationError

from session03.ex2_pydantic import AskRequest, Invoice, invoice_schema_fields, parse_llm_invoice


class TestAskRequest:
    def test_defaults_and_strip(self):
        r = AskRequest.model_validate({"question": "  What is the total?  "})
        assert r.question == "What is the total?"
        assert r.top_k == 5
        assert r.doc_ids == []

    def test_coerces_numeric_string(self):
        assert AskRequest.model_validate({"question": "q", "top_k": "3"}).top_k == 3

    @pytest.mark.parametrize("payload", [
        {},
        {"question": "   "},
        {"question": "q", "top_k": 0},
        {"question": "q", "top_k": 21},
        {"question": "q", "top_k": "three"},
        {"question": None},
        {"question": "q", "tenant_id": "t2"},
    ])
    def test_rejects(self, payload):
        with pytest.raises(ValidationError):
            AskRequest.model_validate(payload)


GOOD = {
    "invoice_no": "inv-42",
    "currency": "EUR",
    "lines": [
        {"description": "Consulting", "quantity": 2, "unit_price": 100.0},
        {"description": "Travel", "quantity": 1, "unit_price": 50.5},
    ],
    "total": 250.5,
}


class TestInvoice:
    def test_valid_and_normalised(self):
        inv = Invoice.model_validate(GOOD)
        assert inv.invoice_no == "INV-42"
        assert inv.lines[1].unit_price == 50.5
        assert inv.model_dump()["currency"] == "EUR"

    @pytest.mark.parametrize(("patch", "fragment"), [
        ({"invoice_no": "42"}, "invoice_no"),
        ({"currency": "INR"}, "currency"),
        ({"lines": []}, "lines"),
        ({"total": 999.0}, "total"),
    ])
    def test_invalid(self, patch, fragment):
        with pytest.raises(ValidationError) as info:
            Invoice.model_validate({**GOOD, **patch})
        assert fragment in str(info.value)

    def test_nested_line_validation(self):
        bad = {**GOOD, "lines": [{"description": "x", "quantity": 0, "unit_price": 1}]}
        with pytest.raises(ValidationError):
            Invoice.model_validate(bad)


class TestParseLlmInvoice:
    def test_ok(self):
        inv, errors = parse_llm_invoice(json.dumps(GOOD))
        assert errors == []
        assert inv is not None and inv.total == 250.5

    def test_nested_error_location(self):
        bad = {**GOOD, "lines": [{"description": "x", "quantity": 0, "unit_price": 1}], "total": 0}
        inv, errors = parse_llm_invoice(json.dumps(bad))
        assert inv is None
        assert any(e.startswith("lines.0.quantity:") for e in errors)

    def test_model_level_error(self):
        inv, errors = parse_llm_invoice(json.dumps({**GOOD, "total": 1.0}))
        assert inv is None
        assert any("total" in e for e in errors)

    def test_invalid_json_does_not_raise(self):
        inv, errors = parse_llm_invoice("Sure! Here is the invoice: {oops")
        assert inv is None
        assert errors


def test_invoice_schema_fields():
    assert invoice_schema_fields() == ["currency", "invoice_no", "lines", "total"]
