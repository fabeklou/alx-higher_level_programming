#!/bin/bash
# This script makes a request that causes the server to respond with a message containing You got me!, in the body of the response.
curl -X PUT 0.0.0.0:5000/catch_me -sL -H "Origin: HolbertonSchool" -d "user_id=98"
