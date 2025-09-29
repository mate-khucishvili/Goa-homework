# 1 - Largest pair sum in array
def largest_pair_sum(numbers): 
    return sum(sorted(numbers)[-2:])

# 2 - Reverse words
def reverse_words(str):
    strings = []
    for i in str.split(' '):
        strings.append(i[::-1])
    return ' '.join(strings)

# 3 - Categorize New Member
def openOrSenior(data):
    result = []
    for i in data:
        
        if i[0] >= 55 and i[1] > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result