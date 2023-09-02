#!/usr/bin/python3
"""a script that fetches https://alx-intranet.hbtn.io/status"""


import urllib.request

addres = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":
    with urllib.request.urlopen(addres) as answer:
        html = answer.read()
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content:", html.decode("utf-8"))
