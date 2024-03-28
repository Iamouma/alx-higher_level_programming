#!/usr/bin/python3
"""Script that takes in a URL and and sends a POST request to the passed URL"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}

    response = requests.post(url, data=data)
    print(response.text)
