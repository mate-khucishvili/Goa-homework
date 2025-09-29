# 1

# Swap Values

def swap_values(args): 
    temp = args[0]
    
    args[0] = args[1]
    
    args[1] = temp


# 2

# Sum of Multiples

def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"
    return sum(range(n, m, n))


# 3

# How old will I be in 2099?

def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth

    if age > 0:
        if age == 1:
            return f"You are {age} year old."
        else:
            return f"You are {age} years old."
    elif age < 0:
        if age == -1:
            return f"You will be born in {-age} year."
        else:
            return f"You will be born in {-age} years."
    else:
        return "You were born this very year!"

# 4

# Multiple of index 

def multiple_of_index(arr):
    li = []
    if arr[0] == 0:
            li.append(0)
    for i in range(1,len(arr)):
        if arr[i] % i == 0:
            li.append(arr[i])

    return li

# 5

# Dollars and Cents

def format_money(amount):
    return '$%.2f' % float(amount)