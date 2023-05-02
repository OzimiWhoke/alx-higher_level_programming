#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept using curl

curl -s -I -X OPTIONS "$url" | grep -i allow
