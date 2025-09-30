
```python
import unittest
from unittest.mock import patch
import github_api

class TestGitHubApiWithMocking(unittest.TestCase):

    @patch("github_api.requests.get")
    def test_get_repos_success(self, mock_get):
        # Simulate GitHub returning 2 repos
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"name": "repo1"}, {"name": "repo2"}]

        repos = github_api.get_repos("fakeuser")
        self.assertEqual(repos, ["repo1", "repo2"])

    @patch("github_api.requests.get")
    def test_get_commit_count_success(self, mock_get):
        # Simulate GitHub returning 3 commits
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"sha": "1"}, {"sha": "2"}, {"sha": "3"}]

        count = github_api.get_commit_count("fakeuser", "repo1")
        self.assertEqual(count, 3)

    @patch("github_api.requests.get")
    def test_get_repos_user_not_found(self, mock_get):
        # Simulate GitHub returning 404
        mock_get.return_value.status_code = 404

        with self.assertRaises(Exception):
            github_api.get_repos("unknownuser")

if __name__ == "__main__":
    unittest.main()
```
