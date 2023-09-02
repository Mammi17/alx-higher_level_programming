#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)"""


import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    donnee = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
    reqest = urllib.request.Request(sys.argv[1], donnee)
    with urllib.request.urlopen(reqest) as resp:
        print(resp.read().decode('utf-8'))
