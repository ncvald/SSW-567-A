import requests

def get_repos(user):
    """Return list of repository names for a given GitHub user."""
    url = f"https://api.github.com/users/{user}/repos"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching repos for user {user}. Status code: {response.status_code}")
    repos = response.json()
    return [repo["name"] for repo in repos]

def get_commit_count(user, repo):
    """Return number of commits for a given repo of a GitHub user."""
    url = f"https://api.github.com/repos/{user}/{repo}/commits"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching commits for repo {repo}. Status code: {response.status_code}")
    commits = response.json()
    return len(commits)

def get_user_repo_commits(user):
    """Return dictionary of {repo: commit_count} for given GitHub user."""
    repos = get_repos(user)
    results = {}
    for repo in repos:
        commits = get_commit_count(user, repo)
        results[repo] = commits
    return results

if __name__ == "__main__":
    user_id = input("Enter GitHub user ID: ")
    try:
        repo_commits = get_user_repo_commits(user_id)
        for repo, count in repo_commits.items():
            print(f"Repo: {repo} Number of commits: {count}")
    except Exception as e:
        print(f"Error: {e}")
