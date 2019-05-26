using System;
using System.Diagnostics;
using System.IO;
using System.Threading;

namespace ServerTester {
internal class Program {
	public static void Main(string[] args) {
		Environment.SetEnvironmentVariable("PYTHONPATH",
			$"{Environment.GetEnvironmentVariable("PYTHONPATH")};{new FileInfo(args[0]).Directory.Parent.FullName}");
		Process p = new Process {
			StartInfo = new ProcessStartInfo("python", Path.GetFullPath(args[0]))
				{RedirectStandardOutput = true, UseShellExecute = false, RedirectStandardError = true}
		};

		p.Start();
		Thread.Sleep(20000);
		if (!p.HasExited) {
			p.Kill();
		}

		while (!p.StandardError.EndOfStream) {
			string readLine = p.StandardError.ReadLine();
			Console.WriteLine(readLine);
			if (readLine.Contains(" * Running on")) {
				Environment.Exit(0);

			}

			Environment.Exit(-1);

		}
	}
}
}