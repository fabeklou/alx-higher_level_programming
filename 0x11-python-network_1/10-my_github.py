#!/usr/bin/python3

"""This script takes your GitHub credentials (username and password)
and uses the GitHub API to display your id

"""

if __name__ == "__main__":

    import requests
    import sys

    URL = "https://api.github.com/user"
    username, password = sys.argv[1:3]
    payload = requests.auth.HTTPBasicAuth(username, password)

    res = requests.get(URL, auth=payload)

    json_res = res.json()
    print(json_res.get("id"))
