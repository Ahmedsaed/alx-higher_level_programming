#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    rm_k = []

    for k, v in a_dictionary.items():
        if v == value:
            rm_k.append(k)

    for i in rm_k:
        a_dictionary.pop(i)

    return a_dictionary
