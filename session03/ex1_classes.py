"""Session 03 · Exercise 1 — Classes, dataclasses, composition.

Run:  uv run pytest session03/tests/test_ex1_classes.py -v
"""

from dataclasses import dataclass, field
from typing import Protocol


class DocumentStore:
    """A tiny per-tenant document store.

    - MAX_DOCS = 3 is a CLASS attribute (shared limit)
    - each instance has its OWN docs (beware the shared-mutable class attribute trap!)
    - add(doc_id, text): raise ValueError("store is full") if already MAX_DOCS docs
    - get(doc_id): return the text; missing -> KeyError
    - `count` is a read-only PROPERTY (store.count, no parentheses)
    - len(store) works  (__len__)
    - repr(store) == "DocumentStore(tenant='t1', docs=2)"
    - DocumentStore.for_demo() classmethod returns a store for tenant "demo"
    - DocumentStore.is_pdf("a.PDF") staticmethod -> True
    """

    MAX_DOCS = 3

    def __init__(self, tenant_id: str) -> None:
        raise NotImplementedError


@dataclass
class Chunk:
    """A chunk of a document. Make it:
    - FROZEN (immutable: assigning chunk.text = ... raises dataclasses.FrozenInstanceError)
    - fields: doc_id: str, index: int, text: str, tags: tuple[str, ...] = ()   (tuple: frozen-friendly)
    - __post_init__: raise ValueError if index < 0 or text is empty/whitespace
    - property word_count -> number of words in text
    Two chunks with the same fields must be == and usable as set members / dict keys.
    """

    doc_id: str = ""  # TODO: replace this placeholder body with the real frozen dataclass


class LLMProvider(Protocol):
    async def complete(self, prompt: str) -> str: ...


class Summarizer:
    """COMPOSITION: a Summarizer HAS-A provider and works with ANY object that has
    `async def complete(prompt) -> str`.

    summarize(text) must call the provider with exactly  "Summarise:\\n" + text.strip()
    and return its reply stripped. Empty/whitespace text -> ValueError, without calling the provider.
    """

    def __init__(self, llm: LLMProvider) -> None:
        raise NotImplementedError

    async def summarize(self, text: str) -> str:
        raise NotImplementedError
