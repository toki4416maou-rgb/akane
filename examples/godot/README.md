# Godot

Godotでは開発中は `AkaneRuntime.exe --http --host 127.0.0.1 --port 17831` を起動し、`HTTPRequest` から `/api` にPOSTするのが簡単です。
リリース時はゲーム起動時にRuntimeを子プロセスとして起動し、終了時に停止してください。
