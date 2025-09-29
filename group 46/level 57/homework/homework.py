# Task-1 - Thinkful - Logic Drills: Traffic light
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    else:
        return "This is not a traffic light color."
# Task-2 - Count by X

def count_by(x, n):
    arr = []
    for num in range(1, n+1):
        result = x * num
        arr.append(result)
    return arr
# Task-3 - Abbreviate a Two Word Name
def abbrev_name(name):
    pirveli, bolo = name.upper().split()
    return f"{pirveli[0]}.{bolo[0]}"

# Task-4 - Count of positives / sum of negatives
def count_positives_sum_negatives(arr):
    if not arr: return []
    dadebiti = 0
    uaryofiti = 0
    for x in arr:
        if x > 0:
            dadebiti += 1
        if x < 0:
            uaryofiti += x
    return [dadebiti, uaryofiti]

# Task-5 - Jenny's secret message

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!" 
    
# დამატებით - გამარჯობა მე ვარ ზურიკო პეტრე პავლე

# Task-1 - Third Angle of a Triangle
def other_angle(a,b):
    return 180 - a - b

# Task-2 - Reversed Words
def reverseWords(str):
    new_cvladi = []
    for i in str.split():
        new_cvladi.append(i)
    new_cvladi.reverse()   
    return ' '.join(new_cvladi)

# Task-3 - Twice as old
def twice_as_old(d, s):
    return abs(d-2*s) # აბრუნებს რიცხვის დადებით ვერსია

# Task-4 - Removing Elements
def remove_every_other(my_list):
    return my_list[::2]

# Task-5 - Do I get a bonus?
def bonus_time(salary, bonus):
    if bonus :
        return "$" + str(salary * 10)
    else:
        return "$" + str(salary)
 