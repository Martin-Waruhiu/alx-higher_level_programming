#!/usr/bin/python3
""" script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter."""

import requests
import sys

if __name__ == '__main__':

    if argv.length != 2:
        q = ""
    else:
        q = argv[1]

    payload = {"q":q}
    url = "http://0.0.0.0:5000/search_user"
    requests.post(url, data = payload)

    try:
        data = response.json()
         if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

