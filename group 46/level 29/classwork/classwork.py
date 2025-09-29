def sum_sum(numbers):
    
    sum_loop = 0
    for num in numbers:
        sum_loop += num
    
    
    sum_function = sum(numbers)
    
    
    return sum_loop, sum_function


numbers = [1, 2, 3, 4, 5]
result = sum_sum(numbers)
print("ჯამი for ციკლით:", result[0])
print("ჯამი sum() ფუნქციით:", result[1])
