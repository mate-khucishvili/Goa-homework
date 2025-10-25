# Codewars 8 kuy
# 1 - Did she say hallo?
def validate_hello(greetings):
    greetings = greetings.lower()
    words = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    for i in words:
        if i in greetings:
            return True
    return False
# 2 - Who ate the cookie?
def cookie(x):
    if type(x) == str:
        return "Who ate the last cookie? It was Zach!"
    elif type(x) in [int, float]:
        return "Who ate the last cookie? It was Monica!"
    else:
        return "Who ate the last cookie? It was the dog!"

# 3 - Grader
def grader(score):
    if score > 1 or score < 0:
        return "F"
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"

# 4 - 5 without numbers !!
def unusual_five():
    return(len('Goooa'))

# Codewars 7 kyu
# 1 - Exes and Ohs
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

# 2 - Sum of two lowest positive integers
def sum_two_smallest_numbers(num_list):
    num_list.sort()
    return num_list[0] + num_list[1]

# 3 - Complementary DNA
def DNA_strand(dna):
    res = ""
    for i in dna:
        if i == "A":
            res += "T"
        elif i == "T":
            res += "A"
        elif i == "C":
            res += "G"
        elif i == "G":
            res += "C"
    return res


# Codewars 6 kyu
# 1 - Find the odd int
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 !=0:
            return i