import asyncio
import time

import pytest

from session06.ex1_async import (
    collect_stream, run_blocking, stream_words, summarize_all, summarize_all_safe, summarize_limited, with_timeout,
)


async def fake_summarize(doc: str) -> str:
    await asyncio.sleep(0.1)
    return f"summary:{doc}"


def test_summarize_all_is_concurrent_and_ordered():
    start = time.perf_counter()
    result = asyncio.run(summarize_all(["d1", "d2", "d3"], fake_summarize))
    assert result == ["summary:d1", "summary:d2", "summary:d3"]
    assert time.perf_counter() - start < 0.25, "calls ran one after another — use gather"


def test_summarize_limited_respects_limit():
    in_flight = 0
    peak = 0

    async def tracked(doc):
        nonlocal in_flight, peak
        in_flight += 1
        peak = max(peak, in_flight)
        await asyncio.sleep(0.05)
        in_flight -= 1
        return doc.upper()

    result = asyncio.run(summarize_limited([f"d{i}" for i in range(6)], tracked, limit=2))
    assert result == [f"D{i}" for i in range(6)]
    assert peak == 2


def test_summarize_all_safe_keeps_successes():
    async def flaky(doc):
        await asyncio.sleep(0.01)
        if doc == "bad":
            raise TimeoutError("llm timed out")
        return f"ok:{doc}"

    assert asyncio.run(summarize_all_safe(["a", "bad", "c"], flaky)) == {
        "a": "ok:a", "bad": "error: TimeoutError", "c": "ok:c",
    }


def test_with_timeout():
    async def slow():
        await asyncio.sleep(1)
        return "late"

    async def fast():
        return "fast"

    start = time.perf_counter()
    assert asyncio.run(with_timeout(slow, 0.05, "fallback")) == "fallback"
    assert time.perf_counter() - start < 0.5
    assert asyncio.run(with_timeout(fast, 0.05, "fallback")) == "fast"


def test_stream_words_is_async_generator():
    gen = stream_words("hello brave new world")
    assert hasattr(gen, "__anext__"), "must be an async generator (async def + yield)"
    assert asyncio.run(collect_stream(gen)) == "hello brave new world"


def test_run_blocking_keeps_loop_free():
    def blocking(x):
        time.sleep(0.2)
        return x * 2

    async def main():
        ticks = 0

        async def ticker():
            nonlocal ticks
            for _ in range(10):
                await asyncio.sleep(0.01)
                ticks += 1

        result, _ = await asyncio.gather(run_blocking(blocking, 21), ticker())
        return result, ticks

    result, ticks = asyncio.run(main())
    assert result == 42
    assert ticks == 10, "the loop froze — the blocking call ran on the event loop thread"
