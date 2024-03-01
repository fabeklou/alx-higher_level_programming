#!/usr/bin/python3

"""This script takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.

"""

if __name__ == "__main__":

    import requests
    import sys

    url, email = sys.argv[1:3]
    values = {"email": email}

    res = requests.post(url, data=values)

    print(res.text)
