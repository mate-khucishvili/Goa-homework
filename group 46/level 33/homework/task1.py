# 1

def double_integer(i):
    return i * 2

# 2

def friend(x):
    return [name for name in x if len(name) == 4]

# 3

def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result

# 4

def find_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

# 5

def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague

# 6

def double_char(s):
    return ''.join([char * 2 for char in s])

# 7

def remove_url_anchor(url):
    return url.split('#')[0]

# 8

def sum_cubes(n):
    return sum(i**3 for i in range(1, n+1))

