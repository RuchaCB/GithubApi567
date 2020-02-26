import unittest
from unittest import mock
import GitHubApi567 


class TestGitHubApi567(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    @mock.patch('GitHubApi567.u_commits')
    def testu_commits(self, mock_u_com): 
        mock_u_com.return_value = ["Repo: helloworld Number of commits: 6", "Repo: Mocks Number of commits: 10","Repo: Project1 Number of commits: 2","Repo: threads-of-life Number of commits: 1","Done"]
        expected = ["Repo: helloworld Number of commits: 6", "Repo: Mocks Number of commits: 10","Repo: Project1 Number of commits: 2","Repo: threads-of-life Number of commits: 1","Done"]
        gihub_id = "richkempinski"
        self.assertEqual(GitHubApi567.u_commits(gihub_id), expected)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
