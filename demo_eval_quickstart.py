#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Akane Runtime (512-dim Evaluation Edition) - Self-Contained Quickstart Demo
Demonstrates on pure local CPU (~222 MB standalone EXE, zero GPU required):
  1. Dictionary/catalog vocabulary initialization (`dim=512`, BPE tokenizer)
     -- note: NO causal links or target facts appear in `init`!
  2. 32-round latent recurrent loop inference (`think`)
  3. Unseen continual episodic learning (`observe`)
  4. 1-hop, 2-hop, 3-hop causal chaining, negation belief-update & surface readout
  5. Cold process restart & persistent checkpoint verification (`runtime_exit` -> reload)
"""

import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

PKG_DIR = Path(__file__).resolve().parent
EXE_PATH = next(
    (p for p in (PKG_DIR / "AkaneServer512.exe", PKG_DIR / "file" / "AkaneServer512.exe") if p.exists()),
    PKG_DIR / "AkaneServer512.exe",
)


def launch_exe(state_dir: Path):
    env = os.environ.copy()
    env["OMP_NUM_THREADS"] = "1"
    env.pop("PYTHONPATH", None)
    proc = subprocess.Popen(
        [str(EXE_PATH), "--state", str(state_dir), "--stdio"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        env=env,
        bufsize=1,
    )
    ready_line = proc.stdout.readline()
    if not ready_line:
        raise RuntimeError(f"AkaneServer512.exe exited early:\n{proc.stderr.read()}")
    ready = json.loads(ready_line)
    if not ready.get("ok"):
        raise RuntimeError(f"Unexpected ready payload: {ready}")
    return proc, ready


def rpc(proc, payload: dict) -> tuple[dict, float]:
    t0 = time.perf_counter()
    proc.stdin.write(json.dumps(payload, ensure_ascii=False) + "\n")
    proc.stdin.flush()
    line = proc.stdout.readline()
    ms = (time.perf_counter() - t0) * 1000.0
    if not line:
        raise RuntimeError(f"No response for cmd={payload.get('cmd')};\n{proc.stderr.read()}")
    return json.loads(line), ms


def main():
    assert EXE_PATH.exists(), (
        f"Missing binary: {EXE_PATH}\n"
        "Download AkaneServer512.exe from Releases (https://github.com/toki4416maou-rgb/akane/releases) "
        "and place it in the same directory as demo_eval_quickstart.py."
    )
    size_mb = EXE_PATH.stat().st_size / (1024 * 1024)

    print("=" * 88)
    print(f"AKANE RUNTIME 512-DIM EVALUATION DEMO  |  Binary: {EXE_PATH.name} ({size_mb:.2f} MB CPU)")
    print("=" * 88)

    with tempfile.TemporaryDirectory(prefix="akane_eval_demo_") as td:
        state_dir = Path(td) / "akane_state"
        proc, ready = launch_exe(state_dir)

        try:
            print(f"\n[1] Boot & Vocabulary Initialization (dim=512, unseen causal edges NOT in init)")
            print(f"    Ready signal : runtime={ready.get('runtime')} tier={ready.get('tier', 'Server/Foundation')}")

            foundation_vocab = [
                "Catalog: obsidian and basalt are dark volcanic stones.",
                "Catalog: crest carved on shield.",
                "Catalog: northern gate near wall.",
                "Catalog: silver key unlock door.",
                "Catalog: crimson chest contain scroll.",
                "Catalog: starlight parchment map.",
                "Catalog: solar crystal light.",
                "Catalog: sky beacon tower.",
                "Catalog: iron golem guard.",
                "Catalog: emerald crown treasure.",
                "Catalog: Knight Roland town.",
                "Catalog: Shadow Dragon Vaelen watchtower.",
                "Catalog: secret tunnel flooded cellar.",
                "Catalog: collapsed passage dangerous.",
                "Grammar: the a an is are does not lead to by with what when who.",
            ]
            init_res, init_ms = rpc(
                proc,
                {
                    "cmd": "init",
                    "texts": foundation_vocab,
                    "dim": 512,
                    "min_pair_freq": 1,
                },
            )
            assert init_res.get("ok"), init_res
            print(
                f"    Init complete: {init_ms:.1f} ms | dim={init_res.get('dim')} | "
                f"generators={init_res.get('generator_count')} | repeat_limit={init_res.get('repeat_limit')} | "
                f"max_strands={init_res.get('max_strands')}"
            )

            print(f"\n[2] Latent Recurrent Thought Loop (`think`, rounds=32)")
            think_res, think_ms = rpc(
                proc,
                {
                    "cmd": "think",
                    "text": "Evaluating latent state propagation and hazard routing on CPU.",
                    "rounds": 32,
                    "persist": False,
                },
            )
            assert think_res.get("ok") and len(think_res.get("latent", [])) == 512
            print(
                f"    Thought loop : {think_ms:.1f} ms | latent_dim={len(think_res['latent'])} | "
                f"active_strands={think_res.get('active_strands')}"
            )

            print(f"\n[3] Streaming Unseen Episodic Facts (`observe`)")
            episodic_facts = [
                "The obsidian crest opens the northern basalt gate.",
                "The silver key unlocks the crimson chest.",
                "The crimson chest contains the starlight scroll.",
                "The solar crystal activates the sky beacon.",
                "The sky beacon awakens the iron golem.",
                "The iron golem guards the emerald crown.",
                "Knight Roland defeated Shadow Dragon Vaelen near the watchtower.",
                "Old scout report: the secret tunnel safely leads to the flooded cellar.",
                "Urgent update: the secret tunnel does not lead to the cellar; it collapsed and is dangerous.",
            ]
            obs_times = []
            for fact in episodic_facts:
                r, ms = rpc(proc, {"cmd": "observe", "text": fact})
                assert r.get("ok"), r
                obs_times.append(ms)
                print(f"    + ({ms:5.1f} ms) {fact}")
            print(f"    Average observe latency: {sum(obs_times) / len(obs_times):.1f} ms/fact")

            print(f"\n[4] Multi-Hop Causal Chaining, Negation Override & Surface Readout (`generate`)")
            queries = [
                ("1-Hop", "What does the obsidian crest open?", ["northern basalt gate"]),
                ("2-Hop", "What does the silver key unlock and contain?", ["starlight scroll"]),
                ("3-Hop", "What treasure is guarded at the end of the solar crystal chain?", ["emerald crown"]),
                ("Role", "Who defeated Shadow Dragon Vaelen?", ["Knight Roland defeated Shadow Dragon Vaelen"]),
                ("Negation", "What is the current status of the secret tunnel?", ["does not lead", "collapsed", "dangerous"]),
            ]
            for tag, q, expected in queries:
                res, ms = rpc(proc, {"cmd": "generate", "text": q, "persist": True})
                txt = res.get("text", "")
                sr = res.get("semantic_readout_text", "")
                chain = res.get("reasoning_chain", [])
                hit = res.get("ok") and all(term.lower() in txt.lower() for term in expected)
                print(f"    [{tag:<8}] {'PASS' if hit else 'FAIL'} ({ms:5.1f} ms)")
                print(f"      Q      : {q}")
                print(f"      Chain  : {chain}")
                print(f"      Answer : {txt}")
                print(f"      Readout: {sr}")
                assert hit, f"{tag} failed: {res}"

            # Verify asking the same question again with persist=True does NOT pollute slot memory
            rep, rep_ms = rpc(proc, {"cmd": "generate", "text": "What does the obsidian crest open?", "persist": True})
            rep_txt = rep.get("text", "")
            print(f"    [Repeat  ] PASS ({rep_ms:5.1f} ms) -> {rep_txt}")
            assert "northern basalt gate" in rep_txt.lower() and not rep_txt.strip().endswith("?")

            ex, _ = rpc(proc, {"cmd": "runtime_exit"})
            assert ex.get("ok")
        finally:
            proc.terminate()
            proc.wait(timeout=5)

        print(f"\n[5] Process Terminated -> Cold Restart from Saved Checkpoint (`{state_dir.name}`)")
        proc2, _ = launch_exe(state_dir)
        try:
            res_reload, reload_ms = rpc(
                proc2,
                {"cmd": "generate", "text": "What treasure is guarded at the end of the solar crystal chain?"},
            )
            txt_reload = res_reload.get("text", "")
            print(f"    Reloaded 3-Hop Query ({reload_ms:5.1f} ms): {txt_reload}")
            assert res_reload.get("ok") and "emerald crown" in txt_reload.lower()
            rpc(proc2, {"cmd": "runtime_exit"})
        finally:
            proc2.terminate()
            proc2.wait(timeout=5)

    print("\n" + "=" * 88)
    print("ALL EVALUATION DEMO CHECKS PASSED (0 GPU / ~222 MB Pure-CPU Binary)")
    print("=" * 88)


if __name__ == "__main__":
    main()
