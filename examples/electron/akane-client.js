const { spawn } = require('child_process');
const readline = require('readline');

class AkaneClient {
  constructor(exe, stateDir) {
    this.proc = spawn(exe, ['--state', stateDir, '--stdio'], { windowsHide: true });
    this.rl = readline.createInterface({ input: this.proc.stdout });
    this.pending = [];
    this.rl.on('line', line => {
      const msg = JSON.parse(line);
      if (msg.event === 'ready') return;
      const resolve = this.pending.shift();
      if (resolve) resolve(msg);
    });
  }
  call(payload) {
    return new Promise(resolve => {
      this.pending.push(resolve);
      this.proc.stdin.write(JSON.stringify(payload) + '\n');
    });
  }
}
module.exports = AkaneClient;
