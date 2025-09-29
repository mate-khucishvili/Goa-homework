#task- 1

# .lower() / .upper() / .capitalize() / .find()

# .lower()- აპატარავებს ყველა ასოს
# .upper()- ადიდებს ყველა ასოს
# .capitalize()- პირველ ასოს ადიდებს
# .find()- ეძებს კონკრეტულ სიმბოლოს სტრინგში

#task- 2

surname = str(input("Enter your surname: "))

if surname[0] == surname[0].upper:
    print("Hello")
else:
    print("Bye")


#task- 3

name = (input("Enter name: "))

num = (input("Enter number: "))

if name.find(num):
    print("Can't find character")
else:
    print("found it:", name.find(num))

#task- 4

surname = input("Enter your surname: ")
change = input("change your surname: ")

if change == "upper":
    print(surname.upper())
elif change == "lower":
    print(surname.lower())
elif change == "capitalize":
    print(surname.capitalize())
else:
    print("invalid input")