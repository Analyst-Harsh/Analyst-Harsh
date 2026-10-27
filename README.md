# Harshit Goyal

### General description
<sub>who I am, in two lines</sub>

**Full-stack AI developer: agents, RAG and on-device voice, from the model loop to the UI. I measure everything I ship.**

[LinkedIn](https://www.linkedin.com/in/harshit-goyal-ai/) · [harshit.1188@gmail.com](mailto:harshit.1188@gmail.com)

**Stack:** Python · TypeScript · React · Next.js · FastAPI · LangGraph · Qdrant · MLX · PostgreSQL/pgvector<br/>
**Currently building:** Fryday v6, LLM hosting with vLLM and Triton<br/>
**Open to:** full-stack developer and forward-deployed engineer (FDE) roles · India or remote

---

### Selected work
<sub>typical performance</sub>

#### [Fryday](https://github.com/Analyst-Harsh/Fryday) · hands-free Hindi voice assistant, fully on a Mac
- **Problem:** voice assistants in Hindi/Hinglish usually need the cloud, and most can't be interrupted cleanly.
- **Built:** browser mic → Silero VAD → Whisper → Qwen3-4B → Kokoro TTS, all local on Apple MLX, streamed over a WebSocket. Barge-in trims the reply in history to the words you actually heard.
- **Measured:** **~2.8 s voice→voice as heard** on a recording (n=3, 2.3–3.3 s). Server side: VAD 0.50 s + ASR 0.54 s + reply→first audio 1.15 s (first token 0.23 s) = **2.14 s**.

#### [Triage-Bot](https://github.com/Analyst-Harsh/Triage-Bot) · LangGraph agent that triages GitHub issues · [live site ↗](https://analyst-harsh.github.io/Triage-Bot/)
- **Problem:** issue triage is repetitive, but an agent that posts on its own needs guardrails and a human in the loop.
- **Built:** Planner → Researcher → Drafter → Risk check → auto-post or approval queue, with Postgres checkpoints, pgvector episodic memory, a FastAPI operator API and a Next.js dashboard.
- **Measured:** cross-provider trajectory evals (an Anthropic judge grades an OpenAI-run agent); **6 OWASP LLM Top 10 prompt-injection cases** kept as regression tests.

#### [DocMind](https://github.com/Analyst-Harsh/DocMind) · eval-driven RAG with citations
- **Problem:** most RAG demos stack techniques on assumption and never check what actually helped.
- **Built:** Next.js chat + FastAPI + Qdrant. Hybrid search, cross-encoder reranking, semantic caching, agentic and graph retrieval, each adopted or rejected by measurement.
- **Measured:** MRR **0.617 → 0.703 → 0.796** (dense → hybrid → reranked). Measurement caught a real bug: Graph RAG's entity expansion was dead code.

### More builds
- [**signal-score**](https://github.com/Analyst-Harsh/signal-score): classical-ML issue-priority scorer with a gated MLflow promotion loop. It rejected all 4 challengers so far.
- [**treeflow**](https://github.com/Analyst-Harsh/treeflow): a pool of named git worktrees for running coding agents in parallel. Pure stdlib Python.
- [**claude-code-mods**](https://github.com/Analyst-Harsh/claude-code-mods): mods for Claude Code's own interface, such as side-ask.

---

### Electrical characteristics
<sub>measured results</sub>

| Parameter | Typ | Test conditions |
|---|---|---|
| [Voice→voice, as heard](https://github.com/Analyst-Harsh/Fryday/blob/main/docs/EXPERIMENTS.md) | ~2.8 s | Fryday, recorded real-mic session, n=3 (2.3–3.3 s) |
| [End-of-turn silence](https://github.com/Analyst-Harsh/Fryday/blob/main/docs/EXPERIMENTS.md) | 500 ms | Fryday, Silero VAD min silence |
| [Hybrid search recall gain](https://github.com/Analyst-Harsh/DocMind/blob/main/backend/EXPERIMENTS.md) | +7.5 pp | DocMind, Recall@5 0.850 → 0.925, 15-query golden set |
| [Reranking MRR](https://github.com/Analyst-Harsh/DocMind/blob/main/backend/EXPERIMENTS.md) | 0.703 → 0.796 | DocMind, cross-encoder, MRR@5 |
| [Semantic cache cost](https://github.com/Analyst-Harsh/DocMind/blob/main/backend/EXPERIMENTS.md) | −22.3% | DocMind, avg cost per query, 0.75 threshold |
| [LLM-judge disagreement](https://github.com/Analyst-Harsh/DocMind/blob/main/backend/EXPERIMENTS.md) | 30.4% | DocMind, 34 of 112 RAGAS scores re-judged |
| [Challengers promoted](https://github.com/Analyst-Harsh/signal-score/blob/main/EXPERIMENTS.md) | 0 of 4 | signal-score promotion gate (exp 2 was a sweep, not gated) |
| [Prompt-injection cases](https://github.com/Analyst-Harsh/Triage-Bot/blob/main/docs/agent/security.md) | 6 | Triage-Bot, OWASP LLM Top 10 (2025), regression-tested |

---

### Ordering information
<sub>contact</sub>

[LinkedIn](https://www.linkedin.com/in/harshit-goyal-ai/) · [harshit.1188@gmail.com](mailto:harshit.1188@gmail.com)
