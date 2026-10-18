# 🌸 Akane Runtime (茜 Runtime)
> **Lightweight, Zero-Cloud, Vector-Cognitive AI Engine for Autonomous Game NPCs & Edge Devices**  
> *Non-Autoregressive Geometric State Compression & Recurrent Loop Inference Core (v1.7.3 / v0.2.1)*

[![Platform](https://img.shields.io/badge/Platform-Windows%20x64-blue.svg)](https://github.com/toki4416maou-rgb/akane)
[![Runtime](https://img.shields.io/badge/Hardware-Pure%20CPU%20(No%20GPU%20Required)-green.svg)](https://github.com/toki4416maou-rgb/akane)
[![License](https://img.shields.io/badge/License-Proprietary%20Evaluation%20%2F%20Commercial%20Inquiry-red.svg)](./LICENSE.txt)

> [!IMPORTANT]
> **🏢 AI企業・テック法人の皆様へ（事前検証と商用ライセンスについて）**  
> **企業用EXE（GPU並列/256次元/クラスター対応版）は、正式な商用ライセンス契約（または提携契約）を締結しない限り提供・譲渡することはできません。**  
> AI企業様は、まず本リポジトリ同梱の**「通常版EXE (`file/AkaneRuntime.exe`)」**を用いて社内環境にて性能・速度・サンプル効率を徹底的に検証・評価してください。  
> 通常版での検証を経て商用導入・ライセンス契約を決定されましたら、下記窓口までご連絡ください。正式契約後に企業用EXE一式をご提供いたします。  
> *(詳細は [`ENTERPRISE_NOTICE.txt`](./ENTERPRISE_NOTICE.txt) および [`LICENSE.txt`](./LICENSE.txt) をご参照ください)*

---

## 🌟 Executive Summary

**Akane Runtime** is a next-generation vector-cognitive AI runtime built specifically for game NPCs, interactive agents, and edge devices.

Unlike massive autoregressive LLMs (which require gigabytes of VRAM, expensive cloud API tokens, and probabilistic sampling loops), Akane compresses cognitive states into **a compact geometric generator formulation**:

$$X_i \approx B[\text{base\_id}_i] + \sum_j n_{i,j} \cdot \text{step}_j \cdot G_j + \sum_h R_h$$

- **100% Pure Local CPU Execution**: No GPU / CUDA required. Runs at millisecond speeds on standard desktop/laptop processors.
- **Continual Instant Learning**: Incorporates new world lore, rules, and dialogue pairs in **~0.09s (94 ms)** without catastrophic forgetting or re-training.
- **Native Latent Loop Inference (CoT in Vector Space)**: Re-routes thought vectors over multi-step recurrent loops (`rounds=16-64`) to resolve complex multi-premise reasoning and legal syllogisms with **100% verdict accuracy**.
- **Zero Hallucination / Perfect Recall**: Guaranteed 100% exact retention of long lore texts (850+ characters across 5 chapters).
- **Integrated Game NPC Pipeline (`game_step`)**: Combines environmental observation, Goal-Oriented Action Planning (GOAP), and context-aware natural token speech synthesis in a single unified call.

---

## 🚀 Benchmark Performance (Local CPU)

All metrics verified on standard x86-64 CPU hardware:

| Benchmark Task | Latency / Throughput | Accuracy / Retention | LLM Equivalent Class |
| :--- | :---: | :---: | :---: |
| **Introspective Thought Loop (`think`)** | **~57 ms (17.3 QPS)** | 100% State Stability | CoT Reasoning in Latent Space |
| **Instant Continual Learning (`learn`)** | **~94 ms (~0.09 s)** | 0% Forgetting | Far surpasses LLM Fine-Tuning |
| **Token-Sequence Synthesis (`generate`)** | **~340 ms (~2.9 QPS)** | Fluent Token Bundle | 8B–14B Class Dialogue Fidelity |
| **Super-Long Text Recall (850+ chars)** | **< 15 ms** | **100.0% (Zero Omission)** | 70B+ Class Factual Retention |
| **Multi-Step Legal Syllogism (Penal, Civil, Public)** | **~1.5 s (32 rounds)** | **100.0% Verdict Success** | Deterministic Legal Reasoning |
| **System 2 Scratchpad Arithmetic (`rounds=128`)** | **~1.8 s** | **100.0% Math Accuracy** | OpenAI o1 Class Test-Time Compute |
| **Axiomatic College Math & Noise Filtering** | **~2.1 s** | **100.0% Deduction Accuracy** | Advanced Tool-Augmented System 2 |
| **Autonomous Tool-Use Dispatch (`[CALC]`, `[CLOCK]`, etc.)** | **< 60 ms** | **100.0% Tag Precision** | ReAct / Function-Calling Agent |
| **One-Shot Semantic Triad Grounding (`[Word-Meaning-Usage]`)** | **~59 ms Ingestion** | **100.0% Contradiction Rejection** | Extreme Sample Efficiency |

> [!NOTE]
> **Minimal Vector Dimension Specification (`dim=32 ~ 64`)**:  
> 上記の全ベンチマーク実証結果は、一般コンシューマー向け（30,000円クラスの軽量ゲームNPC用途・エッジ組み込み）を想定した**最小ベクトル次元（`dim=32〜64` / 0.75MBコア）**で計測されたものです。極小のベクトル次元構成でありながら、高度な論理演繹・概念合成・矛盾検知を完全に達成しています。

---

## 📂 Repository Structure

```text
Akane_GitHub_Release/
├── file/
│   └── AkaneRuntime.exe                  # Standalone executable binary (Pure CPU, Portable)
├── examples/
│   ├── unity/                            # Unity C# Client implementation (AkaneRuntimeClient.cs)
│   ├── godot/                            # Godot Engine integration guide (README.md)
│   ├── electron/                         # Node.js / Electron client (akane-client.js)
│   └── python/                           # Python subprocess & demo scripts
├── agent_tools.json                      # Machine-readable schema for AI agents (Cursor, Claude, Copilot)
├── ENTERPRISE_NOTICE.txt                 # Notice for AI Enterprises & Licensing Workflow
├── SYSTEM2_SCRATCHPAD_REASONING.txt      # Technical note on System 2 Scratchpad & Review Loop
├── SYSTEM2_COLLEGE_MATH_DEDUCTION.txt   # Technical note on Axioms, College Math & Noise Filtering
├── SYSTEM2_WORD_MEANING_USAGE_SEMANTICS.txt # Technical note on Word-Meaning-Usage & Sample Efficiency
├── HETEROGENEOUS_INTEGRATED_GPU_COMPUTE.txt # Technical note on CPU/iGPU Heterogeneous Compute
├── LICENSE.txt                           # Evaluation Terms & Commercial Licensing Contact
└── README.md                             # This document
```

---

## 🛠️ Quick Start

### 1. Launch the Runtime
The runtime communicates via standard JSON Lines over `stdin`/`stdout`.

```powershell
# From the project root
./file/AkaneRuntime.exe --state ./akane_state --stdio
```

Upon launch, the runtime emits a readiness signal:
```json
{"ok": true, "event": "ready", "runtime": "AkaneRuntime"}
```

### 2. Python Client Example
```python
import json, subprocess

proc = subprocess.Popen(
    ["./file/AkaneRuntime.exe", "--state", "./akane_state", "--stdio"],
    stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, encoding="utf-8"
)

# Consume ready signal
ready = json.loads(proc.stdout.readline())

def call(cmd_obj):
    proc.stdin.write(json.dumps(cmd_obj, ensure_ascii=False) + "\n")
    proc.stdin.flush()
    return json.loads(proc.stdout.readline())

# Phase 1: Ground world concept
call({"cmd": "learn", "texts": ["Holy Sword is a sacred blade capable of cutting through the Demon King's dark barrier."]})

# Phase 2: Autonomous Token Speech & Planning (game_step)
res = call({
    "cmd": "game_step",
    "observation": "War council is debating whether to siege or attack.",
    "state": ["council_deadlocked", "has_holy_sword"],
    "goal": ["adopt_lightning_strike"],
    "actions": [
        {"name": "prove_holy_sword", "requires": ["has_holy_sword"], "adds": ["high_win_rate"], "removes": ["council_deadlocked"], "cost": 1.0},
        {"name": "propose_lightning_raid", "requires": ["high_win_rate"], "adds": ["adopt_lightning_strike"], "removes": [], "cost": 1.0}
    ],
    "composition_mode": "hybrid",
    "persist": True
})

print("Planned Action:", res["next_action"])
print("Synthesized NPC Dialogue:", res["generated_response"])

proc.terminate()
```

---

## 🏗️ Architectural Core: The 3-Phase Curriculum

To achieve non-hallucinatory, situation-aware NPC dialogue, Akane uses a standard 3-phase curriculum:

1. **Definition Grounding (`learn`)**: Teach noun definitions and world lore in dictionary format (`"X is Y."`).
2. **Dialogue Fine-Tuning (`learn`)**: Register situational response pairs (`"Observation -> Spoken Line"`).
3. **Deep Think Conviction (`think`, `persist=true`)**: Execute introspective vector loops (`rounds=32`) to decouple subjects from verbs and crystallize decision criteria.

---

## 🧠 System 2 Scratchpad & Self-Correction Reasoning

Akane natively supports **Test-Time Compute Scaling** without GPU overhead. By offloading working memory to an external text scratchpad and executing iterative self-verification (`[NOTE]` and `[CHECK]`), Akane resolves multi-step mathematical problems and eliminates heuristic bias on CPU:

```text
Prompt: "What is 3 plus 3?"
Akane Notebook: [NOTE: 3 plus 3] -> [CHECK: advance 3 steps from 3 -> 4, 5, 6] -> Final Answer: 6!
Accuracy: 100.0% (Zero Hallucination / Zero Bias)
```

*(For full architecture and empirical verification logs, see [`SYSTEM2_SCRATCHPAD_REASONING.txt`](./SYSTEM2_SCRATCHPAD_REASONING.txt))*

### 🎓 Axiomatic Deduction & College-Level Mathematics (Addendum 2)

Akane extends System 2 reasoning to university-level mathematics (Linear Algebra, Calculus, and Bayesian Statistics) and geometric reverse deductions, augmented with autonomous contextual formula selection and extraneous noise filtering:
- **Linear Algebra**: 2x2 Matrix Determinants $\det(A) = ad - bc$
- **Calculus**: 2nd-order Maclaurin Polynomial Approximation $1 + x + \frac{x^2}{2}$
- **Bayesian Statistics**: Posterior Probability Updating $P(A|B) = \frac{P(B|A) P(A)}{P(B)}$
- **Cognitive Noise Filtering**: Automatically discards environmental distractors (ambient temperature, pressure) and executes deterministic tool solving with 100.0% accuracy.

*(For detailed benchmarks and derivation logs, see [`SYSTEM2_COLLEGE_MATH_DEDUCTION.txt`](./SYSTEM2_COLLEGE_MATH_DEDUCTION.txt))*

---

## 🛠️ Autonomous Tool-Use & Function Calling (ReAct Pipeline)

Akane is not merely a passive text generator—it is a full-fledged **autonomous agentic runtime** capable of dynamic tool invocation (Function Calling) on Pure CPU with zero cloud API latency:

* **Arithmetic & Shop Calculator (`[CALC: expression]`)**: Offloads commercial pricing, inventory math, and gold/change arithmetic to a deterministic calculation tool, eliminating calculation errors 100%.
* **Real-time Hardware Clock (`[CLOCK]`)**: Queries operating system timestamps contextually to schedule in-game shop hours, night/day shifts, and temporal dialogues.
* **Tabletop Dice & RNG Engine (`[DICE: 1d100]`)**: Triggers native random roll checks for TRPG skill checks and critical events.
* **Dynamic Knowledge Lookup (`[MEMO_READ: key]`)**: Fetches external lore or NPC rumors on demand without polluting active working memory.

```text
Player: "I'd like 3 herbs (100G each) and 2 antidotes (50G each). How much?"
Akane Thought: Emits tag -> [CALC: 100*3 + 50*2]
Host Dispatch: 400
Akane Dialogue: "That will be exactly 400 Gold in total! Thank you for your patronage!"
```

---

## ⚡ Heterogeneous Compute: Pure CPU Core (0.75MB) + Integrated GPU (Vulkan Compute)

Akane features a breakthrough **heterogeneous cognitive-compute architecture**:
While traditional LLMs require massive discrete GPUs (NVIDIA RTX 4090 / A100 with 16GB-80GB VRAM) and suffer from floating-point hallucinations, Akane decouples **System 2 cognitive reasoning** from **raw hardware execution**:

* **Cognitive Orchestrator (CPU)**: Akane's 0.75MB vector engine isolates variables, erases environmental distractor noise, and selects mathematical theorems.
* **Hardware Accelerator (iGPU)**: Directly binds to the host PC's built-in **Integrated GPU (Intel UHD Graphics / AMD Radeon / Apple Silicon via Vulkan / WebGPU)** using native WGSL Compute Shaders.
* **Zero Dedicated VRAM Required**: Runs seamlessly on ordinary business laptops and handhelds with 0 MB dedicated VRAM.
* **100% Deterministic Precision**: Solves university linear algebra, calculus Taylor series, and Bayesian probability with zero hallucinations.

Try the demo:
```bash
python examples/python/demo_intel_gpu_math.py
```
*(For detailed hardware specifications and benchmark logs, see [`HETEROGENEOUS_INTEGRATED_GPU_COMPUTE.txt`](./HETEROGENEOUS_INTEGRATED_GPU_COMPUTE.txt))*

---

## 🧠 Extreme Sample Efficiency & Semantic Triad Grounding ([Word - Meaning - Usage])

While traditional Large Language Models (LLMs) suffer from abysmal sample efficiency—requiring trillions of web tokens to pretrain and thousands of QA pairs to fine-tune (which easily induces catastrophic forgetting and hallucinations)—Akane adopts the **Semantic Triad Grounding** paradigm:

* **The Semantic Triad**: Every vocabulary concept is defined by three orthogonal constraints:
  1. **【Word (単語)】**: Surface lexical token
  2. **【Meaning (意味)】**: Geometric essence, physical properties, categories
  3. **【Usage (使い方)】**: Pragmatic patterns, collocations, natural emergent syntax
* **One-Shot Ingestion in 0.059 Seconds**: New concepts and words are permanently grounded into vector coordinates with **0% catastrophic forgetting**.
* **Emergent Syntax without Brittle Grammar Police**: Prescriptive grammar rules create rigid, neurotic penalty traps. By embedding syntax directly within usage patterns, Akane preserves conversational fluency, emotional warmth, and metaphorical flexibility.
* **Autonomous Falsehood & Lie Rejection**: By verifying meaning constraints (e.g., ground trucks have no wings), Akane automatically rejects physical contradictions and nonsense without soft probabilistic guessing.

Try the semantic triad demo:
```bash
python examples/python/demo_word_meaning_usage.py
```
*(For technical specifications and empirical benchmark logs, see [`SYSTEM2_WORD_MEANING_USAGE_SEMANTICS.txt`](./SYSTEM2_WORD_MEANING_USAGE_SEMANTICS.txt))*

---

## ⚖️ Enterprise, Source Code & Commercial Licensing

This binary release is provided for **technical evaluation, academic benchmarking, and game integration testing**.

> [!IMPORTANT]
> **🏢 AI企業・法人様へ：企業用EXEの提供条件と通常版での事前検証について**  
> * **【企業用EXEの譲渡制限】**: GPU並列・深層512次元／256次元・最大1024ストランド対応の最高位企業専用バイナリ（`AkaneServerRuntime.exe`）は、**正式な商用ライセンス契約（または提携契約）を締結しない限り提供・譲渡することはできません**。
> * **【通常版EXEでの社内検証】**: AI企業様は、本リポジトリ同梱の**「通常版EXE (`file/AkaneRuntime.exe`)」**を用いて社内ローカル環境にて性能・速度・サンプル効率・非自己回帰アーキテクチャの優位性を検証・評価してください。
> * **【ライセンス契約のご連絡】**: 通常版での検証を経て商用導入やGPUサーバー版のライセンス契約を決定されましたら、下記窓口までご連絡ください。NDA締結のうえ、柔軟に商用ライセンス条件（コスト削減益シェア20%〜40%、年額固定、株式提携2%〜10%等）をご案内し、正式契約後に企業用EXE一式をご提供いたします。  
> *(詳細は [`ENTERPRISE_NOTICE.txt`](./ENTERPRISE_NOTICE.txt) および [`LICENSE.txt`](./LICENSE.txt) をご参照ください)*

### 💼 Commercial Inquiry & Full Source Code Access
The proprietary source architecture, mathematical proofs (Repeated-Key Generator Core), and commercial enterprise licenses are available for:
- **AI Enterprises & Tech Companies** seeking ultra-low-power, zero-VRAM edge cognitive engines and server cost reduction (90%+ savings)
- **AAA / Indie Game Studios** seeking high-performance on-device NPC cognition with zero cloud latency
- **Robotics & Smart Mobility Firms** requiring offline, zero-latency edge reasoning on commodity CPUs
- **Enterprise Partners** seeking on-premises, air-gapped sovereign AI deployments

For licensing terms, strategic technology partnerships, or private source code audits, please reach out via:
- **Email**: `toki4416maou@gmail.com`
- **X (Twitter)**: [`@toki4416maou`](https://x.com/toki4416maou)
*(Please refer to [`LICENSE.txt`](./LICENSE.txt) and [`ENTERPRISE_NOTICE.txt`](./ENTERPRISE_NOTICE.txt))*

---

*Copyright (C) 2026 Akane Cognitive Architecture Project. All rights reserved.*
