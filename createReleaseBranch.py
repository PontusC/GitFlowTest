import subprocess

def runCommand(command):
    try:
        result = subprocess.run(command)
        return result.stdout
    except Exception as e:
        return f"Error: {e}"
    
# Creates a new branch "release" based on develop
runCommand("git branch release")
# Merges changes from develop into release
runCommand("git checkout release")
runCommand("git merge develop -m 'Merges develop branch into release'")