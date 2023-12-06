#!/usr/bin/python3
def search_replace(my_list, search, replace):
    r_list = []
    for i in my_list:
        if i == search:
            r_list.append(replace)
        else:
            r_list.append(i)
    return r_list
