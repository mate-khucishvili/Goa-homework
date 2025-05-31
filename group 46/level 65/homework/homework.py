# 1-List Filtering
def filter_list(l):
    result = []
    
    for i in l:
        if isinstance(i, int):
            result.append(i)
    return result
# 2-Jaden Casing Strings
def to_jaden_case(string):
    # გაყოფა სიტყვებად
    words = string.split()
    

    capitalized_words = [word.capitalize() for word in words]
    
    # დაბრუნდება გაერთიანებული სია
    return ' '.join(capitalized_words)
# 3-Sum of two lowest positive integers
def sum_two_smallest_numbers(num_list):
    num_list.sort()
    return num_list[0] + num_list[1]
# 4-Is this a triangle?
def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)
# 5-Two to One
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

# შეასრულეთ თქვენთვის სასურველი 5 ცალი 7kyu
# 1- Beginner Series #3 Sum of Numbers
def get_sum(a,b):
    if b > a:
        return sum(range(a, b + 1))
    else:
        return sum(range(b, a + 1))

# 2- Find the next perfect square!
def find_next_square(sq):
    result = sq ** 0.5
    if result.is_integer():
        return (result + 1)**2
    return -1

# 3- Disemvowel Trolls
def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s

# 4- Isograms
def is_isogram(string):
    string = string.lower()
    return len(string) == len(set(string))
    
# 5- String ends with?
def solution(text, ending):
    return text.endswith(ending)