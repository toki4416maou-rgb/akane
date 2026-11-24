# Godot

Godot では開発中は `AkaneServer512.exe --http --host 127.0.0.1 --port 17831` を起動し、`HTTPRequest` から `/api` に POST するのが簡単です。
リリース時はゲーム起動時に Runtime を `--stdio` で子プロセスとして起動し、終了時に `runtime_exit` を送って停止してください。
