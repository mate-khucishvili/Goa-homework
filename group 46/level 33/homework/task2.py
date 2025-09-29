# 1

def modify_list():
    my_list = [1, 2, 3, 4, 5]
    my_list.pop(2)
    my_list.insert(0, 10)
    return my_list

# 2

def power(base, exponent):
    return base ** exponent

# 3

def list_length(lst):
    if len(lst) % 2 == 0:
        return "List length is even"
    else:
        return "List length is odd"


