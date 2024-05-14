#!/bin/bash

#Takes in a URL then displays the body size in bytes
response=$(curl -s -o /tmp/response.txt -w "%{size_download}" "$1")

echo "$response"

rm /tmp/response.txt >/dev/null 2>&1
