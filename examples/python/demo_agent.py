import json, subprocess, sys

p = subprocess.Popen(
    [sys.executable, "AkaneRuntime.py", "--state", "./demo_state", "--stdio"],
    stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, encoding="utf-8"
)

def call(obj):
    p.stdin.write(json.dumps(obj, ensure_ascii=False) + "\n")
    p.stdin.flush()
    return json.loads(p.stdout.readline())

print(call({"cmd":"init","texts":["王女は城にいる。","勇者は村にいる。"]}))
print(call({"cmd":"observe","text":"勇者が城に来た。"}))
print(call({"cmd":"choose","context":"勇者が城に来た。","candidates":["ようこそ。","帰ってください。"]}))
p.terminate()
