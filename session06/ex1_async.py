"""Session 06 · Exercise 1 — asyncio for AI backends.

Run:  uv run pytest session06/tests/test_ex1_async.py -v
In every function, `summarize` is an ASYNC callable like:  async def summarize(doc: str) -> str
(think: one LLM API call). Tests use tiny sleeps, so the whole file runs in well under 2 seconds.
"""

import asyncio
from collections.abc import AsyncIterator, Awaitable, Callable
from typing import Any

Summarize = Callable[[str], Awaitable[str]]


async def summarize_all(docs: list[str], summarize: Summarize) -> list[str]:
    """Summarise every doc CONCURRENTLY; return results in the same order as `docs`.
    (3 docs x 0.1s each must finish in ~0.1s, not 0.3s.)"""
    raise NotImplementedError


async def summarize_limited(docs: list[str], summarize: Summarize, limit: int) -> list[str]:
    """Like summarize_all, but never more than `limit` calls in flight at once —
    every LLM provider rate-limits you. Hint: asyncio.Semaphore + `async with`."""
    raise NotImplementedError


async def summarize_all_safe(docs: list[str], summarize: Summarize) -> dict[str, str]:
    """One failing doc must NOT lose the others' results.
    Return {doc: summary} for successes and {doc: "error: <ExceptionClassName>"} for failures.
    Hint: gather(..., return_exceptions=True)."""
    raise NotImplementedError


async def with_timeout(make_call: Callable[[], Awaitable[Any]], seconds: float, default: Any) -> Any:
    """Await make_call(); if it takes longer than `seconds`, give up and return `default`.
    Hint: asyncio.timeout() (3.11+) or asyncio.wait_for()."""
    raise NotImplementedError


async def stream_words(text: str, delay: float = 0.0) -> AsyncIterator[str]:
    """ASYNC GENERATOR that yields the words of `text` one by one, awaiting
    asyncio.sleep(delay) before each — a fake LLM token stream."""
    raise NotImplementedError
    yield  # (keeps this a generator until you implement it — delete when done)


async def collect_stream(stream: AsyncIterator[str]) -> str:
    """Consume an async stream with `async for` and join the pieces with single spaces."""
    raise NotImplementedError


async def run_blocking(fn: Callable[..., Any], *args: Any) -> Any:
    """Run a BLOCKING (sync) function without freezing the event loop; return its result."""
    raise NotImplementedError
