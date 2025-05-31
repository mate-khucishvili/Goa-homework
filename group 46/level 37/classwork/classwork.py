#1

# Regex count lowercase letters


def remove(s):
    if s.endswith("!"):  # ვამოწმებთ, მთავრდება თუ არა სტრინგი "!" სიმბოლოთი
        return s[:-1]  # თუ მთავრდება, ვშლით ბოლო სიმბოლოს (ბოლო ასოს გარეშე ვაბრუნებთ)
    return s  # თუ არა, ვაბრუნებთ პირვანდელ სტრინგს

#2

# Find the capitals

def capitals(word):
    indices = []  
    
    for i in range(len(word)):
        if word[i].isupper(): 
            indices.append(i)  
            
    return indices




