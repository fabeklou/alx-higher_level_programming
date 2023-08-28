#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    my_new_list: list = []
    element: int = 0
    for idx in range(list_length):
        try:
            element = my_list_1[idx] / my_list_2[idx]
        except (TypeError, ValueError):
            print("{}".format("wrong type"))
            element = 0
        except ZeroDivisionError:
            print("{}".format("division by 0"))
            element = 0
        except IndexError:
            print("{}".format("out of range"))
            element = 0
        finally:
            my_new_list.append(element)
    return my_new_list
