#1 Create Phone Number
def create_phone_number(n):
    # პირველი 3 ციფრი 
    code_all = ""
    for i in range(3):
        code_all += str(n[i])
    
    # შემდეგი 3 ციფრი 
    part_one = ""
    for i in range(3, 6):
        part_one += str(n[i])
    
    # ბოლო 4 ციფრი
    part_two = ""
    for i in range(6, 10):
        part_two += str(n[i])
    
    number = "(" + code_all + ") " + part_one + "-" + part_two
    
    return number
#2 Find the odd int
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 !=0:
            return i
#3 Array.diff
def array_diff(a, b):
    result = [] 
    
    for i in a: 
        if i not in b:  
            result.append(i) 
    
    return result
#4 Is it a palindrome?
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1] 
#5 Was the package received before it was sent? (Simplified)
def was_package_received_yesterday(tz_from, tz_to, start, duration):
    return start < tz_from - tz_to - duration
