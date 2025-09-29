# 1 - Binary Addition
def add_binary(a, b):
    return bin(a + b)[2:]

# 2 - Ones and Zeros
def binary_array_to_number(arr):
    result = 0
    n = len(arr)
    for i in range(n):
        result += arr[i] * (2 ** (n - 1 - i))
    return result
 
# 3 - Sort array by string length
def sort_by_length(arr):
    return sorted(arr, key=len)
 
 
# 4 - Count the Digit
def nb_dig(n, d):
    count = 0
    for k in range(n + 1):
        square = k * k
        count += str(square).count(str(d))
    return count

 
# 5 - Small enough? - Beginner
def small_enough(array, limit):
    all_equal = True
    for i in array:
        if i > limit:
            all_equal = False
            break
    return all_equal

 

# 6 - Sum of angles
def angle(n):
    return (n - 2) * 180

 
 
# 7 - Small enough? - Beginner
def small_enough(array, limit):
    all_equal = True
    for i in array:
        if i > limit:
            all_equal = False
            break
    return all_equal
 
 
# 8 - Sort the Gift Code
def sort_gift_code(code):
    return ''.join(sorted(code))

 
 
# 9 - Boiled Eggs
def cooking_time(eggs):
    return ((eggs + 7) // 8) * 5
 
 
# 10 - Divide and Conquer
def div_con(x):
    result = 0
    for i in x:
        if type(i) == int:
            result += i
        elif type(i) == str:
            result -= int(i)
    return result

 
 
# 11 - Smallest value of an array
def find_smallest(numbers, to_return):
    small_value = min(numbers)
    if to_return == "value":
        return small_value
    elif to_return == "index":
        return numbers.index(small_value)

 
 

# 12 - Digitize
def digitize(n):
    return [int(d) for d in str(n)]
 
# 13 - All unique
def has_unique_chars(string):
    item = set()
    for i in string:
        if i in item:
            return False
        item.add(i)
    return True

 
 
# 14 - Simple string characters
def solve(s):
    mayali = 0
    dabali = 0
    num = 0
    spec = 0
    
    for i in s:
        if i.isupper():
            mayali += 1
        elif i.islower():
            dabali += 1
        elif i.isdigit():
            num += 1
        else:
            spec += 1
    
    return [mayali, dabali, num, spec]

 
# 15 - 21 Sticks
def make_move(sticks):
    run = sticks % 4
    return run if run != 0 else 1

 


 
 
