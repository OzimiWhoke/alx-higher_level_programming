#!/usr/bin/python3
"""
a Python script that takes in a URL, 
sends a request to the URL and 
displays the value of the X-Request-Id
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)
