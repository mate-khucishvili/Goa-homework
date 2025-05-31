num1, num2 = int(input("Enter your number: ")), int(input("Enter your number: "))

if num1 > num2:
    range1 = range(num2, num1 + 1)
    sum1 = 0

    # print only even numbers
    for i in range1:
        if i%2 == 0:
            print(i)
            sum1 += i
    
    print("Sum of all even numbers are:", str(sum1))
else:
    range2 = range(num1, num2 + 1)
    sum2 = 0

    # print only odd numbers
    for i in range2:
        if i%2 != 0:
            print(i)
            sum2 += i
    
    print("Sum of all even numbers are:", str(sum2))











