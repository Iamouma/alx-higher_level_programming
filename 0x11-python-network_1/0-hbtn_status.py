#!/usr/bin/python3
"""The script that grts the status of https://alx-intranet.hbtn.io/status using urllib"""

from urllib import request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with request.urlopen(url) as response:
        ropse = response.read()

        print("Body reponse:")
        print("\t- type: {}".format(type(ropse)))
        print("\t- content: {}".format(ropse))
        print("\t- utf8 content: {}".format(ropse.decode("utf-8")))
