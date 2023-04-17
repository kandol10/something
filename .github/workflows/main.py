from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Retrieve the raw content of the file from GitHub
    github_repo_owner = 'kandol10'
    github_repo_name = 'Something'
    github_file_path = 'index.html'
    response = requests.get(f'https://raw.githubusercontent.com/{github_repo_owner}/{github_repo_name}/main/{github_file_path}')

    # Return the content of the file to the client
    return response.content.decode('utf-8')

if __name__ == '__main__':
    app.run()
