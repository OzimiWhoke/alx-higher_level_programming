#!/bin/bash
#  a Bash script that takes in a URL, 
# sends a GET request to the URL, 
# and displays the body of the response using curl

echo "Enter the URL:"
read url

response=$(curl -s -o /dev/null -w "%{http_code}" "$url")
if [[ "$response" -eq "200" ]]; then
  body=$(curl -s "$url")
  echo "$body"
else
  echo "Error: Response status code was not 200"
fi
