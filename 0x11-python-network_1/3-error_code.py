#!/usr/bin/python3
"""Takes in a url displays its body and handles errors as well"""

import sys
import urllib.request
from urllib.error import HTTPError

if __name__ == "__main__":
url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
    content = response.read().decode('utf-8')
    print(content)
except HTTPError as e:
    print(f"Error code:{e.code}")
