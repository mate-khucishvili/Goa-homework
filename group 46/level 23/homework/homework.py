#task- 1
name = input("Enter your name: ")

print(name.lower())

#task- 2

surname = input("Enter your surname: ")

print(surname.upper())

#task- 3

word_1 = "everest"

print(word_1.capitalize())

#task- 4

word_2 = "Titan"

print(word_2.find("a"))

#task- 5

old_list = ["გამარჯობა", "როგორ ხარ", "ლამაზი დღეა", "პითონი საუკეთესოა"]


new_list= []


for i in old_list:
    new_list.append(old_list.upper())


print(new_list)