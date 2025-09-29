#1

def lowercase_count(strng):
    count = 0  
    for char in strng:  
        if char.islower():  
            count += 1 
    return count 

#2

def capitals(word):
    indices = []  
    for i in range(len(word)): 
        if word[i].isupper():
            indices.append(i)  
    return indices  

#3

def array(string):
    parts = string.split(',')
    
    if len(parts) <= 2:
        return None
    

    return ' '.join(parts[1:-1])

#4

def contamination(text, char):
    if text == "" or char == "":  
        return ""  
    result = "" 
    for i in text: 
        result += char  
    return result  

#5

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1] 

#6

def obfuscate(email):
    result_email = ""
    for i in email:
        if i == '@':
            result_email += " [at] "
        elif i == '.':
            result_email += " [dot] "
        else:
            result_email += i
    return result_email