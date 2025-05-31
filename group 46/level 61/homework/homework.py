# 1 - List Filtering
def filter_list(l):
    result = []
    
    for i in l:
        if isinstance(i, int):
            result.append(i)
    return result

# 2 - Exes and Ohs
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

# 3 - Shortest Word
def find_short(s):
    return min(len(i) for i in s.split())

# 4 - Friend or Foe?
def friend(x):
    friends = []
    
    for i in x:
        
        if len(i) == 4:
            
            friends.append(i)
    
    return friends

# 5 - Two to One
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))


# დამატებითი 5-ცალი 8kyu

# 1 - Multiply
def multiply(a, b):
    a * b

# 2 - Even or Odd
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# 3 - Convert a Number to a String!
def number_to_string(num):
    return(str(num))

# 4 - Reversed Strings
def solution(string):
    return string[:: -1 ]

# 5 - Return Negative
def make_negative(number):
    if number > 0:
        return -number
    return number



