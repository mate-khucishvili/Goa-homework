# 1 

# Generate range of integers


def generate_range(start, stop, step):
    result = []
    current = start
    while current <= stop:
        result.append(current)
        current += step
    return result


# 2

# reverseIt

def reverse_it(data):
    if type(data) in [int, str, float]:
        return type(data)(str(data)[::-1])
    return data

# 3

# Sum without highest and lowest number


def sum_array(arr):
    if not arr or len(arr) <= 1:
        return 0
    return sum(arr) - min(arr) - max(arr)


# 4

# Count by X


def count_by(x, n):
    result = []  
    for i in range(1, n + 1): 
        result.append(x * i)  
    return result 