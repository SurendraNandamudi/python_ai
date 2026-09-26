import pytest

from session01.ex3_lists import batched, dedupe_keep_order, rank_doc_desc, rank_doc_then_chunk, sliding_windows, top_k

HITS = [("d1", 4, 0.71), ("d2", 1, 0.93), ("d1", 2, 0.88), ("d3", 7, 0.64), ("d2", 3, 0.93)]


def test_top_k():
    assert top_k(HITS, 3) == [("d2", 1, 0.93), ("d2", 3, 0.93), ("d1", 2, 0.88)]


def test_top_k_does_not_mutate():
    hits = list(HITS)
    top_k(hits, 2)
    assert hits == HITS


def test_top_k_k_larger_than_list():
    assert len(top_k(HITS, 99)) == 5


def test_rank_doc_then_chunk():
    hits = [("b", 1, 0.9), ("a", 1, 0.9), ("a", 5, 0.9), ("c", 0, 0.95)]
    assert rank_doc_then_chunk(hits) == [("c", 0, 0.95), ("a", 5, 0.9), ("a", 1, 0.9), ("b", 1, 0.9)]


def test_rank_doc_desc():
    hits = [("a", 2, 0.9), ("b", 3, 0.9), ("b", 1, 0.9), ("c", 0, 0.5)]
    original = list(hits)
    assert rank_doc_desc(hits) == [("b", 1, 0.9), ("b", 3, 0.9), ("a", 2, 0.9), ("c", 0, 0.5)]
    assert hits == original


def test_dedupe_keep_order():
    assert dedupe_keep_order(["d3", "d1", "d3", "d2", "d1"]) == ["d3", "d1", "d2"]
    assert dedupe_keep_order([]) == []


def test_batched():
    assert batched([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert batched([], 3) == []
    with pytest.raises(ValueError):
        batched([1], 0)


class TestSlidingWindows:
    def test_example(self):
        assert sliding_windows(list("abcdefg"), 3, 1) == [["a", "b", "c"], ["c", "d", "e"], ["e", "f", "g"]]

    def test_last_window_shorter(self):
        assert sliding_windows(list("abcdefgh"), 3, 1) == [
            ["a", "b", "c"], ["c", "d", "e"], ["e", "f", "g"], ["g", "h"],
        ]

    def test_no_overlap(self):
        assert sliding_windows([1, 2, 3, 4], 2, 0) == [[1, 2], [3, 4]]

    def test_window_bigger_than_input(self):
        assert sliding_windows([1, 2], 5, 1) == [[1, 2]]

    def test_empty(self):
        assert sliding_windows([], 3, 1) == []

    @pytest.mark.parametrize(("size", "overlap"), [(3, 3), (3, 5), (3, -1)])
    def test_invalid_overlap(self, size, overlap):
        with pytest.raises(ValueError):
            sliding_windows([1, 2, 3], size, overlap)
