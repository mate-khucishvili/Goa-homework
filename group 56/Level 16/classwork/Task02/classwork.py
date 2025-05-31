number = 5
user_number = int(input("Enter number: "))
counter = 0

while user_number != number:
    user_number = input("Enter number: ")
    counter += 1

print("Access")
print("Access:", str(counter))