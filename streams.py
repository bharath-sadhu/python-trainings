#We can read inputs from command line using input method

#name = input("Please enter your name: ")
#print(name)


#reading environment variables
import os
print(os.environ)
print(os.environ.get('TEST_PYTHON'))

#echo $? to see status


import subprocess

# subprocess module to run shell commands where return is not necessary
#parent process(wait state) -> <- child process synchronously
# parent process will know whether child process
# has succesfully excuted or ot seeing exit code of child process

result = subprocess.run(["date"])
print(result.returncode)

result = subprocess.run(["cat", "does_not_exist.txt"])
print(result.returncode)


result = subprocess.run(["hostname"], capture_output=True)
print(result.stdout)
print(result.returncode)

result = subprocess.run(["rm","does_not_exist.txt"], capture_output=True)
print(result.stdout)
print(result.returncode)
print(result.stderr)
