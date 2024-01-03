import os
import subprocess

def update_github(username, token, repo_path):
  try:
    # Change to the repository directory
    os.chdir(repo_path)

    # Check if the repository is initialized
    if not os.path.isdir(os.path.join(repo_path, '.git')):
      # Initialize the repository if it's not already initialized
      subprocess.run(['git', 'clone', f'https://github.com/{username}/learn-python.git', repo_path])

    # Stash local changes
    subprocess.run(['git', 'stash'])

    # Set upstream branch explicitly
    subprocess.run(['git', 'branch', '--set-upstream-to=origin/master', 'master'])

    # Set Git credentials for the pull operation
    subprocess.run(['git', 'config', '--local', 'credential.helper', 'store'])
    subprocess.run(['git', 'config', '--local', f'credential.helper',
                    f'!f() {{ echo "username={username}\\password={token}"; }}; f'])

    # Pull the latest changes
    subprocess.run(['git', 'pull'])

    # Apply the stashed changes
    subprocess.run(['git', 'stash', 'apply'])

    print("Code updated successfully.")
  except subprocess.CalledProcessError as e:
    print(f"Error updating code: {e}")
  finally:
    os.chdir(os.path.expanduser("~"))

  # Example usage:


github_username = "zianitest"
github_token = "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"
repository_path = r"C:\Users\a\PycharmProjects\learn-python"

update_github(github_username, github_token, repository_path)
def function_name():

  return "Hello Python From Inside Function"

dataFromFunction = function_name()

print(dataFromFunction)



