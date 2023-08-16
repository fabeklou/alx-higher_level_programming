#!/usr/bin/python3

def roman_to_int(roman_string):
    result: int = 0
    i: int = 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    if not isinstance(roman_string, str) or roman_string is None:
        return result
    while i < len(roman_string):
        if i < len(roman_string) - 1:
            if roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]:
                result += roman_dict.get(roman_string[i + 1], 0) - \
                    roman_dict.get(roman_string[i], 0)
                i += 2
                continue
        result += roman_dict.get(roman_string[i], 0)
        i += 1
    return result
