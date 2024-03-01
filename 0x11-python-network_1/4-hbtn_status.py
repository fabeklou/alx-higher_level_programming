#!/usr/bin/python3

"""This module fetches https://alx-intranet.hbtn.io/status

"""

if __name__ == "__main__":

    import requests

    URL = "https://alx-intranet.hbtn.io/status"

    res = requests.get(URL)
    data = res.text

    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
