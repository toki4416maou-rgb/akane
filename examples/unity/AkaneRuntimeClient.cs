using System;
using System.Diagnostics;
using System.IO;
using System.Threading.Tasks;

public sealed class AkaneRuntimeClient : IDisposable
{
    private readonly Process process;
    private readonly StreamWriter input;
    private readonly StreamReader output;

    public AkaneRuntimeClient(string exePath, string stateDir)
    {
        process = new Process();
        process.StartInfo = new ProcessStartInfo {
            FileName = exePath,
            Arguments = $"--state \"{stateDir}\" --stdio",
            UseShellExecute = false,
            RedirectStandardInput = true,
            RedirectStandardOutput = true,
            CreateNoWindow = true,
            StandardInputEncoding = System.Text.Encoding.UTF8,
            StandardOutputEncoding = System.Text.Encoding.UTF8
        };
        process.Start();
        input = process.StandardInput;
        output = process.StandardOutput;
    }

    public async Task<string> CallJsonAsync(string json)
    {
        await input.WriteLineAsync(json);
        await input.FlushAsync();
        return await output.ReadLineAsync();
    }

    public void Dispose()
    {
        try { if (!process.HasExited) process.Kill(); } catch { }
        process.Dispose();
    }
}
