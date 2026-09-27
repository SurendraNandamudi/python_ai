import asyncio
import dataclasses

import pytest

from session03.ex1_classes import Chunk, DocumentStore, Summarizer


class TestDocumentStore:
    def test_add_get_count_len_repr(self):
        s = DocumentStore("t1")
        s.add("d1", "hello")
        s.add("d2", "world")
        assert s.get("d1") == "hello"
        assert s.count == 2
        assert len(s) == 2
        assert repr(s) == "DocumentStore(tenant='t1', docs=2)"

    def test_count_is_a_property(self):
        assert isinstance(DocumentStore.__dict__.get("count"), property)

    def test_instances_are_independent(self):
        a, b = DocumentStore("t1"), DocumentStore("t2")
        a.add("d1", "x")
        assert b.count == 0

    def test_full_store(self):
        s = DocumentStore("t1")
        for i in range(DocumentStore.MAX_DOCS):
            s.add(f"d{i}", "x")
        with pytest.raises(ValueError, match="full"):
            s.add("extra", "x")

    def test_missing(self):
        with pytest.raises(KeyError):
            DocumentStore("t1").get("nope")

    def test_classmethod_and_staticmethod(self):
        assert DocumentStore.for_demo().tenant_id == "demo"
        assert DocumentStore.is_pdf("Report.PDF") is True
        assert DocumentStore.is_pdf("notes.txt") is False


class TestChunk:
    def test_fields_and_word_count(self):
        c = Chunk("d1", 0, "revenue grew twelve percent")
        assert c.word_count == 4
        assert c.tags == ()

    def test_frozen(self):
        c = Chunk("d1", 0, "text")
        with pytest.raises(dataclasses.FrozenInstanceError):
            c.text = "changed"

    def test_equality_and_hashable(self):
        a, b = Chunk("d1", 0, "x", ("pdf",)), Chunk("d1", 0, "x", ("pdf",))
        assert a == b
        assert len({a, b}) == 1

    @pytest.mark.parametrize(("index", "text"), [(-1, "x"), (0, "   ")])
    def test_post_init_validation(self, index, text):
        with pytest.raises(ValueError):
            Chunk("d1", index, text)


class FakeLLM:
    def __init__(self):
        self.prompts = []

    async def complete(self, prompt: str) -> str:
        self.prompts.append(prompt)
        return "  A short summary.  "


def test_summarizer_uses_any_provider():
    llm = FakeLLM()
    result = asyncio.run(Summarizer(llm).summarize("  Long invoice text  "))
    assert result == "A short summary."
    assert llm.prompts == ["Summarise:\nLong invoice text"]


def test_summarizer_rejects_empty_without_calling():
    llm = FakeLLM()
    with pytest.raises(ValueError):
        asyncio.run(Summarizer(llm).summarize("   "))
    assert llm.prompts == []
