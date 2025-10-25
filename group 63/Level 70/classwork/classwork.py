# 1- reverseIt
def reverse_it(data):
    if type(data) in [int, str, float]:
        return type(data)(str(data)[::-1])
    return data

# 2- Friend or Foe?
def friend(x):
    res = []
    for i in x:
        if len(i) == 4:
            res.append(i)
    return res

# 3- Sum of Cubes
def sum_cubes(n):
    return sum(i**3 for i in range(1, n+1))

# 4- Say hello!
def greet(name):
    if name:
        return f"hello {name}!"

# 5- Find the odd int
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 !=0:
            return i
