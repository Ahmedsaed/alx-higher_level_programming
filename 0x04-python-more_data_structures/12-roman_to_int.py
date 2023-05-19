#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0

    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    nums = [roman_dict[x] for x in roman_string]

    for i in range(len(nums)):
        result += nums[i]
        if nums[i - 1] < nums[i] and i != 0:
            result -= nums[i - 1] * 2

    return result
