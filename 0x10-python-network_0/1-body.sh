#!/bin/bash
# That takes in a URL, sends a GET request to the URL,
# displays the body of the response
curl -s "$1" -X GET -L
