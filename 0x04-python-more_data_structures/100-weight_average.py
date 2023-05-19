#!/usr/bin/python3

def weight_average(my_list=[]):
    nom, denom = 0, 0

    if not my_list or not len(my_list):
        return 0

    for i in my_list:
        nom += i[0] * i[1]

    for i in my_list:
        denom += i[1]

    return nom / denom
