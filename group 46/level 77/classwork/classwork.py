#1 Make a function that does arithmetic!
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

#2 Anagram Detection
def is_anagram(test, original):
    return sorted(original.lower()) == sorted(test.lower())
#3 Count by X
def count_by(x, n):
    result = []  
    for i in range(1, n + 1): 
        result.append(x * i)  
    return result 
#4 Third Angle of a Triangle
def other_angle(a,b):
    return 180 - a - b
#5 Sum even numbers
def sum_even_numbers(seq):
    sum = 0
    for i in seq:
        if isinstance(i, int) and i % 2 == 0:
            sum += i
    return sum
#6 Cat years, Dog years
def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        kata = 15
        zdaxli = 15
    elif human_years == 2:
        kata = 15 + 9
        zdaxli = 15 + 9
    else:
        extra_years = human_years - 2
        kata = 15 + 9 + extra_years * 4
        zdaxli = 15 + 9 + extra_years * 5
    return [human_years, kata, zdaxli]
#7 Sum The Strings
def sum_str(a, b):
    a = a if a else '0'
    b = b if b else '0'
    return str(int(a) + int(b))
#8 Remove the minimum
def remove_smallest(numbers):
    if not numbers:
        return []

    smallest = min(numbers)

    index = numbers.index(smallest)
    
    return numbers[:index] + numbers[index+1:]