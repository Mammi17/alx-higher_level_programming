#!/usr/bin/python3
"""script that takes 2 arguments in order to solve this challenge."""


import requests
import sys


if __name__ == '__main__':
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    paginate = {'per_page': 10}
    res = requests.get(url, params=paginate)

    if res.status_code == 200:
        commits = res.json()

        for commit in commits:
            sha = commit['sha']
            author = commit['commit']['author']['name']
            print(f'{sha}: {author}')
    else:
        pass
        # print('Error:', res.status_code)
