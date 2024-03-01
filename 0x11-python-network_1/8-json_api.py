#!/usr/bin/python3

"""This script takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.

"""

if __name__ == "__main__":

    import requests
    import sys

    URL = "http://0.0.0.0:5000/search_user"
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    res = requests.post(URL, data=payload)
    json_res = res.json()

    if not json_res:
        print("No result")
    elif isinstance(json_res, str):
        print("Not a valid JSON")
    else:
        print("[{}] {}".format(json_res.get("id"), json_res.get("name")))
