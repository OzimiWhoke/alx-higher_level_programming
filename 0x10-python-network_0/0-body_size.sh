#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL, 
# and displays the size of the body of the response using curl

echo "Enter the URL:"
read url

size=$(curl -s -o /dev/null -w '%{size_download}' "$url")

echo "The size of the response body is $size bytes."
