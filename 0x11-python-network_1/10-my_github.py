#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""


import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    """sys.argv[1] = repo owner and sys.argv[2] = owner[repo]"""
    basic_auth = HTTPBasicAuth(argv[1], argv[2])
    reqest = requests.get("https://api.github.com/user", auth=basic_auth)
    print(reqest.json().get("id"))
