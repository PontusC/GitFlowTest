import subprocess

def runCommand(command):
    try:
        result = subprocess.run(command)
        print(result)
        return result.stdout
    except Exception as e:
        return f"Error: {e}"

# Switches to relase branch and pulls changes from main
runCommand("git checkout release")
runCommand("git merge main -m'Merges main into release branch'")
# Switches to develop branch and pulls changes from main
runCommand("git merge develop")
runCommand("git merge main -m'Merges main into develop branch'")