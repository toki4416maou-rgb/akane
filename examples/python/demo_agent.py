import json
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
exe = next(
    (p for p in (ROOT / "AkaneServer512.exe", ROOT / "file" / "AkaneServer512.exe") if p.exists()),
    ROOT / "AkaneServer512.exe",
)

with tempfile.TemporaryDirectory(prefix="akane_demo_agent_") as td:
    p = subprocess.Popen(
        [str(exe), "--state", td, "--stdio"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        bufsize=1,
    )

    ready = json.loads(p.stdout.readline())
    assert ready.get("ok") and ready.get("event") == "ready", ready

    def call(obj):
        p.stdin.write(json.dumps(obj, ensure_ascii=False) + "\n")
        p.stdin.flush()
        return json.loads(p.stdout.readline())

    print(call({"cmd": "init", "texts": ["The princess is in the castle.", "The hero is in the village."], "dim": 512}))
    print(call({"cmd": "observe", "text": "The hero arrived at the castle."}))
    print(call({"cmd": "choose", "context": "The hero arrived at the castle.", "candidates": ["Welcome to the castle.", "Please leave immediately."]}))
    call({"cmd": "runtime_exit"})
    p.terminate()
    p.wait(timeout=5)
