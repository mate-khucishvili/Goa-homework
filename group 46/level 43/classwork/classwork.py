#1

# Get Nth Even Number


def nth_even(n):
    return (n - 1) * 2

# 2

# Add Length

def add_length(str_):
    words = str_.split()

    result = []
    for i in words:
        word_len = len(i)  
        result.append(i + ' ' + str(word_len))

    return result



# 3

# To square(root) or not to square(root)


def square_or_square_root(arr):
    result = []  

    for num in arr:  
        root = num ** 0.5  
        
        if root == int(root): 
            result.append(int(root)) 
        else:
            result.append(num ** 2)  

    return result 



# 4

# Remove First and Last Character Part Two

def array(string):
    par = string.split(',')

    if len(par) <= 2:
        return ""

    return ' '.join(par[1:-1])


# 5

# Difference of Volumes of Cuboids


def find_difference(a, b):
    v1 = a[0] * a[1] * a[2]
    v2 = b[0] * b[1] * b[2]
    if v1 > v2:
        return v1 - v2
    elif v1 < v2:
        return v2 - v1
    else:
        return 0