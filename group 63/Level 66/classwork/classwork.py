# ---  Easy Codewars 8 kuy -----

# 1 - Is the string uppercase?
def is_uppercase(inp):
    for mozgi in inp:
        if mozgi.isalpha() and mozgi.islower():
            return False
    return True

# 2 - Grasshopper - Terminal game move function
def move(position, roll):
    return position + roll * 2
# ----- Easy Codewars 7 kyu: ------

# 1 - Disemvowel Trolls
def disemvowel(string_):
    words = "aeiouAEIOU"
    res = ""
    for mozgi in string_:
        if mozgi not in words:
            res += mozgi
    return res

# 2 - Exes and Ohs
def xo(s):
    s = s.lower()
    return s.count("o") == s.count("x")

# ----  Hard Codewars 8 kuy: -----

# 1 - Grasshopper - Summation
def summation(num):
    sum = 0
    for mozgi in range(1,num + 1):
        sum += mozgi
    return sum
    

# ------ Hard Codewars 7 kuy: -----

# 1 - Convert number to reversed array of digits
def digitize(n):
    digits = []
    if n == 0:
        digits.append(0)
    else:
        while n > 0:
            digits_1 = n % 10
            digits.append(digits_1)
            n = n // 10
    return digits

# ------------ Boss Level ------------

# 1 - max diff - easy
def max_diff(lst):
    if len(lst) < 2:
        return 0
    return max(lst) - min(lst)