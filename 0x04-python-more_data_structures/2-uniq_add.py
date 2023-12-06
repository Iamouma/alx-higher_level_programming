#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = []
    sum = 0
    for i in my_list:
        if i in uniq:
            sum += 1
            uniq.append(i)
    return sum
