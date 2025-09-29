# შეასრულეთ codewars-ის შემდეგი ამოცანები ;>
# 1) https://www.codewars.com/kata/57a1fd2ce298a731b20006a4
# 2) https://www.codewars.com/kata/55edaba99da3a9c84000003b
# 3) https://www.codewars.com/kata/55ecd718f46fba02e5000029
# 4) https://www.codewars.com/kata/57e76bc428d6fbc2d500036d
# 5) https://www.codewars.com/kata/5b077ebdaf15be5c7f000077

# 1 - Is it a palindrome?
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1] 

# 2 - Find numbers which are divisible by given number
def divisible_by(numbers, divisor):
    div = []
    for num in numbers:
        if num % divisor == 0:
            div.append(num)
    return div

# 3 - What is between?
def between(a, b):
    return list(range(a, b + 1))

# 4 - Convert a string to an array
def string_to_array(s):
    return s.split(" ")


# 5 - If you can't sleep, just count sheep!!
def count_sheep(n):
    result = ""
    for i in range(1, n + 1):
        result += str(i) + " sheep..."
    return result
