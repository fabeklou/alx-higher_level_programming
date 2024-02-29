#!/bin/bash
# This script takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -X GET -I "$1" -s | grep Content-Length | cut -d ' ' -f 2
