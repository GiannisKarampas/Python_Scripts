# Clone GitHub repositories of a user from a specific folder locally. 
import argparse
import os
import git

def clone_repo(owner, repo, destination_folder):
    # Clone the repository to the specific folder
    github_url_prefix = os.getenv('GITHUB_URL_PREFIX', 'https://github.com')
    repo_url = f'{github_url_prefix}/{owner}/{repo}.git'

    try:
        git.Repo.clone_from(f'{repo_url}', destination_folder)
        print(f"Repository cloned to {destination_folder}")
    except git.exc.GitCommandError as e:
        print(f"Error: {e}")

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Clone a GitHub repository to a specific folder.')
    parser.add_argument('owner', type=str, help='Owner of the GitHub repository')
    parser.add_argument('repo', type=str, help='Name of the GitHub repository')
    parser.add_argument('destination_folder', type=str, help='Destination folder for the cloned repository')
    args = parser.parse_args()

    # Clone the repository
    clone_repo(args.owner, args.repo, args.destination_folder)

if __name__ == "__main__":
    main()