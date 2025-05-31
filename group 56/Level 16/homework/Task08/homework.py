correct_password = "12345"

user_input = input("Enter the password: ")

while user_input != correct_password:
    print("Incorrect password")
    user_input = input("Enter the password: ")

print("Password correct!")
