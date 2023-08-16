#!/usr/bin/python3

def weight_average(my_list=[]):
    average, mul_sum, sec_sum = 0, 0, 0
    if my_list:
        for val1, val2 in my_list:
            mul_sum += val1 * val2
            sec_sum += val2
        average = mul_sum / sec_sum
    return average
