#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
"""

import requests
import sys

url = sys.argv[1]
response = requests.get(url)

if response.status_code >= 400:
    print(f"Error code: {response.status_code}")
else:
    print(response.text)
