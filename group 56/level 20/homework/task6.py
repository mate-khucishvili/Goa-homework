num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))


sum = 0


for number in range(num1, num2 + 1):
    number += sum


print(number)
