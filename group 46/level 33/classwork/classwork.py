# 1
def get_volume_of_cuboid(length, width, height):
    return length * width * height


# 2

def find_average(nums):
    total = sum(nums)
    
    average = total / len(nums)
    
    return average

# 3

def no_boring_zeros(n):
    if n == 0:
        return 0
    while n % 10 == 0:
        n //= 10
    return n

# 4

def final_grade(exam, projects):
    
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0


# 5

def maps(a):
    return [x * 2 for x in a]


print(maps([1, 2, 3]))

# 6

def xo(s):
    s = s.lower()

    return s.count('x') == s.count('o')

# 7

def hero(bullets, dragons):
    
    return bullets >= dragons * 2