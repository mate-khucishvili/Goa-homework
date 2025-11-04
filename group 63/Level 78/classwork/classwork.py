# 1 - Reversed Strings
def solution(string):
    return string[::-1]
# 2 - Grasshopper - Function syntax debugging
def main(verb, noun): 
    return verb + noun

# 3 - Area or Perimeter
def area_or_perimeter(l, w):
    if l == w:
        return l * l  
    else:
        return 2 * (l + w)  

# 4 - Return Negative
def make_negative(number):
    if number > 0:
        return -number
    return number

# 5 - Opposite number
def opposite(number):
    return -number

# 6 - Mumbling
def accum(st):
    parts = []
    
    for i, o in enumerate(st):               #enumerate - ახალი მეთოდი ასოს აძლევს თავის ინდექს მაგ (აბსდაგ) - იქნება ა-0 ბ-1 ს-2 დ-3 ა-4 გ-5
        part = o.upper() + o.lower() * i
        parts.append(part)
        
    return '-'.join(parts)

# 7 - Anagram Detection
def is_anagram(test, original):
    return sorted(original.lower()) == sorted(test.lower())