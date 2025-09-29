#1 -Beginner Series #2 Clock
def past(h, m, s):
    hou_ms = h * 3600000
    
    min_ms = m * 60000
    
    sec_ms = s * 1000
    
    return hou_ms + min_ms + sec_ms

#2 -A Needle in the Haystack
def find_needle(haystack):
    result = haystack.index("needle")
    return f"found the needle at position {result}" 

#3 - Beginner Reduce but Grow
def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result

#4 -Transportation on vacation
def rental_car_cost(d):
    fasi = d * 40
    if d >= 7:
        fasi -= 50
    elif d >= 3:
        fasi -= 20
    return fasi

#5 -Is this a triangle?
def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)

#6 -Find the stray number
def stray(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i
