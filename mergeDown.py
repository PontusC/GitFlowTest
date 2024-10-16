import subprocess

def runCommand(command):
    try:
        result = subprocess.run(command)
        return result.stdout
    except Exception as e:
        return f"Error: {e}"

# Switches to relase branch and pulls changes from main
runCommand("git checkout release")
runCommand("git merge origin/main")
# Switches to develop branch and pulls changes from main
runCommand("git merge develop")
runCommand("git merge origin/main")