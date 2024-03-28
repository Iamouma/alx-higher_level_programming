#!/usr/bin/python3
"""Script that takes in and sends a URL request"""

import sys
from urllib import request, error


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("UTF-8"))
    except error.HTTPError as er:
        print("Error code:", er.code)
