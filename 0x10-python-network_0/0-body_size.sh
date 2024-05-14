#!/bin/bash
# Takes in a URL then displays the body size in bytes
curl -s -o /tmp/response.txt -w "%{size_download}" "$1" && cat /tmp/response.txt; rm /tmp/response.txt >/dev/null 2>&1
