import requests

# Replace the placeholders below with your actual values
github_repo_owner = 'your-github-username'
github_repo_name = 'Something'
github_file_path = 'main/a'

# Retrieve the raw content of the file from GitHub
response = requests.get(f'https://raw.githubusercontent.com/{github_repo_owner}/{github_repo_name}/main/a')

# Print the content of the file
print(response.content.decode('utf-8'))
