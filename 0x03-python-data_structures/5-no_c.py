#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for k in range(len(my_string)):
        if not (my_string[k] == 'c' or my_string[k] == 'C'):
            new_string += my_string[k]
            return (new_string)
