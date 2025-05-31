#or ის შემთხვევაში True იქნება იმ შემთხვევაში როცა ერთი პირობა მაინც თუა შესრულებული
#and ის შემთხვევაში უნდა იყოს ყველა პირობა შესრულებული თორემ ვერ მივიღებთ True-ს და მაგის მაგივრად მივიღებთ False


print(True or False)
print(True or True)
print(False or False)

print(True and False)
print(True and True)
print(False and False)

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

my_name = "mate"

print(user_age >= 18 and user_name == my_name )