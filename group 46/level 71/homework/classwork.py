# 1 - Who likes it?
def likes(names):
    n = len(names)

    if n == 0:
        return "no one likes this"
    if n == 1:
        return f"{names[0]} likes this"
    if n == 2:
        return f"{names[0]} and {names[1]} like this"
    if n == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    if n >= 4:
        return f"{names[0]}, {names[1]} and {n - 2} others like this"

# 2 - Create Phone Number
def create_phone_number(n):
    # პირველი 3 ციფრი 
    code_all = ""
    for i in range(3):
        code_all += str(n[i])
    
    # შემდეგი 3 ციფრი 
    part_one = ""
    for i in range(3, 6):
        part_one += str(n[i])
    
    # ბოლო 4 ციფრი
    part_two = ""
    for i in range(6, 10):
        part_two += str(n[i])
    
    number = "(" + code_all + ") " + part_one + "-" + part_two
    
    return number
# 3 - Find the odd int
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 !=0:
            return i
        
# 4 - Row Weights
def row_weights(array):
    team1 = 0
    team2 = 0

    for i in range(len(array)):
        if i % 2 == 0:
            team1 += array[i]
        else:
            team2 += array[i]

    return (team1, team2)

# 5 - Largest pair sum in array
def largest_pair_sum(numbers): 
    return sum(sorted(numbers)[-2:])
