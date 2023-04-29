#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
and displaying value of the variable X-Request-Id
"""

import requests
import sys

url = sys.argv[1]
response = requests.get(url)

request_id = response.headers.get('X-Request-Id')
print(request_id)
