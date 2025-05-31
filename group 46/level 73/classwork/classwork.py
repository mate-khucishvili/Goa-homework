# 1 - Printer Errors
def printer_error(s):
    kargi_nawili = "abcdefghijklm"
    
    erorebis_raodenoba = 0
    for i in s:
        if i not in kargi_nawili:
            erorebis_raodenoba += 1

    sabolo_sigrzde = len(s)

    return f"{erorebis_raodenoba}/{sabolo_sigrzde}"
 
# 2 - Number of People in the Bus

def number(bus_stops):
    sum=0
    for i in bus_stops:
        sum+=i[0]-i[1]
    return sum
 
# 3 - Don't give me five!
def dont_give_me_five(start, end):
    count = 0  
    for i in range(start, end + 1): 
        if '5' not in str(i):
            count += 1
    return count

 
# 4 - Array.diff
def array_diff(a, b):
    result = [] 
    
    for i in a: 
        if i not in b:  
            result.append(i) 
    
    return result  

 
# 5 - Take a Ten Minutes Walk
def is_valid_walk(walk):
    if len(walk) != 10:
        return False

    x = 0  
    y = 0  

    for i in walk:
        if i == 'n':
            y += 1
        elif i == 's':
            y -= 1
        elif i == 'e':
            x += 1
        elif i == 'w':
            x -= 1

    return x == 0 and y == 0


 
# 6 - Sum of Digits / Digital Root
def digital_root(n):
    while n >= 10:
        n = sum(int(i) for i in str(n))
    return n

 
# 7 - Unique In Order
def unique_in_order(sequence):
    result = []
    nawili = object()  
    for i in sequence:
        if i != nawili:
            result.append(i)
            nawili = i
    return result
 