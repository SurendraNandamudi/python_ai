# 30-day roadmap — Software Developer → AI Engineer

**Start:** 2026-09-25 (Day 1) · **End:** 2026-10-24 (Day 30) · full-time
**Goal:** build, explain, debug, design and *defend* real AI applications — with NeuroDocx as the case study.

## How every day runs

| Block | Where | What |
|---|---|---|
| **Learn** (~3h) | Mentor laptop | Visual, interactive lessons → predict → reveal → quick checks |
| **Build** (~4h) | Practice laptop | `git pull` → exercises + tests → the day's build → `git push` |
| **Defend** (~1h) | Either | 10 interview questions out loud · explain 2 concepts without notes · revision sheet |

Rules: RECAP → TEST → FIND GAPS → PRACTISE → MOVE ON. A major misunderstanding blocks the next topic.
Every day ends with something **pushed** to this repo.

## The capstone that grows all month: `neurodocx_mini/`

From Day 5 onward, every phase adds a layer to one FastAPI app — by Day 30 it is a portfolio piece:

```
Day 5-6   API skeleton: tenants (JWT), document upload, async processing
Day 7-9   LLM client: streaming, retries, cost tracking, summaries, structured extraction
Day 13-15 Embeddings + vector store (tenant-isolated) + ingestion/OCR pipeline
Day 16-19 Grounded RAG chat with citations, hybrid search, reranking, an eval suite
Day 20-22 Tool-calling agent: search, compliance check, KPI validation, text-to-SQL
Day 23-25 MCP server exposing NeuroDocx tools/resources/prompts
Day 26-27 Guardrails, prompt-injection defence, tracing, cost controls
```

---

## Phase 1 — Python recap (Days 1–5)

| Day | Date | Session | Topics (from the 41-topic list) | Practice pushed |
|---|---|---|---|---|
| 1 | 09-25 | **S1** Data & memory | Execution model, dynamic vs strong typing, types, operators, `==` vs `is`, `None`, truthiness, memory model, strings, lists, tuples, sets, dicts, Big-O (1–6, 26, 27) | `session01/` ✅ pushed |
| 2 | 09-26 | S1 wrap-up + **S2** Functions | Control flow (7) · S1 checkpoint · comprehensions (8), functions, `*args/**kwargs`, keyword/positional-only (9), LEGB scope, closures (10), lambda/map/filter/reduce (11), exceptions (12) | `session02/` |
| 3 | 09-27 | **S3** OOP + **S4** Protocols | Classes, properties, inheritance vs composition, ABCs (16), dunder methods (17), dataclasses (18), enums (19) · iterators (20), generators & LLM streaming (21), decorators & `@app.get` (22), context managers (23) | `session03/`, `session04/` |
| 4 | 09-28 | **S5** Structure + **S6** Async | Type hints, generics, TypedDict (24), `match` (25), modules/packages/`__main__` (13), files & pathlib (14), JSON/CSV (15), project layout (41) · async/await vs JS, event loop, tasks, gather (35), threads vs processes vs GIL (36) | `session05/`, `session06/` |
| 5 | 09-29 | **S7** Production Python | Pydantic (38), httpx + retries/timeouts (37), pytest + mocks (39), logging (32), config & secrets (33), uv/venv/lockfiles (34), regex (31), collections/itertools/functools (28–30), debugging (40) | `session07/` + **Python checkpoint interview** |

## Phase 2 — Backend (Days 5–6)

| Day | Date | Topics | Build |
|---|---|---|---|
| 5 (pm) | 09-29 | FastAPI basics: routing, path/query/body, Pydantic request/response models, status codes, OpenAPI | `neurodocx_mini/` skeleton |
| 6 | 09-30 | Dependency injection, JWT auth + **tenant dependency**, async DB access, background tasks vs queues (RabbitMQ why), SSE streaming, error handling, API tests with `TestClient` | Upload → queue → process → status endpoint, tenant-scoped |

## Phase 3 — LLM fundamentals (Days 7–9)

| Day | Date | Topics | Build |
|---|---|---|---|
| 7 | 10-01 | What an LLM is (next-token prediction), pre-training → SFT → RLHF, **tokens & tokenisation (BPE)**, context windows, why models hallucinate | Token counter + context-budget helper |
| 8 | 10-02 | LLM APIs: messages/roles/system prompt, temperature/top-p/max tokens, streaming, provider abstraction (Azure OpenAI / Claude / Ollama), rate limits, retries, cost per token | `llm_client.py` with streaming + retries + cost log; `/summarize` endpoint |
| 9 | 10-03 | Prompt engineering (few-shot, delimiters, chain-of-thought vs hidden reasoning), **structured output** with JSON schema + Pydantic validation, intro to function calling | Invoice field extraction → validated Pydantic model |

## Phase 4 — Transformers (Days 10–12)

| Day | Date | Topics | Build |
|---|---|---|---|
| 10 | 10-04 | Token embeddings, positional information (why + sinusoidal/RoPE idea), attention intuition | Attention weights by hand in NumPy |
| 11 | 10-05 | **Self-attention, Q/K/V, scaled dot-product, causal masking, multi-head attention** | Multi-head attention in NumPy (~60 lines) |
| 12 | 10-06 | Transformer block (attention + FFN + residual + layer norm), decoder-only models, **inference: prefill vs decode, KV cache**, quantization, GPU inference basics | Diagram + explain-it-back recording |

## Phase 5 — Embeddings & vector search (Days 13–15)

| Day | Date | Topics | Build |
|---|---|---|---|
| 13 | 10-07 | Embeddings as vectors, **cosine similarity** vs dot vs L2, sentence-transformers, normalisation | Semantic search in pure NumPy |
| 14 | 10-08 | **Vector databases** (Chroma, pgvector), ANN, **HNSW**, IVF, metadata filtering, multi-tenant isolation (collection vs filter) | Chroma store in `neurodocx_mini`, tenant-filtered |
| 15 | 10-09 | Document intelligence: OCR, Azure DI vs PaddleOCR fallback, layout/tables, multimodal models | Ingestion pipeline: file → text → clean → metadata |

## Phase 6 — RAG deeply (Days 16–19)

| Day | Date | Topics | Build |
|---|---|---|---|
| 16 | 10-10 | **RAG** end-to-end, why it reduces hallucination, grounded prompts, citations | Naive RAG chat with citations + streaming |
| 17 | 10-11 | **Chunking** strategies (fixed, recursive, semantic, structure-aware), overlap, retrieval, top-k, query rewriting | Chunker comparison on the same docs |
| 18 | 10-12 | **Hybrid search** (BM25 + vectors, RRF), **reranking** (cross-encoders), context compression | Hybrid + rerank stage |
| 19 | 10-13 | **RAG evaluation** (faithfulness, answer relevance, context precision/recall), golden sets, LLM-as-judge, failure modes, **RAG security** | Eval suite that runs in pytest |

## Phase 7 — Tools & agents (Days 20–22)

| Day | Date | Topics | Build |
|---|---|---|---|
| 20 | 10-14 | **Function / tool calling** in depth: schemas, the tool loop, parallel calls, errors | Tools: `search_documents`, `check_compliance` |
| 21 | 10-15 | **AI agents**: LLM vs agent, ReAct loop, planning, **agent memory** (short/long-term), state, stopping conditions | Agentic document assistant |
| 22 | 10-16 | Agentic patterns (router, orchestrator-workers, evaluator-optimizer), frameworks (LangGraph, agent SDKs), **AI + SQL / text-to-SQL** with safety | KPI-validation agent with read-only SQL tool |

## Phase 8 — MCP deeply (Days 23–25)

| Day | Date | Topics | Build |
|---|---|---|---|
| 23 | 10-17 | **MCP**: why it exists, architecture (host / client / server), JSON-RPC, transports (stdio, streamable HTTP), **tools / resources / prompts** | Hello-world MCP server |
| 24 | 10-18 | Building real servers, testing with the inspector, connecting to Claude / an IDE | **NeuroDocx MCP server**: search, compliance, doc resources, prompts |
| 25 | 10-19 | **MCP vs REST APIs vs function calling**, auth (OAuth), multi-tenant MCP, tool poisoning | Tenant-aware auth on the MCP server |

## Phase 9 — Security, evaluation, production (Days 26–27)

| Day | Date | Topics | Build |
|---|---|---|---|
| 26 | 10-20 | **AI security**: direct & indirect **prompt injection**, jailbreaks, data exfiltration, OWASP LLM Top 10, PII, guardrails, securing agents & tools | Injection test set + input/output guards |
| 27 | 10-21 | **AI evaluation** in CI, **observability** (traces, spans, token/cost dashboards), **cost optimisation** (caching, prompt caching, model routing, batching), **fine-tuning vs RAG, LoRA, QLoRA** | Tracing + cost report for `neurodocx_mini` |

## Phase 10 — System design & interview (Days 28–30)

| Day | Date | Topics | Output |
|---|---|---|---|
| 28 | 10-22 | AI system-design framework · design: multi-tenant enterprise RAG, document-intelligence pipeline, customer-support agent | 3 written designs |
| 29 | 10-23 | **NeuroDocx architecture defence**: every choice (NestJS + FastAPI split, RabbitMQ, ChromaDB, AES-256-GCM, tenant isolation, OCR fallback) with trade-offs, scaling, failure modes | Architecture doc + mock grilling |
| 30 | 10-24 | **Full interview simulation**: Python coding · AI concepts · system design · project deep-dive | Scorecard + gap plan |

---

## Progress log

| Day | Date | Done | Gaps found |
|---|---|---|---|
| 1 | 09-25 | S1: 1.1–1.7 taught (memory model, strings, lists, tuples, sets, dicts) | `[row] * n` shares references; composite set members need a tuple |
| 2 | 09-26 | Repo + uv set up; roadmap written | — |
