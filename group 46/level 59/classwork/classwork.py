# 1 - Count of positives / sum of negatives
def count_positives_sum_negatives(arr):
    if not arr: return []
    dadebiti = 0
    uaryofiti = 0
    for x in arr:
        if x > 0:
            dadebiti += 1
        if x < 0:
            uaryofiti += x
    return [dadebiti, uaryofiti]

# 2 - Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo" 
    else:
        return name + " does not play banjo"
        
# 3 - Simple multiplication
def simple_multiplication(number):
    return number * 8 if number % 2 == 0 else number * 9

# 4 - Invert values
def invert(lst):
    return [-x for x in lst]

# 5 - Beginner - Reduce but Grow
def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result

# 6 - Disemvowel Trolls
def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s

# 7 - Sum of two lowest positive integers
def sum_two_smallest_numbers(num_list):
    num_list.sort()
    return num_list[0] + num_list[1]
