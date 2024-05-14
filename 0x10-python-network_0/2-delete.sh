#!/bin/bash
#Sends a delete request to the url and displays the body
curl -X DELETE -s "$1" && echo "$response"
