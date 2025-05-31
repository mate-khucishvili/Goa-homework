# 1 - while loop
i = 0
while i < 20:
    print("Skola magaria")
    i += 1

# 2 -
user_pasuxi = input("შეიყვანე ელემენტები გამოყავი მძიმით (,): ")
items = user_pasuxi.split(",")

for item in items:
    print(item.strip())

# 3 - მსგავსებები და განსხვავებები: set dictionary tuple

# მსგავსებები:
# ყველა ინახავს მონაცემებს

# განსხვავებები:
# set – უნიკალური ელემენტები {}

# dict – key-value წყვილები {key: value}

# tuple – უცვლელია ()

# 4 - რას ნიშნავს immutable და mutable

# Immutable – მნიშვნელს ვერ შეცვლი მაგალითად: tuple int str — ანუ თუ შექმნი ვერ შეცვლი

# Mutable – შეგვიძლია შეცვლა მაგალითად: list set dictionary

# 5 - კონკატენაცია

a = "Hello"
b = "World"
print(a + " " + b)  # Hello World

# 6 - დეკლარირება

x = 555554

# 7 - and და or ოპერატორების მაგალითები

# and 
print(True and True)     # True
print(True and False)    # False
print(5 > 2 and 3 < 10)  # True
print(1 == 1 and 2 != 2) # False

# or
print(True or False)     # True
print(False or False)    # False
print(5 > 10 or 3 < 10)  # True
print(1 != 1 or 2 == 2)  # True
