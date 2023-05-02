#!/bin/bash
# sends a JSON POST request to a URL using curl

curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
