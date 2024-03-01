#!/bin/bash
# This script sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -X GET "$1" -s -I | grep HTTP | cut -d ' ' -f 2
