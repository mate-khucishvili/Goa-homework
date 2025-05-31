# 1- Printer Errors
def printer_error(s):
    kargi_nawili = "abcdefghijklm"
    
    erorebis_raodenoba = 0
    for i in s:
        if i not in kargi_nawili:
            erorebis_raodenoba += 1

    sabolo_sigrzde = len(s)

    return f"{erorebis_raodenoba}/{sabolo_sigrzde}"
# 2- Don't give me five!
def dont_give_me_five(start, end):
    count = 0  
    for i in range(start, end + 1): 
        if '5' not in str(i):
            count += 1
    return count
# 3- Triangular Treasure
def triangular(n):
    if n <= 0:
        return 0
    return n * (n + 1) // 2

# 4- Sorted? yes? no? how?
def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return "yes, ascending"
    elif arr == sorted(arr)[::-1]: 
        return "yes, descending"
    else:
        return "no"
# 5-Bumps in the Road
def bumps(road):
    if road.count('n') <= 15:
        return "Woohoo!"
    else:
        return "Car Dead"
    
# დამატებით

# 1-Sum of two lowest positive integers
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

# 2-Friend or Foe?
def friend(x):
    friends = []
    
    for name in x:
        
        if len(name) == 4:
            
            friends.append(name)
    
    return friends


# 3- Two to One
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))


# 4- Printer Errors
def printer_error(s):
    kargi_nawili = "abcdefghijklm"
    
    erorebis_raodenoba = 0
    for i in s:
        if i not in kargi_nawili:
            erorebis_raodenoba += 1

    sabolo_sigrzde = len(s)

    return f"{erorebis_raodenoba}/{sabolo_sigrzde}"   # ეს დავალება გამიჭირდა დამეხმარეს მაგრამ მაინც ვერ მივხვდი 


# 5-Reverse words
def reverse_words(str):
    string = []
    for i in str.split(' '):
        string.append(i[::-1])
    return ' '.join(string)