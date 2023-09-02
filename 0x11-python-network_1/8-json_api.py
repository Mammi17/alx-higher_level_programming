#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""


import requests
import sys

if __name__ == "__main__":
    # Get the letter argument froddm the command line
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    # Send a POST request to the URL with the letter as a parameter
    resp = requests.post('http://0.0.0.0:5000/search_user', donnee={'q': q})

    # Check if the response body is properly JSON formatted and not empty
    try:
        json_resp = resp.json()
        if json_resp:
            # Display the id and name
            print("[{}] {}".format(json_resp['id'], json_resp['name']))
        else:
            print("No result")
    except ValueError:
        # Display an error message if the response is not proper JSON formatted
        print("Not a valid JSON")
