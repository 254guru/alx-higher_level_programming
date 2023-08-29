#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                value_1 = my_list_1[i]
                value_2 = my_list_2[i]
                if not (isinstance(value_1, (int, float)) and
                        isinstance(value_2, (int, float))):
                    result_list.append(0)
                    print("wrong type")
                elif value_2 == 0:
                    result_list.append(0)
                    print("division by 0")
                else:
                    result = value_1 / value_2
                    result_list.append(result)
            except IndexError:
                result_list.append(0)
                print("out of range")
    finally:
        return result_list
