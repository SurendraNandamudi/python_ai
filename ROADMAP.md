# 30-day roadmap — Software Developer → AI Engineer

**Start:** 2026-09-25 (Day 1) · **End:** 2026-10-24 (Day 30) · full-time
**Goal:** build, explain, debug, design, **ship** and *defend* real AI applications — with NeuroDocx as the case study.

## How every day runs

| Block | Where | What |
|---|---|---|
| **Learn** (~3h) | Mentor laptop | Visual, interactive lessons → predict → reveal → quick checks |
| **Build** (~4h) | Practice laptop | `git pull` → exercises + tests → the day's build → `git push` |
| **Defend** (~1h) | Either | 10 interview questions out loud · explain 2 concepts without notes · revision sheet |
| **Frontier 30** (30 min, from Day 7) | Either | One *latest* concept per day — see the list at the bottom |

Rules: RECAP → TEST → FIND GAPS → PRACTISE → MOVE ON. A major misunderstanding blocks the next topic.
Every day ends with something **pushed** to this repo.

## The capstone that grows all month: `docintel/`

One product, built layer by layer — the exact product question:
*"User uploads a document → gets a summary → can ask questions about it"*, shipped as a
**standalone service that other (Python or non-Python) systems can call**.

```
Day 5-6    FastAPI skeleton: API keys + JWT tenants, upload, async job processing
Day 7-9    LLM client (provider-agnostic): streaming, retries, cost; /summarize; structured extraction
Day 12-13  Embeddings + tenant-isolated vector store
Day 14-17  Ingestion (OCR) → chunking → hybrid retrieval → rerank → grounded Q&A with citations → evals
Day 18-20  Agentic assistant: tools, memory, multi-step tasks, human approval
Day 21-22  MCP server exposing the same capabilities to AI clients
Day 23     Swap in a company's OWN model (self-hosted, OpenAI-compatible) with zero app changes
Day 24     Expose it: REST + SSE + webhooks + generated SDKs; called from a Node service
Day 25     Deploy it: Docker, CI/CD, Hetzner + TLS, workers, scaling
Day 26-27  Guardrails, injection defence, tracing, cost controls · Higgsfield media generation
```

---

## Phase 1 — Python recap (Days 1–5)

| Day | Date | Session | Topics (from the 41-topic list) | Practice pushed |
|---|---|---|---|---|
| 1 | 09-25 | **S1** Data & memory | Execution model, typing, operators, `==` vs `is`, `None`, truthiness, memory model, strings, lists, tuples, sets, dicts, Big-O (1–6, 26, 27) | `session01/` ✅ |
| 2 | 09-26 | S1 wrap + **S2** Functions | Control flow (7) · S1 checkpoint · comprehensions (8), functions & `*args/**kwargs` (9), LEGB/closures (10), lambda/map/filter/reduce (11), exceptions (12) | `session02/` |
| 3 | 09-27 | **S3** OOP + **S4** Protocols | Classes, composition, ABCs (16), dunders (17), dataclasses (18), enums (19) · iterators (20), generators → LLM streaming (21), decorators → `@app.get` (22), context managers (23) | `session03/`, `session04/` |
| 4 | 09-28 | **S5** Structure + **S6** Async | Type hints (24), `match` (25), modules/packages (13), files & pathlib (14), JSON/CSV (15), project layout (41) · async/await vs JS, event loop, gather (35), threads/processes/GIL (36) | `session05/`, `session06/` |
| 5 | 09-29 | **S7** Production Python | Pydantic (38), httpx + retries (37), pytest + mocks (39), logging (32), config & secrets (33), uv/lockfiles (34), regex (31), collections/itertools/functools (28–30), debugging (40) | `session07/` + **Python checkpoint interview** |

## Phase 2 — Backend (Days 5–6)

| Day | Date | Topics | Build |
|---|---|---|---|
| 5 (pm) | 09-29 | FastAPI: routing, Pydantic request/response models, status codes, OpenAPI | `docintel/` skeleton |
| 6 | 09-30 | Dependency injection, JWT + **tenant dependency**, API keys, async DB, background tasks vs queues (why RabbitMQ), SSE streaming, error model, API tests | Upload → queue → worker → job status, tenant-scoped |

## Phase 3 — LLM fundamentals (Days 7–9)

| Day | Date | Topics | Build |
|---|---|---|---|
| 7 | 10-01 | What an LLM is, pre-training → SFT → RLHF, **tokens & BPE**, **context windows**, why models hallucinate, **reasoning models** & test-time compute | Token counter + context-budget helper |
| 8 | 10-02 | LLM APIs: roles/system prompt, sampling params, **streaming**, **provider abstraction** (Azure OpenAI / Claude / Ollama / self-hosted), rate limits, retries, cost | `llm/` gateway interface + `/summarize` (map-reduce for long docs) |
| 9 | 10-03 | **Prompt engineering**, **structured output** (JSON schema + Pydantic), **function calling** intro, **context engineering** | Invoice/contract field extraction → validated model |

## Phase 4 — Transformers (Days 10–11)

| Day | Date | Topics | Build |
|---|---|---|---|
| 10 | 10-04 | Token embeddings, positional info (sinusoidal / RoPE), **attention**, **self-attention, Q/K/V**, scaled dot-product, causal mask | Attention by hand in NumPy |
| 11 | 10-05 | **Multi-head attention**, transformer block (FFN, residual, layer norm), decoder-only LLMs, **Mixture-of-Experts**, **inference: prefill vs decode, KV cache** | Multi-head attention in NumPy + explain-it-back |

## Phase 5 — Embeddings & vector search (Days 12–13)

| Day | Date | Topics | Build |
|---|---|---|---|
| 12 | 10-06 | **Embeddings**, **vectors**, **cosine similarity** vs dot vs L2, sentence-transformers, normalisation, embedding model choice | Semantic search in pure NumPy |
| 13 | 10-07 | **Vector DBs** (Chroma, pgvector, Qdrant), ANN, **HNSW**, IVF, metadata filtering, **multi-tenant isolation** | Tenant-isolated vector store in `docintel` |

## Phase 6 — RAG deeply (Days 14–17)

| Day | Date | Topics | Build |
|---|---|---|---|
| 14 | 10-08 | **Document intelligence & OCR** (Azure DI vs PaddleOCR fallback, layout, tables, **multimodal** LLMs on page images), **chunking** strategies | Ingestion: file → text → chunks → embeddings (async worker) |
| 15 | 10-09 | **RAG** end-to-end, why it reduces hallucination, **retrieval**, grounded prompts, **citations**, streaming answers | `/documents/{id}/ask` with citations |
| 16 | 10-10 | **Hybrid search** (BM25 + vectors, RRF), **reranking**, query rewriting, **agentic RAG**, **GraphRAG** (when it's worth it), long-context vs RAG | Hybrid + rerank stage |
| 17 | 10-11 | **RAG evaluation** (faithfulness, relevance, context precision/recall), golden sets, LLM-as-judge, failure modes, **RAG security** | Eval suite in pytest |

## Phase 7 — Agentic AI (Days 18–20)

| Day | Date | Topics | Build |
|---|---|---|---|
| 18 | 10-12 | **Tool calling** in depth: schemas, the tool loop, parallel calls, errors, idempotency | Tools: `search_documents`, `summarize`, `check_compliance` |
| 19 | 10-13 | **AI agents** & **agentic AI**: LLM vs agent vs workflow, ReAct, planning, **agent memory** (short/long-term), state machines, stopping conditions, **human-in-the-loop** approval | Agentic document assistant (LangGraph-style graph) |
| 20 | 10-14 | Agentic patterns (router, orchestrator-workers, evaluator-optimizer), **multi-agent** systems, **A2A protocol**, **computer-use / browser agents**, **text-to-SQL** with safety, agent evaluation | KPI-validation agent with read-only SQL tool |

## Phase 8 — MCP (Days 21–22)

| Day | Date | Topics | Build |
|---|---|---|---|
| 21 | 10-15 | **MCP**: why it exists, **architecture** (host / client / server), JSON-RPC, transports (stdio, streamable HTTP), **tools / resources / prompts**, **MCP vs APIs vs function calling** | `docintel` MCP server (FastMCP) |
| 22 | 10-16 | Connecting to Claude / IDEs, inspector testing, **OAuth for MCP**, multi-tenant MCP, tool poisoning, MCP + A2A together | Tenant-aware remote MCP server |

## Phase 9 — Ship it: own models, integration, deployment (Days 23–25)

| Day | Date | Topics | Build |
|---|---|---|---|
| 23 | 10-17 | **Company's own LLM**: when to self-host, **fine-tuning vs RAG**, **LoRA / QLoRA**, **quantization** (GGUF, AWQ, FP8), **serving** (vLLM, SGLang, TGI, Ollama), **OpenAI-compatible endpoints**, GPU sizing (VRAM math), throughput vs latency, batching, **speculative decoding**, **model gateway** (LiteLLM-style routing + fallback), air-gapped / on-prem | Run a local model behind an OpenAI-compatible server; switch `docintel` to it by config only |
| 24 | 10-18 | **Exposing an AI service**: REST + OpenAPI, **SSE streaming**, **async jobs + webhooks** (HMAC-signed), idempotency keys, versioning, API keys vs OAuth2 client-credentials vs JWT, rate limits & quotas per tenant, **generated SDKs** (TS/Java/C#), gRPC, queue-based integration, embeddable widget, **integration patterns**: separate microservice vs sidecar vs Python library vs MCP | Call `docintel` from a **Node/TypeScript service** using a generated client; webhook receiver |
| 25 | 10-19 | **Deployment**: Dockerfile (multi-stage, non-root), docker compose (api + worker + queue + vector DB + Postgres), **CI/CD** (GitHub Actions: test → build → push → deploy), Hetzner + Caddy TLS, secrets, health/readiness probes, horizontal scaling of workers, GPU vs CPU nodes, Kubernetes concepts, zero-downtime deploys | `docintel` running on a server with HTTPS |

## Phase 10 — Production & generative media (Days 26–27)

| Day | Date | Topics | Build |
|---|---|---|---|
| 26 | 10-20 | **AI security**: direct & indirect **prompt injection**, jailbreaks, data exfiltration, OWASP LLM Top 10, PII redaction, guardrails, securing agents, tools and MCP | Injection test set + input/output guards |
| 27 | 10-21 | **AI evaluation** in CI, **observability** (traces, OpenTelemetry, token/cost dashboards), **cost optimisation** (prompt caching, semantic caching, model routing, batching) · **Generative media via Higgsfield API** (100+ image/video models, async submit → poll/webhook, cost control, storing outputs) | Tracing + cost report · "visual summary" feature via Higgsfield |

## Phase 11 — System design & interview (Days 28–30)

| Day | Date | Topics | Output |
|---|---|---|---|
| 28 | 10-22 | AI system-design framework · designs: multi-tenant enterprise RAG, document-intelligence SaaS, customer-support agent, "bring your own model" platform | 3 written designs |
| 29 | 10-23 | **NeuroDocx architecture defence**: NestJS + FastAPI split, RabbitMQ, ChromaDB, AES-256-GCM, tenant isolation, OCR fallback, own-model option — trade-offs, scaling, failure modes | Architecture doc + mock grilling |
| 30 | 10-24 | **Full interview simulation**: Python coding · AI concepts · system design · project deep-dive | Scorecard + gap plan |

---

## Frontier 30 — one latest concept a day (Days 7–27)

Interview-level: what it is, why it matters, when you'd use it, one trade-off.

| Day | Concept | Day | Concept |
|---|---|---|---|
| 7 | Reasoning models & test-time compute | 18 | Computer-use & browser agents |
| 8 | Prompt caching | 19 | A2A (agent-to-agent) protocol |
| 9 | Context engineering | 20 | Agent memory systems (episodic/semantic) |
| 10 | Mixture-of-Experts | 21 | Speculative decoding |
| 11 | Long context vs RAG | 22 | Small language models & on-device AI |
| 12 | Matryoshka & late-interaction embeddings (ColBERT) | 23 | Distillation & synthetic data |
| 13 | Multimodal & vision-language models | 24 | Diffusion vs autoregressive generation (image/video/text) |
| 14 | GraphRAG | 25 | Prompt optimisation (DSPy, GEPA) |
| 15 | Agentic RAG | 26 | Guardrail models & constitutional approaches |
| 16 | **JEPA & world models** (LeCun: predict in embedding space, not tokens) | 27 | State-space models (Mamba) & hybrids |
| 17 | LLM-as-judge pitfalls | | |

---

## Progress log

| Day | Date | Done | Gaps found |
|---|---|---|---|
| 1 | 09-25 | S1: 1.1–1.7 taught (memory model, strings, lists, tuples, sets, dicts) | `[row] * n` shares references; composite set members need a tuple |
| 2 | 09-26 | Repo + uv set up; roadmap v2 (agentic AI, own models, integration, deployment, Higgsfield, frontier concepts) | — |
