import copy

from session01.ex5_dicts import build_index, deep_merge, get_path, invert, merge_config, top_words, word_count

CHUNKS = [
    {"tenant": "t1", "doc": "d1", "text": "Revenue grew 12%"},
    {"tenant": "t2", "doc": "d7", "text": "Invoice overdue"},
    {"tenant": "t1", "doc": "d1", "text": "EMEA led growth"},
    {"tenant": "t1", "doc": "d3", "text": "Headcount flat"},
]


def test_build_index():
    assert build_index(CHUNKS) == {
        ("t1", "d1"): ["Revenue grew 12%", "EMEA led growth"],
        ("t2", "d7"): ["Invoice overdue"],
        ("t1", "d3"): ["Headcount flat"],
    }


def test_word_count():
    assert word_count("The cat and THE hat") == {"the": 2, "cat": 1, "and": 1, "hat": 1}
    assert word_count("") == {}


def test_top_words():
    counts = {"b": 2, "a": 2, "c": 5, "d": 1}
    assert top_words(counts, 3) == [("c", 5), ("a", 2), ("b", 2)]


def test_merge_config():
    defaults = {"top_k": 5, "temperature": 0.2}
    overrides = {"temperature": 0}
    assert merge_config(defaults, overrides) == {"top_k": 5, "temperature": 0}
    assert defaults == {"top_k": 5, "temperature": 0.2}


def test_deep_merge():
    base = {"llm": {"model": "gpt-5-mini", "temp": 0.2}, "rag": {"top_k": 5}}
    override = {"llm": {"temp": 0}, "rag": 3, "new": True}
    before = copy.deepcopy(base), copy.deepcopy(override)
    assert deep_merge(base, override) == {
        "llm": {"model": "gpt-5-mini", "temp": 0},
        "rag": 3,
        "new": True,
    }
    assert (base, override) == before


def test_deep_merge_result_does_not_share_nested_dicts():
    base = {"llm": {"model": "a"}}
    merged = deep_merge(base, {})
    merged["llm"]["model"] = "changed"
    assert base["llm"]["model"] == "a"


def test_get_path():
    doc = {"meta": {"lang": "de", "pages": 0, "ocr": {"engine": "azure"}}, "tags": ["x"]}
    assert get_path(doc, "meta.lang", "en") == "de"
    assert get_path(doc, "meta.ocr.engine") == "azure"
    assert get_path(doc, "meta.missing", "en") == "en"
    assert get_path(doc, "meta.pages", 99) == 0          # falsy value must survive
    assert get_path(doc, "tags.first", "none") == "none"  # list is not a dict
    assert get_path(doc, "nope.deeper") is None


def test_invert():
    assert invert({"d1": "t1", "d2": "t2", "d3": "t1"}) == {"t1": ["d1", "d3"], "t2": ["d2"]}
