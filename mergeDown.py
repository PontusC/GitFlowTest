import subprocess

def runCommand(command):
    try:
        result = subprocess.run(command)
        return result.stdout
    except Exception as e:
        return f"Error: {e}"

# Switches to main branch
runCommand("git checkout origin/main")
# Merges current branch (main) to release and develop
runCommand("git merge origin/release")
runCommand("git merge origin/develop")