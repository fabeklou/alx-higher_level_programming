#!/usr/bin/python3

"""This module takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).

"""

if __name__ == "__main__":

    from urllib import request, parse, error
    import sys

    url = sys.argv[1]

    try:
        with request.urlopen(url) as res:
            print(res.read().decode())
    except (error.HTTPError, error.URLError) as err:
        print("Error code: {}".format(err.code))
