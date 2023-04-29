#!/usr/bin/python3
"""
a Python script that takes in a URL and an email address, 
sends a POST request
"""

import requests
import sys

if __name__ == '__main__':
url = sys.argv[1]
email = sys.argv[2]

payload = {'email': email}
response = requests.post(url, data=payload)

print(response.text)
