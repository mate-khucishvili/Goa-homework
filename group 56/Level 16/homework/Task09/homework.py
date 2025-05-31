user_nick = "Dark555"
user_password = 12345

user_input_nick= str((input("Enter nick name: ")))
user_input_password= int((input("Enter password: ")))

while user_nick != user_input_nick or user_password != user_input_password:
    print("Incorrect username or password")
    user_input_nick = input("Enter your username: ")
    user_input_password = input("Enter your password: ")
print("Access")
