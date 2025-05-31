# 1
# Returning Strings

def greet(name):
    return(f"Hello, {name} how are you doing today?")

# 2

# Basic Mathematical Operations

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2

# 3

# Century From Year

def century(year):
    return (year + 99) // 100

# 4

# Keep Hydrated!

def litres(time):
    return int(time * 0.5)

# 5

# Opposites Attract

def lovefunc(flower1, flower2):
    return (flower1 + flower2) % 2 == 1

