#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request 
to http://0.0.0.0:5000/search_user
"""

import requests
import sys

if len(sys.argv) == 1:
    q = ""
else:
    q = sys.argv[1]

payload = {"q": q}
response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

try:
    data = response.json()
    if data:
        print("[{}] {}".format(data["id"], data["name"]))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")

