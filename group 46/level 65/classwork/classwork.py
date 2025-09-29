# 1 - Exclamation marks series #2: Remove all exclamation marks from the end of sentence

def remove(st):
    while st and st[-1] == "!":
        st = st[:-1]
    return st

# 2 - Fix the loop!
def list_animals(animals):
    lst = ''
    for i in range(len(animals)):
        lst += str(i + 1) + '. ' + animals[i] + '\n'
    return lst


# 3 - Find the Integral
def integrate(coefficient, exponent):
    new_exponent = exponent + 1
    new_coefficient = coefficient // new_exponent
    return f"{new_coefficient}x^{new_exponent}"

# 4 - Breaking chocolate problem
def breakChocolate(n, m):
    if n > 0 and m > 0:
        return m*n - 1
    else:
        return 0
    
# 5 - Anagram Detection
def is_anagram(test, original):
    return sorted(original.lower()) == sorted(test.lower())

# 6 - Are the numbers in order?
def in_asc_order(arr):
    return arr == sorted(arr)

# 7 - Flatten and sort an array
def flatten_and_sort(array):
    new_list= []
    for i in array:
        new_list += i 
    return sorted(new_list)