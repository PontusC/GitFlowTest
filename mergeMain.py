import subprocess

def runCommand(command):
    try:
        result = subprocess.run(command)
        return result.stdout
    except Exception as e:
        return f"Error: {e}"

# Switches from develop branch to release branch
runCommand("git checkout main")
# Merges current branch (release) into specified branch (main)
runCommand("git merge origin/release")
# Switches from develop branch to main branch
runCommand("git checkout main")
# Merges given branch (release) into specified branch (release)
runCommand("git merge release")