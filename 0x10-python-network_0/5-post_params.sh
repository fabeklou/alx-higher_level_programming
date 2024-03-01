#!/bin/bash
# This script takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -X POST "$1" -s -H "Content-Type: application/x-www-form-urlencoded" -d "email=test@gmail.com&subject=I will always be here for PLD"
