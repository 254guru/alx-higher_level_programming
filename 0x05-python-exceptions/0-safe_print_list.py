#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for item in my_list:
            if count < x:
                print(item, end=' ')
                count += 1
            else:
                break
    except Exception as e:
        pass
    finally:
        print("")
    return count
