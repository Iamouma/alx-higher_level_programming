#!/usr/bin/python3
def print_last_digit(number):
    end_digit = abs(number) % 10
    print(f"{end_digit:d}", end='')
    return(end_digit)
