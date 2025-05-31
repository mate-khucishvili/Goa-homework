
num1 = float(input("Enter number: "))
num2 = float(input("Enter number: "))
operator = input("Choose one operator: +, -, *, /, **, %  ")

if operator == "+":
    print(num1, "+", num2, "=", num1+num2)
elif operator == "-":
    print(num1, "-", num2, "=", num1-num2)
elif operator == "*":
    print(num1, "*", num2, "=", num1*num2)
elif operator == "/":
    if num2 == 0:
        print("გაყოფა 0-ზე არ შეიძლება")
    else:
        print(num1, "/", num2, "=", num1/num2)
elif operator == "**":
    print(num1, "**", num2, "=", num1**num2)
elif operator == "%":
    print(num1, "%", num2, "=", num1%num2)
else:
    print("Wrong operator")