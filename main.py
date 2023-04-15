import requests

# Replace the placeholders below with your actual values
github_repo_owner = 'kandol10'
github_repo_name = 'Something'
github_file_path = 'index.html'

# Retrieve the raw content of the file from GitHub
response = requests.get(f'https://raw.githubusercontent.com/{github_repo_owner}/{github_repo_name}/main/{github_file_path}')

# Print the content of the file
print(response.content.decode('utf-8'))
