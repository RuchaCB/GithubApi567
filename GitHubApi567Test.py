import unittest
from unittest import mock
import GitHubApi567


class TestGitHubApi567(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testu_commits(self): 
        total = 0
        l_1=[]
        for repo, num in GitHubApi567.u_commits('richkempinski'):
            l_1.append("Repo: %s Number of commits: %d" % (repo, num))
            total += num 
        l_1.append("Done")
        self.assertEqual(l_1,["Repo: helloworld Number of commits: 6", "Repo: Mocks Number of commits: 10","Repo: Project1 Number of commits: 2","Repo: threads-of-life Number of commits: 1","Done"])
    
    @mock.patch('GitHubApi567.u_commits')
    def mock_u_commits(self, mock_u_com):
        print(mock_u_com)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
