#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""


import requests

if __name__ == "__main__":
    answer = requests.get("https://alx-intranet.hbtn.io/status")
    if answer.status_code == 200:
        print("Body response:")
        print("\t- type: {}".format(type(answer.text)))
        print("\t- content: {}".format(answer.text))
    else:
        print("Error fetching {}: {}".format(url, answer.status_code))
