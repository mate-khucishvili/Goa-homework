# 1
def capitals(word):
    result = []
    for i in range(len(word)):
        if word[i].isupper():  # თუ ასო დიდია
            result.append(i) # ვამატებთ ინდექსს სიაში

    return result

# 2

def max_multiple(divisor, bound):
    
    # ვიპოვოთ ყველაზე დიდი მთელი რიცხვი რომელიც დაბმულობს divisor-ით და არ აღემატება bound-ს
    # ვყოფთ bound-ს divisor-ზე და ვიღებთ მთელი ნაწილის შედეგს
    max_multiple = (bound // divisor) * divisor
    
    # ვბრუნებთ შედეგს რაც არის divisor-ით გაყოფილი ყველაზე დიდი რიცხვი რომელიც არ აღემატება bound-ს
    return max_multiple


# 3

def sum_digits(number):
    # თუ რიცხვი ნეგატიურია, გადავიყვანოთ დადებითში
    if number < 0:
        number = -number
    
    # ციფრების ჯამი
    return sum(int(digit) for digit in str(number))


# 4

def dont_give_me_five(start, end):
    count = 0
    for num in range(start, end + 1):
        if num // 10 == 5 or num % 10 == 5:
            continue
        count += 1
    return count


# 5
def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result

# 6

def invert(lst):
    return [-x for x in lst]

# 7

def sum_array(arr):
    if len(arr) <= 2:
        return 0
    
    arr.sort()

    return sum(arr[1:-1])
