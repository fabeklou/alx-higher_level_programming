#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response
test $(curl -X GET -I "$1" -s | grep HTTP/ | cut -d ' ' -f 2) -eq 200 && curl -X GET "$1" -s
