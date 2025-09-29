# 1 - Isograms
def is_isogram(string):
    string = string.lower()
    return len(string) == len(set(string))
 
# 2 - Jaden Casing Strings
def to_jaden_case(string):
    # გაყოფა სიტყვებად
    words = string.split()
    
    capitalized_words = [word.capitalize() for word in words]
    
    # დაბრუნდება გაერთიანებული სია
    return ' '.join(capitalized_words)

# 3 - Mumbling
def accum(st):
    # ცარიელი სია თითოეული გარდაქმნილი ნაწილისთვის
    parts = []
    
    for i, char in enumerate(st):
        # დიდი ასო + იგივე პატარა ასოები i-ჯერ
        part = char.upper() + char.lower() * i
        
        # დამუშავებული ნაწილის დამატება სიაში
        parts.append(part)
    
    # ყველა ნაწილის შეერთება ტირეებით
    return '-'.join(parts)
 
# 4 - Regex validate PIN code
def validate_pin(pin):
    
    if len(pin) == 4 or len(pin) == 6:
        
        if pin.isdigit():
            return True  
        else:
            return False  
    else:
        return False 
 
# 5 - Sum of odd numbers
def row_sum_odd_numbers(n):
    return n ** 3
 

# დამატებით გააკეთეთ 5 ცალი 7kyu codewars

# 1 - Vowel Count
def get_count(sentence):
    result = 0 
    for i in sentence:
        if i in 'aeiou':
            result = result + 1
    return result
         
# 2 - Disemvowel Trolls
def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s


# 3 - Square Every Digit
def square_digits(num):
    num_str = str(num)
    
    result = " "
    
    for i in num_str:
        result += str(int(i) ** 2)
        
    return int(result)


# 4 - List Filtering
def filter_list(l):
    result = []
    
    for i in l:
        if isinstance(i, int):
            result.append(i)
    return result


# 5 - Say hello!
def greet(name):
    if name:
        return f"hello {name}!"

