#!/usr/bin/python3

""" This module fetches https://alx-intranet.hbtn.io/status
using the < urllib > module

"""

if __name__ == "__main__":

    from urllib import request

    URL = "https://alx-intranet.hbtn.io/status"

    with request.urlopen(URL) as res:
        data = res.read()

    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
    print("\t- utf8 content: {}".format(data.decode()))
