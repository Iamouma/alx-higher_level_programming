#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    argc = len(argv)
    s_args = 0
    for index in range(argc - 1):
        s_args += int(argv[index + 1])
    print("{}".format(s_args))
