#!/usr/bin/python3
"""displays the value of the X-Request-Id found in the header"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    header = response.info()
    print(header['X-Request-Id'])
