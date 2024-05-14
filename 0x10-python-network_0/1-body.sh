#!/bin/bash

#Takes in a URL and sends a get request and displays response body

if ! [[ "$1" =~ ^https?:// ]]; then
    url="http://$1"
else
    url="$1"
fi

response=$(curl -s -w "%{http_code}" -o /tmp/response.txt "$1")

status_code=$(tail -c 3 /tmp/response.txt)

if [ "$status_code" = "200" ];
then
	cat /tmp/response.txt
fi

rm /tmp/response.txt >/dev/null 2>&1
