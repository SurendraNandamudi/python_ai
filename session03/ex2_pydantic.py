"""Session 03 · Exercise 2 — Pydantic at the boundaries (API input + LLM output).

Run:  uv run pytest session03/tests/test_ex2_pydantic.py -v
"""

from typing import Literal  # noqa: F401  (you will need it)

from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator, model_validator  # noqa: F401


class AskRequest(BaseModel):
    """Body of POST /documents/{id}/ask
    - question: str, surrounding whitespace stripped, must not be empty after stripping
    - top_k: int, default 5, between 1 and 20 inclusive
    - doc_ids: list[str], default empty list
    - unknown fields (e.g. tenant_id!) must be REJECTED
    """


class InvoiceLine(BaseModel):
    """description: str · quantity: int >= 1 · unit_price: float >= 0"""


class Invoice(BaseModel):
    """What we ask the LLM to extract from an invoice.
    - invoice_no: str matching ^INV-\\d+$ ; lower-case input like "inv-42" must be accepted
      and stored upper-cased (hint: field_validator(mode="before") or normalise first)
    - currency: exactly one of "USD", "EUR", "GBP"
    - lines: list[InvoiceLine], at least one
    - total: float, must equal sum(quantity * unit_price) within 0.01
      else ValueError whose message contains "total"
    """


def parse_llm_invoice(raw_json: str) -> tuple[Invoice | None, list[str]]:
    """Validate an LLM's raw JSON reply.
    Success -> (invoice, [])
    Failure -> (None, ["<dotted.location>: <message>", ...]) — ready to send BACK to the LLM
    so it can fix its answer. Location for nested errors looks like "lines.0.quantity".
    For model-level errors (no field), use just the message.
    Invalid JSON must also come back as (None, [...]) — never raise.
    """
    raise NotImplementedError


def invoice_schema_fields() -> list[str]:
    """Return the sorted list of REQUIRED top-level field names from Invoice's JSON schema
    (this schema is what you send to the LLM as the required output format)."""
    raise NotImplementedError
