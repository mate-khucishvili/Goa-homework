#1 

def mult_numbers(a, b):
    return a * b

# გამოყენება:
result = mult_numbers(5, 3)
print(result)

# 2

# isalnum
text1 = "Python3"
print(text1.isalnum())
text2 = "Python 3!"
print(text2.isalnum())

# isdigit

number = "12345"
print(number.isdigit())
text = "123a"
print(text.isdigit())

# islower

text = "hello"
print(text.islower()) 
text2 = "Hello"
print(text2.islower())  

# isnumeric

text = "12345"
print(text.isnumeric())  
text2 = "⅕"  
print(text2.isnumeric())

# isupper

text = "HELLO"
print(text.isupper())
text2 = "Hello"
print(text2.isupper())

# count

text = "banana"
print(text.count("a"))  # 3

# 3

# min

numbers = [3, 1, 4, 1, 5]
print(min(numbers))

# max

numbers = [3, 1, 4, 1, 5]
print(max(numbers))
