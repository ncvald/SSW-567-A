
import unittest
from unittest.mock import patch
import github_api

class TestGitHubApi(unittest.TestCase):

    @patch("github_api.requests.get")
    def test_get_repos_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        repos = github_api.get_repos("someuser")
        self.assertEqual(repos, ["repo1", "repo2"])

    @patch("github_api.requests.get")
    def test_get_commit_count_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"sha": "1"}, {"sha": "2"}]
        count = github_api.get_commit_count("someuser", "repo1")
        self.assertEqual(count, 2)

    @patch("github_api.requests.get")
    def test_get_repos_user_not_found(self, mock_get):
        mock_get.return_value.status_code = 404
        with self.assertRaises(Exception):
            github_api.get_repos("unknownuser")

if __name__ == "__main__":
    unittest.main()