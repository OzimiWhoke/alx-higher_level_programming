#!/bin/bash
# displays the size(in bytes) of the body of the response using curl of a given URL

curl -s "$1" | wc -c
