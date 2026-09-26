import pytest

from session01.ex4_tuples_sets import Hit, can_read, has_all_scopes, hybrid_merge, mark_seen, min_max_score, to_hits


def test_to_hits():
    hits = to_hits([("d1", 4, 0.71), ("d2", 1, 0.93)])
    assert hits == [Hit("d1", 4, 0.71), Hit("d2", 1, 0.93)]
    assert hits[1].score == 0.93


def test_min_max_score():
    assert min_max_score(to_hits([("d1", 4, 0.71), ("d2", 1, 0.93), ("d3", 2, 0.5)])) == (0.5, 0.93)
    with pytest.raises(ValueError):
        min_max_score([])


def test_hybrid_merge():
    result = hybrid_merge({"c1", "c2", "c3", "c5", "c8"}, {"c2", "c5", "c7", "c9"})
    assert result == {
        "candidates": ["c1", "c2", "c3", "c5", "c7", "c8", "c9"],
        "agreed": ["c2", "c5"],
        "vector_only": ["c1", "c3", "c8"],
        "keyword_only": ["c7", "c9"],
        "disagreement": ["c1", "c3", "c7", "c8", "c9"],
    }


def test_mark_seen_is_tenant_aware():
    seen: set[tuple[str, str]] = set()
    assert mark_seen(seen, "t1", "doc-9") is True
    assert mark_seen(seen, "t1", "doc-9") is False
    assert mark_seen(seen, "t2", "doc-9") is True  # same doc id, different tenant
    assert seen == {("t1", "doc-9"), ("t2", "doc-9")}


def test_can_read():
    assert can_read({"viewer", "finance"}, {"finance", "admin"}) is True
    assert can_read({"viewer"}, {"admin"}) is False
    assert can_read(set(), {"admin"}) is False


def test_has_all_scopes():
    assert has_all_scopes({"docs:read", "docs:write", "chat"}, {"docs:read", "chat"}) is True
    assert has_all_scopes({"docs:read"}, {"docs:read", "chat"}) is False
    assert has_all_scopes({"x"}, set()) is True
