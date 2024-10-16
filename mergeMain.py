import subprocess

def runCommand(command):
    try:
        result = subprocess.run(command)
        print(result)
        return result.stdout
    except Exception as e:
        return f"Error: {e}"

# Switches from develop branch to main branch
runCommand(['git', 'checkout', 'main'])
# Merges current branch (main) with specified branch (release)
runCommand(['git', 'merge', 'release', '-m"Merging relase into main"'])