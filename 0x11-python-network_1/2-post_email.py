#!/usr/bin/python3

"""This module takes in a URL and an email,
sends a POST request to the passed URL with
the email as a parameter, and displays
the body of the response (decoded in utf-8)

"""

if __name__ == "__main__":

    from urllib import request, parse
    import sys

    url, email = sys.argv[1:3]

    values = {"email": email}
    data = parse.urlencode(values).encode('ascii')

    req = request.Request(url, data)

    with request.urlopen(req) as res:
        print(res.read().decode())
