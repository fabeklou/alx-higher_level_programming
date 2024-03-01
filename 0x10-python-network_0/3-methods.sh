#!/bin/bash
# This script takes in a URL and displays all HTTP methods the server will accept.
curl -X GET "$1" -sI | grep Allow | cut -d ':' -f 2-
