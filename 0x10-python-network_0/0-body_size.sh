#!/bin/bash
# This script takes in a URL, sends a request to that URL,
# and displays the size of the body of the response

URL=$1

curl -X GET -I "$URL" -s | grep Content-Length | cut -d ' ' -f 2
