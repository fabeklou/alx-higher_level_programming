#!/usr/bin/python3

"""This script takes 2 arguments in order to solve this challenge.

"""

if __name__ == "__main__":

    import requests
    import sys
    from pprint import pprint

    repo, owner = sys.argv[1:3]
    URL = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    res = requests.get(URL)

    commits = res.json()

    # json_res.sort(key=lambda x: x.get("commit").get("author").get("time"),
    #               reverse=True)

    for commit in commits[:10]:
        sha = commit.get("sha")
        name = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, name))
