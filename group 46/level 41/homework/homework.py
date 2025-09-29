# 1 

# Convert number to reversed array of digits


def digitize(n):
    num_string = str(n)
    
    digits = [int(digit) for digit in num_string]
    
    rev_digits = digits[::-1]
    
    return rev_digits


# 2

# Beginner Series #1 School Paperwork

def paperwork(n, m):

    if n < 0 or m < 0:
        return 0
    
    return n * m


# 3


# Beginner Series #2 Clock

# ეს გამიჭირდა და ასე ახსნა იყოს რომ შეხედვისას გამახსენდეს

def past(h, m, s):       # ანუ მაგალითად შუალედი თუ იქნება : 0 საათი, 1 წუთი, 1 წამი

    hou_ms = h * 3600000 # 1 საათი = 1 × 3600000 = 3600000 მილიწამი ( ეს ისე ვერ ვიმახსოვრებ და ასე იყოს D )
    
    min_ms = m * 60000 # 0 წუთი = 0 × 60000 = 0 მილიწამი
    
    sec_ms = s * 1000 # 0 წამი = 0 × 1000 = 0 მილიწამი
    
    return hou_ms + min_ms + sec_ms # ჯამი: 3600000 + 0 + 0 = 3600000 მილიწამი.

# 4

# Simple multiplication


def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9


# 5

# Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    max_distance = mpg * fuel_left
    
    return max_distance >= distance_to_pump


# 6 

#Calculate BMI


def bmi(weight, height):
    bmi_value = weight / (height ** 2)
    
    if bmi_value <= 18.5:
        return "Underweight"
    elif bmi_value <= 25.0:
        return "Normal"
    elif bmi_value <= 30.0:
        return "Overweight"
    else:
        return "Obese"


# 7

# Fake Binary


def fake_bin(x):
    
    result = ""
    
    for i in x:
        
        if int(i) < 5:
            result += "0"
        else:
            result += "1"
    
    return result


# 8

# Count by X

def count_by(x, n):
    result = []  
    for i in range(1, n + 1): 
        result.append(x * i)  
    return result 

# 9

# Abbreviate a Two Word Name


def abbrev_name(name):
    first_name, last_name = name.split()
    
    return first_name[0].upper() + '.' + last_name[0].upper()


# 10

# Area or Perimeter


def area_or_perimeter(l, w):
    if l == w:
        return l * l  
    else:
        return 2 * (l + w)  

