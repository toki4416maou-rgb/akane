const path = require('path');
const { spawn } = require('child_process');
const readline = require('readline');

const runtime = path.join(process.resourcesPath || __dirname, 'AkaneRuntime.exe');
const child = spawn(runtime, [], { stdio: ['pipe', 'pipe', 'pipe'], windowsHide: true });
const lines = readline.createInterface({ input: child.stdout });

let ready = false;
const pending = [];
lines.on('line', (line) => {
  const msg = JSON.parse(line);
  if (msg.event === 'ready') {
    ready = true;
    return;
  }
  const next = pending.shift();
  if (next) next.resolve(msg);
});

function call(request) {
  return new Promise((resolve, reject) => {
    if (!ready) return reject(new Error('AkaneRuntime not ready'));
    pending.push({ resolve, reject });
    child.stdin.write(JSON.stringify(request) + '\n');
  });
}

async function shutdown() {
  if (!ready) return;
  try { await call({ cmd: 'runtime_exit' }); } catch (_) {}
  child.stdin.end();
}

module.exports = { call, shutdown };
