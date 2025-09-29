# 1 Get Nth Even Number

def nth_even(n):
    return 2 * (n - 1);


# 2 Add Length

def add_length(str_):
    result = []
    for word in str_.split():
        result.append(word + ' ' + str(len(word)))
    return result



# 3 To square(root) or not to square(root)

def square_or_square_root(arr):
    result = []
    for x in arr:
        root = x**0.5
        if root.is_integer():
            result.append(root)
        else:
            result.append(x*x)
    return result
# 4 Remove First and Last Character Part Two

def array(s):
    items = s.split(',')
    
    if len(items) <= 2:
        return None
    
    return ' '.join(items[1:-1])

# 5 Difference of Volumes of Cuboids

def find_difference(a, b):
    v1 = a[0] * a[1] * a[2]
    v2 = b[0] * b[1] * b[2]
    if v1 > v2:
        return v1 - v2
    elif v1 < v2:
        return v2 - v1
    else:
        return 0