import json
import subprocess
from pathlib import Path

runtime = Path(__file__).resolve().parents[2] / "AkaneRuntime.exe"
proc = subprocess.Popen(
    [str(runtime)],
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
