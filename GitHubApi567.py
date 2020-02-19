import json
import requests

def r_commits(url, _a=0):
    r = requests.get(url)
    commits = r.json()
    num = len(commits)
    if num == 0:
        return _a
    link = r.headers.get('link')
    if link is None:
        return _a + num 
    new_link = r.headers['link']
    for l in new_link.split(','):
        s_1, s_2 = l.split(';')
        if s_2.strip() == 'rel="next"':
            new = s_1.strip()[1:-1]
    if new is None:
        return _a + num 
    return r_commits(new, _a + num)

def u_commits(user):
    r = requests.get('https://api.github.com/users/%s/repos' % user)
    repos = r.json()
    for repo in repos:
        if repo['fork'] is True:
            continue
        num = r_commits(repo['url'] + '/commits')
        yield (repo['name'], num)

if __name__ == '__main__':
    total = 0
    for repo, num in u_commits('richkempinski'):
        print ("Repo: %s Number of commits: %d" % (repo, num))
        total += num 
    print ("Done")
