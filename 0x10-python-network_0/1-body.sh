#!/bin/bash
# That takes in a URL, sends a GET request to the URL,
# displays the body of the response
curl -sL -o /dev/null -w "%{response_code}\n" "$1" | [ $(cat) = "200" ] && curl -sL -X "GET" "$1"
