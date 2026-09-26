from session02.ex3_comprehensions import email_domains, flatten, label_scores, long_chunk_lengths, tenant_doc_map, transpose


def test_flatten():
    assert flatten([[1, 2], [3], []]) == [1, 2, 3]


def test_long_chunk_lengths():
    assert long_chunk_lengths({"c1": "abc", "c2": "a", "c3": "abcd"}, 3) == {"c1": 3, "c3": 4}


def test_email_domains():
    assert email_domains(["A@X.com", "b@x.com", "nope", "c@y.io"]) == {"x.com", "y.io"}


def test_transpose():
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert transpose([]) == []


def test_label_scores():
    assert label_scores([0.9, 0.2, 0.5], 0.5) == ["relevant", "noise", "relevant"]


def test_tenant_doc_map():
    rows = [("t1", "d3"), ("t2", "d1"), ("t1", "d1"), ("t1", "d3")]
    assert tenant_doc_map(rows) == {"t1": ["d1", "d3"], "t2": ["d1"]}
