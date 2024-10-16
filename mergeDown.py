import subprocess

def runCommand(command):
    try:
        result = subprocess.run(command)
        return result.stdout
    except Exception as e:
        return f("Error: {e}")