#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dict = {}
    for i in a_dictionary.items():
        n_dict.update({i[0]: i[1] * 2})
    return n_dict
