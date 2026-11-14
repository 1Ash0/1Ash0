<div align="center">

<a href="https://github.com/1Ash0">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=26&duration=3200&pause=1200&color=58A6FF&center=true&vCenter=true&width=720&height=60&lines=Hi%2C+I'm+Asmit;I+build+systems.;Then+I+find+where+they+break." alt="Asmit: I build systems. Then I find where they break." />
</a>

**B.Tech + M.S. by Research in CSE @ IIIT Hyderabad**
AI systems · agent reliability · evals · telemetry you can verify

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/asmit-shaw-6a09a2315)
[![Email](https://img.shields.io/badge/Email-asmit.shaw%40research.iiit.ac.in-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:asmit.shaw@research.iiit.ac.in)
[![GitHub](https://img.shields.io/badge/GitHub-1Ash0-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/1Ash0)
[![assay](https://img.shields.io/badge/latest-assay-FF5B3A?style=flat-square)](https://1ash0.github.io/assay/)
<!-- TODO: add portfolio badge once the site is live
[![Portfolio](https://img.shields.io/badge/Portfolio-111111?style=flat-square)](https://YOUR-SITE) -->

</div>

---

## 🔬 Latest: assay

<p align="center"><a href="https://1ash0.github.io/assay/"><img src="https://raw.githubusercontent.com/1Ash0/assay/main/docs/assets/demo.gif" alt="assay rebuilding the request a model was sent and sealing it against the transcript's own hash" width="560"></a></p>

**Can you trust your coding agent's telemetry?** I summed the usage on every line of one of my own Claude Code sessions and got 20,195 output tokens. Counted once per message: 5,320. **assay** audits the record before you read anything into it: it states what was captured, runs 14 self-consistency checks with findings pinned to file, line and bytes, and rebuilds each API request to hash-match the transcript's own digest. Local-only, deterministic, no model in any verdict.

[**Live site**](https://1ash0.github.io/assay/) · [**Explorer**](https://1ash0.github.io/assay/explorer.html) · [**Repo and limitations**](https://github.com/1Ash0/assay)

---

## 🏆 Highlights

| | |
|---|---|
| 🎓 **Reliance Foundation Scholar** | Merit-based national scholarship |
| 📄 **Research paper, FMFP 2026** | ML for Darrieus hydrokinetic turbines (IIT Roorkee SPARK, under Prof. Chandra Shekhar Pant and Dan Singh Pimoli). The model's failure to generalize became the core result. |
| 🏢 **Samsung R&D Bangalore** | Research intern, Design Automation Lab |
| 🚀 **Former President, E-Cell IIIT-NR** | Ran E-Summit 2026: 1,700+ registrations, 375+ hackathon participants, ₹1.3L+ prize pool |
| 📈 **Lateral entry to IIIT Hyderabad (LEEE 2026)** | Simultaneous B.Tech + M.S. by Research in CSE, after a 9.44 CGPA at IIIT Naya Raipur |
| 🧠 **Stanford Machine Learning Specialization** | Completed on Coursera, Aug 2026 |

---

## 🔍 What I care about

Agents and ML systems usually fail quietly: a confident wrong answer, a badly chosen tool, a trace that looks fine and isn't. I build the system, then break it on purpose to see what it does under pressure.

Canary is the clearest example. I planted facts in an agent's context, compacted it four different ways, and checked which facts survived. A channel rule died in 27 of 27 runs under the head+tail policy, and nothing in the agent's output hinted that it was gone.

surfacelab asks the same question of tool choice. On tools with one clear job each, models were near perfect; on real MCP servers loaded together, gpt-oss found the only right tool 77% of the time, and its misses landed on tools whose descriptions read alike.

assay turns the same question on the logs themselves. When I tried to rebuild exactly what a model was sent from its own transcript, it worked for 0 of 2,049 requests; with the stored blobs, 99.7% hash-matched. Anything it can't prove stays "unresolved" instead of being guessed. I also tested whether an LLM could do the checking: AUROC 0.48 on 379 human-labelled spans, so no model gets near a verdict.

That's the through-line in my research direction: calibrated uncertainty, interpretable policies, and evals and telemetry that catch silent failure.

---

## 🛠️ Selected work

| Project | What it does | Stack | Links |
|---|---|---|---|
| **[assay](https://github.com/1Ash0/assay)** | Audits Claude Code telemetry: states what was captured (Capture Level L1–L4), runs 14 self-consistency checks with findings pinned to file, line and byte range, and rebuilds each API request to hash-match the transcript's own digest (99.7% of held-out requests; 0 of 2,049 from lines alone). A naive sum of the log overcounted output tokens 3.8× in one run. An LLM judge scored AUROC 0.48, so no model touches a verdict. One user's sessions, run locally. | TypeScript, zod, Vitest, OpenTelemetry | [Live site](https://1ash0.github.io/assay/) · [Repo](https://github.com/1Ash0/assay) |
| **[surfacelab](https://github.com/1Ash0/surfacelab)** | Open evaluation of how AI agents choose MCP tools: 12 preregistered experiments, 3 models, 396 recorded calls on 82 tools from 11 real servers, drawn as a scroll-driven 3D observatory. Found that misses land on look-alike descriptions, and that adding a second browser server changed the agent's first move in 14 of 24 requests. | Python, Three.js/WebGL, Docker | [Observatory](https://1ash0.github.io/surfacelab/) · [Repo](https://github.com/1Ash0/surfacelab) |
| **[Canary](https://github.com/1Ash0/canary)** | Open-source kit that plants facts in an agent's context, compacts it four ways, and measures which facts survive. 3 canaries, 4 policies, 27 seeds per cell, preregistered, every run replayable. | Python | [Live demo](https://canary-brown.vercel.app) · [Repo](https://github.com/1Ash0/canary) |
| **[ChunkScope](https://github.com/1Ash0/chunkscope)** | Visualizes a RAG pipeline end to end, so you can see how chunking and retrieval choices change what the model receives | Next.js, FastAPI, Three.js/WebGL, pgvector | Being upgraded for deployment |
| **[Nexora](https://github.com/1Ash0/Nexora)** | Five-agent research pipeline (planner, executor, critic, contradiction engine, synthesizer) on LangGraph. Deep research in under 3 minutes. | LangGraph, Qdrant, Redis Pub/Sub, Groq | Being upgraded for deployment |
| **[C Shell](https://github.com/1Ash0/c-shell)** | A Unix shell written from scratch in C for my OS course: parsing, process creation, job handling | C | Course project |


---

## 🧰 Tech arsenal

<div align="center">

<img src="https://skillicons.dev/icons?i=py,c,js,ts,react,nextjs,fastapi,postgres,redis,threejs,docker,git,linux,vercel&perline=14" alt="Python, C, JavaScript, React, Next.js, FastAPI, PostgreSQL, Redis, Three.js, Docker, Git, Linux, Vercel" />

</div>

| Area | What I use |
|---|---|
| **Languages** | Python, C, JavaScript, TypeScript |
| **Agents and LLM systems** | LangGraph, MCP, Groq, multi-agent orchestration, context compaction, evals |
| **Telemetry and testing** | OpenTelemetry, Vitest, Playwright, JSON Schema (zod) |
| **Retrieval and data** | pgvector, Qdrant, PostgreSQL, Redis (Pub/Sub) |
| **Web and visualization** | Next.js, React, FastAPI, Three.js/WebGL |
| **Systems** | Linux, xv6 (MLFQ scheduler), a Unix shell in C |
| **Shipping** | Git, Docker, Vercel, GitHub Actions |

<!-- TODO: remove any icon or row you don't actually use; keep this list honest -->

---

<details>
<summary><b>🧪 Building now (click to expand)</b></summary>

<br/>

Canary, surfacelab and assay are a set of agent-harness projects, built one at a time. What's next on assay:

- A hooks (L2) importer: no run has been captured at L2 yet
- An intake for redacted runs from other people, since every number so far is one user's
- Extending the parent-chain check to links of non-event lines, a blind spot found by planting a known fault

Each gets linked here once it has a working demo, not before.

</details>

<details>
<summary><b>🎓 Background (click to expand)</b></summary>

<br/>

- **Research**: ML for hydrokinetic turbines, IIT Roorkee (SPARK), published at FMFP 2026
- **Industry**: Samsung R&D Bangalore (Design Automation Lab); business analyst at RootVestors
- **Education**: IIIT Hyderabad (2026 to 2029, B.Tech + M.S. by Research); previously IIIT Naya Raipur
- **Certifications**: Stanford Machine Learning Specialization (Coursera); DSA (takeUforward)
- **Leadership**: E-Cell IIIT-NR (President; earlier People Ops), MUN IIIT-NR, Technovate
- **School**: ISC 2023: 96.75 · ICSE 2021: 98.80

</details>

---

## ⚡ Live from GitHub

*This section refreshes itself every 6 hours via GitHub Actions.*

<table>
<tr>
<td valign="top" width="50%">

### Recently active repos
<!-- REPOS:START -->
- **[DnA-ICC](https://github.com/1Ash0/DnA-ICC)** · `Python`
- **[mcp-226-docstring-eval](https://github.com/1Ash0/mcp-226-docstring-eval)** · `Python`
- **[assay](https://github.com/1Ash0/assay)** · `TypeScript`<br/><sub>Can you trust your coding agent’s telemetry? assay audits Claude Code…</sub>
- **[surfacelab](https://github.com/1Ash0/surfacelab)** · `Python`
- **[canary](https://github.com/1Ash0/canary)** · `Python`
<!-- REPOS:END -->

</td>
<td valign="top" width="50%">

### Latest commits
<!-- COMMITS:START -->
- [`4a17a18`](https://github.com/1Ash0/DnA-ICC/commit/4a17a18a6c3e06c2934ea406dda299e430846cba) Re-record demo video as one continuous take with natural na… <sub>· DnA-ICC · 13 Nov 2026</sub>
- [`9b8f87d`](https://github.com/1Ash0/DnA-ICC/commit/9b8f87dccc5f1ad2cd9f8a0a5c15a8eb07056e20) Burn narration captions into 45.mp4; add 45.srt <sub>· DnA-ICC · 13 Nov 2026</sub>
- [`7de666a`](https://github.com/1Ash0/DnA-ICC/commit/7de666a2d01c8cb1fa3a8d42e8594110ef0e1f9e) Add demo video 45.mp4 <sub>· DnA-ICC · 13 Nov 2026</sub>
- [`5d3062f`](https://github.com/1Ash0/DnA-ICC/commit/5d3062fd7a8db23357c0098efffe72042f36a737) Rename matches form field to match_count; add update-path t… <sub>· DnA-ICC · 13 Nov 2026</sub>
- [`0d9dae3`](https://github.com/1Ash0/DnA-ICC/commit/0d9dae3892f10288ab5b43c5af5c9813d7cce229) Phase 4: ICC rankings MySQL schema, populate data, Flask ap… <sub>· DnA-ICC · 12 Nov 2026</sub>
- [`77a17c5`](https://github.com/1Ash0/mcp-226-docstring-eval/commit/77a17c56ebe21b0dbd7b8077149f3bd16a937ce8) Data for modelcontextprotocol/python-sdk#226 docstring-form… <sub>· mcp-226-docstring-eval · 06 Nov 2026</sub>
<!-- COMMITS:END -->

</td>
</tr>
</table>

<sub>Last refreshed: <!-- UPDATED:START -->14 Nov 2026, 04:51 UTC<!-- UPDATED:END --></sub>

---

## 📬 Contact

| | |
|---|---|
| ✉️ **Email** | [asmit.shaw@research.iiit.ac.in](mailto:asmit.shaw@research.iiit.ac.in) |
| 💼 **LinkedIn** | [asmit-shaw](https://www.linkedin.com/in/asmit-shaw-6a09a2315) |
| 🐙 **GitHub** | [1Ash0](https://github.com/1Ash0) |
| 🎓 **Affiliation** | IIIT Hyderabad, B.Tech + M.S. by Research in CSE |

---

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/1Ash0/1Ash0/output/github-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/1Ash0/1Ash0/output/github-snake.svg" />
  <img alt="Contribution graph, eaten by a snake" src="https://raw.githubusercontent.com/1Ash0/1Ash0/output/github-snake.svg" />
</picture>

**Working on agent reliability, evals, telemetry, or RAG failure modes? Let's compare notes: [LinkedIn](https://www.linkedin.com/in/asmit-shaw-6a09a2315).**

</div>
