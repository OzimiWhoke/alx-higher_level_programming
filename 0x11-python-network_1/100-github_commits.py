#!/usr/bin/python3
"""
evaluates candidates applying for a back-end position with 
multiple technical challenges
"""

import requests
import sys

# Check if the correct number of arguments were provided
if len(sys.argv) != 3:
    print("Usage: python3 {} <repo_name> <owner_name>".format(sys.argv[0]))
    sys.exit(1)

# Get the repository name and owner name from the command-line arguments
repo_name = sys.argv[1]
owner_name = sys.argv[2]

# Construct the URL for the API request
url = "https://api.github.com/repos/{}/{}/commits".format(owner_name, repo_name)

# Make the API request
response = requests.get(url)

# Check if the API request was successful
if response.status_code != 200:
    print("Error: Could not retrieve commits.")
    sys.exit(1)

# Parse the JSON response and extract the commit information
commits = response.json()
for commit in commits[:10]:
    sha = commit["sha"]
    author_name = commit["commit"]["author"]["name"]
    print("{}: {}".format(sha, author_name))
