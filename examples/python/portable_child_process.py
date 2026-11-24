import json
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
runtime = next(
    (p for p in (ROOT / "AkaneServer512.exe", ROOT / "file" / "AkaneServer512.exe") if p.exists()),
    ROOT / "AkaneServer512.exe",
)

with tempfile.TemporaryDirectory(prefix="akane_portable_") as td:
    proc = subprocess.Popen(
        [str(runtime), "--state", td, "--stdio"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        bufsize=1,
    )

    ready = json.loads(proc.stdout.readline())
    assert ready.get("event") == "ready", ready

    proc.stdin.write(json.dumps({"cmd": "runtime_ping"}, ensure_ascii=False) + "\n")
    proc.stdin.flush()
    print(json.loads(proc.stdout.readline()))

    proc.stdin.write(json.dumps({"cmd": "runtime_exit"}, ensure_ascii=False) + "\n")
    proc.stdin.flush()
    print(json.loads(proc.stdout.readline()))
    proc.wait(timeout=5)
