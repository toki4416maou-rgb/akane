# Akane Runtime

> **Lightweight Pure-CPU Continual Vector Memory & Stateful Inference Engine**  
> Standalone Windows x64 Runtime (`AkaneServer512.exe` · Evaluation Edition · Core `v1.7.3`)

Akane Runtime is a compact, non-autoregressive **512-dimensional vector-native cognitive engine** designed for continual episodic memory, multi-hop causal state tracking, and real-time agent/NPC workflows—running **100% on local CPU without requiring VRAM or cloud inference calls**.

---

## Core Architecture

Rather than backpropagating through billion-parameter matrices or keeping unbounded prompt histories, Akane represents incoming text through a continuous-discrete geometric formulation (`Xᵢ ≈ B[baseᵢ] + Σⱼ nᵢ,ⱼ · sⱼ · Gⱼ + Σₕ rₕ`):

- **Adaptive Surface Codec**: Streaming subword/surface tokenization with IDF-aware centering, surface-manifold readout projection (`semantic_readout_text`), and an X-space learned grammatical verbalizer persisted in `codec.json`.
- **Repeated-Key Core (`dim=512`)**: Quantizes representations against `128` orthogonal generator bases, `6-bit` repeat limits (`63`), and `8` residual key streams.
- **Dynamic Braid & Persistent Vector State**: Maintains parallel hypothesis strands (Dynamic Braid schedule up to `1,024` strands across `4` interference rounds) alongside multi-slot persistent state vectors that update incrementally via `observe` without catastrophic forgetting.
- **Integrated Planning & RPC**: Exposes `stdio` JSON-Lines and `HTTP` REST APIs with Goal-Oriented Action Planning (`plan` / `game_step`), episodic retrieval (`remember` / `recall`), and action selection (`choose`).

---

## Observed Benchmarks (Local x86-64 CPU, Zero GPU)

All metrics below were measured locally with the standalone `AkaneServer512.exe` binary (`222.26 MB`, `233,056,509` bytes) using pure CPU (`OMP_NUM_THREADS=1`):

| Metric / Capability | Measured Result | Conditions |
| :--- | :--- | :--- |
| **Executable Footprint** | `222.26 MB` (`0 MB` VRAM) | Self-contained Windows x64 binary (`stdio` / `HTTP`) |
| **512-dim Initialization (`init`)** | `~0.81 s` – `3.54 s` | `4`-sentence seed (`805.2 ms`) / vocabulary catalog (`3,538.3 ms`) |
| **32-Round Latent Loop (`think`)** | `~263 ms` – `427 ms` | `rounds=32`, `dim=512`, `max_strands=1024` |
| **Continual Episodic Ingestion (`observe`)** | `~430 ms / fact` avg | Streaming unseen facts + belief updates into persistent slots |
| **Multi-Hop & Negation (`generate`)** | `~571 ms` – `606 ms` | Unseen `1-Hop`, `2-Hop`, `3-Hop` chains, role query & negation update |
| **Cold Checkpoint Reload (`--state`)** | `~677 ms` | Restart fresh process from disk & verify 3-hop recall (`PASS`) |
| **Bilingual EN/JA Verification** | `6/6 + Repeat PASS` | Evaluated on `25k`-vocab state & fresh BPE core (no `stack.memory`) |

*Note: Akane is an experimental continual-memory and stateful-routing engine built to run standalone on edge devices/game NPCs or as a low-latency companion memory layer alongside frontier LLMs (such as Claude). It is not a replacement for frontier LLM open-ended coding or zero-shot world knowledge.*

---

## Quick Start (60-Second Self-Contained Demo)

1. Download **`akane512_evaluation.zip`** (or **`AkaneServer512.exe`**) from the [Releases](https://github.com/toki4416maou-rgb/akane/releases) page.
2. Place `AkaneServer512.exe` in the root of this repository folder (or inside `./file/AkaneServer512.exe`).
3. Run the verification demo (requires Python 3.9+ standard library only—no `pip install` needed):

```powershell
python demo_eval_quickstart.py
```

The demo automatically runs:
1. Vocabulary catalog initialization (`dim=512` — **zero** target causal facts in `init`)
2. 32-round latent recurrent loop (`think`)
3. Unseen continual `observe` stream (multi-hop chains + scout-report negation override)
4. Live `1-Hop`, `2-Hop`, `3-Hop`, role, negation-override, and non-destructive repeat queries
5. Clean shutdown (`runtime_exit`), cold restart from saved checkpoint, and reload verification

---

## Transport & Integration

### 1. `stdio` JSON-Lines RPC
```powershell
./AkaneServer512.exe --state ./akane_state --stdio
```
Wait for the initial readiness line (`{"ok": true, "event": "ready", ...}`), then exchange one JSON object per line. Full schema is defined in [`agent_tools.json`](./agent_tools.json).

### 2. Local HTTP Server
```powershell
./AkaneServer512.exe --state ./akane_state --http --host 127.0.0.1 --port 17831
```
- Health check: `GET http://127.0.0.1:17831/health`
- Inference & control endpoint: `POST http://127.0.0.1:17831/api`

---

## Repository Contents

```text
akane/
├── demo_eval_quickstart.py          # Self-contained CPU multi-hop & persistence demo
├── agent_tools.json                 # JSON command schema for AkaneServer512.exe
├── LICENSE.txt                      # Non-Commercial Technical Evaluation License
├── README.md                        # This documentation
├── .gitignore
└── examples/
    ├── python/
    │   ├── demo_agent.py            # Minimal observe + choose example
    │   └── portable_child_process.py# stdio lifecycle & runtime_ping example
    ├── electron/
    │   ├── akane-client.js          # Node.js / Electron stdio client
    │   └── akane-portable-client.js # Electron packaged child-process helper
    ├── godot/
    │   └── README.md                # Godot HTTPRequest integration notes
    └── unity/
        └── AkaneRuntimeClient.cs    # Unity C# UTF-8 stdio client
```

---

## Licensing & Contact

- **Evaluation License:** All files and release binaries are licensed strictly for non-commercial technical evaluation, benchmarking, and due diligence under [`LICENSE.txt`](./LICENSE.txt). Production commercial use, SaaS/cloud deployment, OEM distribution, and custom licensing require a separate agreement.
- **Founder / Author:** Toki Hoshino (`Akane Cognitive Lab`)
- **Email:** `toki4416maou@gmail.com`
- **X (Twitter):** [`@toki4416maou`](https://x.com/toki4416maou)
