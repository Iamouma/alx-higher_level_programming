#!/usr/bin/python3
def best_score(a_dictionary):
    if type(a_dictionary) is not dict or len(a_dictionary) == 0:
        return None
    biggest = list(a_dictionary.keys())[0]
    biggernum = a_dictionary[biggest]
    for i, k in a_dictionary.items():
        if k > biggernum:
            biggernum = k
            biggest = i
    return biggest
