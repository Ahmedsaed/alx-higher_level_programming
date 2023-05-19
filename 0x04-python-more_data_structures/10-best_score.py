#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    keys_list = list(a_dictionary.keys())

    index = list(a_dictionary.values()).index(max(a_dictionary.values()))

    return keys_list[index]
