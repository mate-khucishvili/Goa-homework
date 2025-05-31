# task- 1

numbers = []

for i in range(201): 
    if i % 2 == 0:
        numbers.append(i)

print(numbers)

#task- 2

favorite_names = []

for i in range(5):
    name = input(f"შეიყვანეთ თქვენი #{i+1} საყვარელი სახელი: ")
    favorite_names.append(name)

print("თქვენი საყვარელი სახელები:", favorite_names)

#task- 3

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


odd_elements = [my_list[i] for i in range(len(my_list)) if i % 2 != 0]

print(odd_elements)

#task- 4 

my_string = "გამარჯობა, როგორ ხარ?"
char_count = len(my_string)

print("სტრინგის სიმბოლოების რაოდენობა:", char_count)

#task- 5

my_list = [10, 20, 30, 40, 50]

index = int(input("შეიყვანეთ ინდექსი რომლის ამოღებაც გსურთ (0-დან 4-მდე): "))
if 0 <= index < len(my_list):
    trush_element = my_list.pop(index)
    print(f"ამოღებული ელემენტი: {trush_element}")
    print("განახლებული სია:", my_list)
else:
    print("არასწორი ინდექსი!")

#task- 6

my_list = [5, 10, 15, 20, 25]
list_length = len(my_list)

print("სიის სიგრძე არის:", list_length)

