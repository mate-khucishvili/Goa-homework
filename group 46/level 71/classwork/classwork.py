# 1 - Array.diff
def array_diff(a, b):
    result = [] 
    
    for i in a: 
        if i not in b:  
            result.append(i) 
    
    return result

# 2 - Duplicate Encoder
def duplicate_encode(word):
    word = word.lower()
    result = ""

    for i in word:
        if word.count(i) == 1:
            result += "("
        else:
            result += ")"

    return result

# 3 - Break camelCase
def solution(s):
    result = ""
    for i in s:
        if i.isupper():
            result += " " + i
        else:
            result += i
    return result

# 4 - Are the numbers in order?
def in_asc_order(arr):
    return arr == sorted(arr)

# 5 - Remove duplicate words
def remove_duplicate_words(s):
    words = s.split() 
    result = []  


    for i in words:
        if i not in result:  
            result.append(i)  

    return ' '.join(result) 
