import subprocess
import sys

# Answer to Part 1.
proc = subprocess.run([sys.executable, "..\Starter\client.py", "C:\labs\words"])
print(f"Child exited with return code {proc.returncode}")

# Answer to Part 2.
proc = subprocess.run([sys.executable, "..\Starter\client.py", "C:\labs\words"],
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if proc.stdout:
    lines = proc.stdout.splitlines()
    print(proc.stdout.decode()) # Decode into Unicode
    print(f"Number of lines = {len(lines)}")

if proc.stderr:
    print("error:", proc.stderr.decode())


