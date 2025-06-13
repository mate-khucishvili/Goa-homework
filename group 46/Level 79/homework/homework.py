# 1 Reversed Strings
def solution(string):
    return string[:: -1 ]
# 2 Sum Arrays
def sum_array(a):
    return sum(a)
# 3 Unique In Order
def unique_in_order(sequence):
    result = []
    nawili = object()  
    for i in sequence:
        if i != nawili:
            result.append(i)
            nawili = i
    return result
# 4 IP Validation
# https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/python
# გაუგებარი