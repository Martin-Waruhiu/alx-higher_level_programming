#!/usr/bin/python3
"""takes in a URL and an email address, 
sends a POST request to the passed URL with the email 
as a parameter, and finally displays the body of the response."""

import requests
import sys

if __name__ == "__main__":
    url = argv[1]
    value  = {"Email": argv[2]}
    response = requests.post(url, data=value)
    print(response.text)
