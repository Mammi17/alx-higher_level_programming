#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays
thevalue of the variable X-Request-Id in the response header"""


import sys
import requests

if __name__ == "__main__":
    with requests.get(sys.argv[1]) as resp:
        x_request_id = resp.headers.get('X-Request-Id')
        print(x_request_id)
