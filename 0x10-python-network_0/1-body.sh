#!/bin/bash
#Takes in a URL and sends a get request and displays response body
curl -s "$1" | grep -Eo '(^HTTP.*\n)*' 
