import subprocess

result = subprocess.run(["rm","does_not_exist.txt"], capture_output=True)
print(result.stdout)
print(result.returncode)
print(result.stderr.decode('utf8'))