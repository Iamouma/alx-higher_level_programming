#!/usr/bin/python3
"""Script takes letter and sends a POST request"""

import sys
import requests


if __name__ == "__main__":
    num = "" if len(sys.argv) == 1 else sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"

    data = {'q': num}

    response = requests.post(url, data=data)

    try:
        p_response = response.json()

        if p_response == {}:
            print("No result")
        else:
            print("[{}] {}".format(p_response.get(
                "id"), p_response.get("name")))
    except ValueError:
        print("Not a valid JSON")
