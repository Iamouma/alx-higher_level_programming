#!/usr/bin/python3
def magic_calculation(a, b):
    len = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise ValueError("Value of i is too large")
            else:
                len += (a ** b) / i
        except ValueError:
            len = b + a
            break
    return len
