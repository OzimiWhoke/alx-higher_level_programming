#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = {i for i in my_list}
    result = 0
    for i in new_list:
        result += i
    return result
