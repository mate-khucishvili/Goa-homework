#1 Count characters in your string
def count(s):
    result = {}
    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


#2 The Vowel Code
def encode(st):
    L=[]
    A = {"a":"1","e":"2","i":"3","o":"4","u":"5"}
    for i in st:
        if i in A:
            L.append(A[i])
        else:
            L.append(i)
    return "".join(L)
    
def decode(st):
    L=[]
    A = {"1":"a","2":"e","3":"i","4":"o","5":"u"}
    for i in st:
        if i in A:
            L.append(A[i])
        else:
            L.append(i)
    return "".join(L)
#3 Handshake problem
def get_participants(handshakes):
    M = 1 
    raodenoba = 2 
    if handshakes == 0:
        return 0
    while raodenoba:
        if handshakes > M:
            M += raodenoba
            raodenoba += 1
        else:
            return raodenoba
#4 Sort Arrays (Ignoring Case)
def sortme(a):
    return sorted(a, key=str.lower)

# შემდეგი ნაწილი დავალების დამატებითი 

#1 Complementary DNA
def DNA_strand(dna):
    result = ""
    for i in dna:
        if i == "A":
            result += "T"
        elif i == "T":
            result += "A"
        elif i == "C":
            result += "G"
        elif i == "G":
            result += "C"
    return result

#2 Simple Fun #176: Reverse Letter
def reverse_letter(st):
    result = []

    for i in st:
        if i.isalpha():
            result.append(i)

    result.reverse()

    return ''.join(result)

#3 Make a function that does arithmetic!
def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a / b
    else:
        raise ValueError("Invalid operator")

#4 Find the next perfect square!
def find_next_square(sq):
    result = sq ** 0.5
    if result.is_integer():
        return (result + 1)**2
    return -1
#5 Fix string case
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
