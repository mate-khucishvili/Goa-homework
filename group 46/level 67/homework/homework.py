# 1-Jaden Casing Strings
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

# 2-Beginner Series #3 Sum of Numbers
def get_sum(a,b):
    if b > a:
        return sum(range(a, b + 1))
    else:
        return sum(range(b, a + 1))
# 3-Maximum Length Difference
# https://www.codewars.com/kata/5663f5305102699bad000056/train/python

# 4-Simple beads count
def count_red_beads(n):
    return(n-1)*2
# 5-Simple Fun #136: Missing Values
def missing_values(seq): 
    x = 0
    y = 0
    for i in seq:
        if seq.count(i) == 1:
            x = i
        if seq.count(i) == 2:
            y = i
    return x * x * y

# დამატებითი 8kyu 

# 1-Convert a Boolean to a String
def boolean_to_string(b):
    return str(b)

# 2-Opposites Attract

def lovefunc(flower1, flower2):
    return (flower1 + flower2) % 2 == 1

# 3-Beginner Series #2 Clock
def past(h, m, s):
    h_ms = h * 3600000
    
    m_ms = m * 60000
    
    s_ms = s * 1000
    
    return h_ms + m_ms + s_ms

# 4-Sentence Smash
def smash(words):
    return " ".join(words)

# 5-Fake Binary
def fake_bin(x):
    result = ""
    for i in x:
        if int(i) < 5:
            result += "0"
        else:
            result += "1"
    
    return result

# 6-Count by X
def count_by(x, n):
    result = []  
    for i in range(1, n + 1): 
        result.append(x * i)  
    return result 

# 7-Quarter of the year
def quarter_of(month):
    return (month + 2) // 3

# 8-Total amount of points
def points(games):
    result = 0
    for i in games:
        x = int(i[0])
        y = int(i[2])
        
        if x>y:
            result += 3
        elif x==y:
            result += 1
    
    return result

# 9-Parse nice int from char problem
def get_age(age):
    return int(age[0])

# 10-Grasshopper - Debug sayHello
def say_hello(name):
    return f"Hello, {name}"