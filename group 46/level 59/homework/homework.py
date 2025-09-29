# 1 - The highest profit wins!
def min_max(lst):
  return [min(lst), max(lst)]

# 2 - Leap Years
def is_leap_year(year):
    if year % 400 == 0:
        return True
    
    if year % 100 == 0:
        return False
    
    if year % 4 == 0:
        return True
    
    return False


# 3 - Fizz Buzz
def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result

# 4 - Simple Fun #136: Missing Values
def missing_values(seq): 
    x = 0
    y = 0
    for i in seq:
        if seq.count(i) == 1:
            x = i
        if seq.count(i) == 2:
            y = i
    return x * x * y

# 5 - Simple Fun #136: Missing Values
def missing_values(seq): 
    x = 0
    y = 0
    for i in seq:
        if seq.count(i) == 1:
            x = i
        if seq.count(i) == 2:
            y = i
    return x * x * y