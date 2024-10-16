import subprocess

def runCommand(command):
    try:
        result = subprocess.run(command)
        print(result)
        return result.stdout
    except Exception as e:
        return f"Error: {e}"

# Switches to release
runCommand(['git', 'checkout', 'release'])
# Merges current branch (main) with specified branch (release)
runCommand(['git', 'merge', 'main', '-m"Merging main into release"'])
# Switches to develop
runCommand(['git', 'checkout', 'develop'])
# Merges current branch (main) with specified branch (release)
runCommand(['git', 'merge', 'main', '-m"Merging main into develop"'])




