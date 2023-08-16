#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    sorted_score = sorted([(value, key)
                          for key, value in a_dictionary.items()],
                          reverse=True)
    return sorted_score[0][1]
