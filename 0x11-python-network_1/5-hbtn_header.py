#!/usr/bin/python3
""" takes in a URL, sends a request to the
URL and displays the value of the variable
X-Request-Id in the response header"""

import requests
import sys

if __name__ == "__main__":
    url = argv[1]

response = requests.get(url)
x = response.headers.get("X-Request-Id")
print(x)
