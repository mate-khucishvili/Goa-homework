#1
# Expressions Matter

def expression_matter(a, b, c):
    return max(a*b*c, a+b+c, (a+b)*c, a*(b+c))


#2
# String array duplicates


def dup(array):
    result = []  
    for word in array:
        new_word = ""  
        for i in range(len(word)):
            if i == 0 or word[i] != word[i - 1]:
                new_word += word[i]
        result.append(new_word)
    return result


#3
# Stop gninnipS My sdroW!


def spin_words(sentence):
    L = sentence.split()
    new = []
    for word in L:
        if len(word) >= 5:
            new.append(word[::-1])
        else:
            new.append(word)
    string = " ".join(new)
    return string

#4
# Fix string case


def solve(s):
    upper = 0
    lower = 0
    
    for i in s:
        if i.islower():
            lower += 1
        else:
            upper += 1
            
    if upper == lower or lower > upper:
        return s.lower()
    else:
        return s.upper()

#5
# Form The Minimum

def min_value(digits):
    sorted_digits = sorted(set(digits))
    result = ""
    for member in sorted_digits:
        result += str(member)
    return int(result)

#6 
# Maximum Multiple

def max_multiple(divisor, bound):
    
    max_multiple = (bound // divisor) * divisor
    
    return max_multiple

#7
# Alphabetically ordered

def alphabetic(s):
    return sorted(s) == list(s)

#8
# Case-sensitive!

def case_sensitive(s):
    non_lower = [i for i in s if i.isupper()]
    return [len(non_lower) == 0, non_lower]
