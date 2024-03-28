#!/usr/bin/python3
"""A script that takes in and sends request to the URL"""

import sys
from urllib import request

if __name__ == "__main__":
    url = sys.argv[1]

    with request.urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))
