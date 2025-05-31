num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))
num3 = int(input("შეიყვანეთ მესამე რიცხვი: "))

for i in range(num1, num2, num3):
    print(i ** 2)
