import subprocess

def runCommand(command):
    try:
        result = subprocess.run(command)
        return result.stdout
    except Exception as e:
        return f"Error: {e}"
    
# Creates a new branch "release" based on develop
print(runCommand("git branch release"))
# Pushes changes from develop to release
print(runCommand("git push origin release"))