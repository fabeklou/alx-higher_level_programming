#!/usr/bin/python3

"""This module takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response.

"""

if __name__ == "__main__":

    from urllib import request
    import sys

    url = sys.argv[1]
    VAR = "X-Request-Id"

    with request.urlopen(url) as res:
        header = res.info()

    print(header.get(VAR))
