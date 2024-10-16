import subprocess

def runCommand(command):
    try:
        result = subprocess.run(command)
        print(result)
        return result.stdout
    except Exception as e:
        return f"Error: {e}"
    
# Creates a new branch "release" based on develop
runCommand("git branch release")
# Pushes changes from develop to release
runCommand(['git', 'checkout', 'release'])
runCommand(['git', 'merge', 'develop', '-m"Merging develop into release"'])