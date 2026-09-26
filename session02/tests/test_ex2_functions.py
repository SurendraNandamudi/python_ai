import pytest

from session02.ex2_functions import apply_to_all, build_request, make_counter, make_multipliers, merge_all, pipeline, retry


class TestBuildRequest:
    def test_defaults(self):
        assert build_request("hi") == {"prompt": "hi", "model": "gpt-5-mini", "temperature": 0.2}

    def test_keywords_and_extra(self):
        assert build_request("hi", model="m", temperature=0, max_tokens=512) == {
            "prompt": "hi", "model": "m", "temperature": 0, "max_tokens": 512,
        }

    def test_prompt_is_positional_only(self):
        with pytest.raises(TypeError):
            build_request(prompt="hi")

    def test_model_is_keyword_only(self):
        with pytest.raises(TypeError):
            build_request("hi", "m")


def test_merge_all():
    assert merge_all({"a": 1}, {"a": 2, "b": 3}, b=9) == {"a": 2, "b": 9}
    assert merge_all() == {}


def test_merge_all_does_not_mutate():
    first = {"a": 1}
    merge_all(first, {"a": 2})
    assert first == {"a": 1}


def test_make_counter_independent():
    c1, c2 = make_counter(), make_counter(10)
    assert [c1(), c1(), c2(), c1()] == [1, 2, 11, 3]


def test_make_multipliers():
    fns = make_multipliers(4)
    assert [f(10) for f in fns] == [0, 10, 20, 30]


def test_pipeline():
    assert pipeline(str.strip, str.lower, len)("  HeLLo ") == 5
    assert pipeline()(42) == 42


class TestRetry:
    def test_succeeds_after_failures(self):
        calls = []

        def flaky():
            calls.append(1)
            if len(calls) < 3:
                raise ConnectionError("boom")
            return "ok"

        assert retry(flaky, attempts=3) == "ok"
        assert len(calls) == 3

    def test_reraises_last(self):
        calls = []

        def always():
            calls.append(1)
            raise TimeoutError(f"attempt {len(calls)}")

        with pytest.raises(TimeoutError, match="attempt 2"):
            retry(always, attempts=2)

    def test_non_retryable_propagates_immediately(self):
        calls = []

        def bug():
            calls.append(1)
            raise TypeError("bug")

        with pytest.raises(TypeError):
            retry(bug, attempts=5, exceptions=(ConnectionError,))
        assert len(calls) == 1


def test_apply_to_all():
    assert apply_to_all(round, [1.234, 5.678], ndigits=1) == [1.2, 5.7]
    assert apply_to_all(str.upper, ["a", "b"]) == ["A", "B"]
