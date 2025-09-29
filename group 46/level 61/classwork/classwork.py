# 1 - Get the mean of an array
def get_average(marks):
    return int(sum(marks) / len(marks))

# 2 - Total amount of points
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

# 3 - Sum of two lowest positive integers
def sum_two_smallest_numbers(num_list):
    num_list.sort()
    return num_list[0] + num_list[1]

# 4 - Number of People in the Bus
def number(bus_stops):
    sum=0
    for i in bus_stops:
        sum+=i[0]-i[1]
    return sum

# 5 - Build a square
def generate_shape(n):
    return '\n'.join(['+' * n] * n)

# 6 - Multiples of 3 or 5
def solution(number):
    if number <= 0:
        return 0 
    
    total = 0
    for i in range(number): 
        if i % 3 == 0 or i % 5 == 0:  
            total += i  
    return total  


# 7 - Get the mean of an array
def get_average(marks):
    return int(sum(marks) / len(marks))