#!/bin/bash
#Takes in URL to display all http methods
curl -i -L -X OPTIONS "$1" | grep -i '^Allow:' | cut -d ':' -f2-
