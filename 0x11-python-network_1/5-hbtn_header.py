#!/usr/bin/python3
"""
Take in a URL, send a request to the URL, and displays the
value of the X-Request-Id variable found in the header of the
response using requests
"""
import requests
from sys import argv


if __name__ == "__main__":
    """Take in a URL, sends a request to the URL, and displays
    the value of the X-Request-Id variable found in the header
    of the response using requests"""
    r = requests.get(argv[1])
    try:
        r_id = r.headers['X-Request-Id']
        print(r_id)
    except KeyError:
        pass


