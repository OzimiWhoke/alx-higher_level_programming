#!/bin/bash
# sends a request to a URL passed as an argument, and displays only the status code of the response using curl
curl -o /dev/null -s -w "%{http_code}" "$1"
