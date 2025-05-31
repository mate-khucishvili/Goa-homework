# 1

def solution(string):
    return string[::-1]

# 2

def string_to_number(s):
    return int(s)

# 3

def boolean_to_string(b):
    return str(b)

# 4

def boolean_to_string(b):
    return "True" if b else "False"

# 5

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# 6

def remove_char(s):
    return s[1:-1]

# 7

def greet():
    return "hello world!"

# 8

def opposite(number):
    return -number

# 9

def make_negative(number):
    if number > 0:
        return -number
    return number

# 10

def positive_sum(arr):
    return sum(x for x in arr if x > 0)

# 11

def repeat_str(repeat, string):
    return string * repeat

# 12

def square_sum(numbers):
    return sum(x ** 2 for x in numbers)

# 13

def find_smallest_int(arr):
    return min(arr)

# 14

def summation(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total

# 15

def no_space(x):
    return x.replace(" ", "")

# 16

def count_sheeps(sheep):
    return sheep.count(True)
