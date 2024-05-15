#!/bin/bash
#Takes in a URL and sends a get request and displays response body
status_code=$(curl -s -w "%{http_code}" -o /dev/null "$1"); [ "$status_code" = "200" ] && curl -s "$1" 
