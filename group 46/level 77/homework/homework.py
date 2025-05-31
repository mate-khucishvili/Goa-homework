# 1 - Summing a number's digits
def sum_digits(number):
    number_str = str(number)
    
    if number_str[0] == '-':
        number_str = number_str[1:]
    
    return sum(int(i) for i in number_str)
 
# 2 - Search for letters
def sort_gift_code(code):
    return ''.join(sorted(code))
 
# 3 - Sort the Gift Code
def change(st):
    result = ""
    st = st.lower()
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i in st:
            result += "1"
        else:
            result += "0"
    return result
 
# 4 - Stop gninnipS My sdroW!
def spin_words(sentence):
    L = sentence.split()
    new = []
    for word in L:
        if len(word) >= 5:
            new.append(word[::-1])
        else:
            new.append(word)
    string = " ".join(new)
    return string

# დამატებითი 6 kyu

# 1 - Bit Counting
def count_bits(n):
    return bin(n).count('1')

 
# 2 - Replace With Alphabet Position
def alphabet_position(text):
    adgili = []
    for i in text.lower():
        if i.isalpha():                                                         
            adgili.append(str(ord(i) - 96))       # ord —  იღებს ერთ სიმბოლოს და აბრუნებს მისი ASCII ან Unicode კოდის ციფრულ მნიშვნელობას        ord('a')  # აბრუნებს 97
#  გაგრძელება                                                                                                                                        ord('A')  # აბრუნებს 65
    return ' '.join(adgili)

 
# 3 - Count characters in your string
def count(s):
    result = {}
    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result
 
# 4 - Who likes it?
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

# 5 - Unique In Order
def unique_in_order(sequence):
    result = []
    nawili = object()  
    for i in sequence:
        if i != nawili:
            result.append(i)
            nawili = i
    return result