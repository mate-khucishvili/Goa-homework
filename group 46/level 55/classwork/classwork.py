# 1. დიქშენერი მანქანის აღწერით
my_car = {
    "brand": "Mercedes-Benz",
    "model": "G-Class",
    "year": 2023
}

# გასაღებებისა და მნიშვნელობების წყვილებად გამოტანა
print("გასაღებები და მნიშვნელობები წყვილებად:")
for key, value in my_car.items():
    print(f"{key}: {value}")

# გასაღებების ცალ-ცალკე გამოტანა
print("გასაღებები:")
for key in my_car.keys():
    print(key)

# მნიშვნელობების ცალ-ცალკე გამოტანა
print("მნიშვნელობები:")
for value in my_car.values():
    print(value)

# 2. სეტები და მათი ოპერაციები
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# სეტების გაერთიანება
union_set = set1.union(set2)
print(f"გაერთიანება: {union_set}")

# განსხვავებები
difference1 = set1.difference(set2)
difference2 = set2.difference(set1)
print(f"განსხვავება (set1 - set2): {difference1}")
print(f"განსხვავება (set2 - set1): {difference2}")

# მსგავსებები
intersection_set = set1.intersection(set2)
print(f"მსგავსებები: {intersection_set}")

# 3. დიქშენერის მნიშვნელობების for ციკლით გამოტანა
my_dict = {
    "a": 10,
    "b": 20,
    "c": 30
}

print("\nდიქშენერის მნიშვნელობები for ციკლით:")
for value in my_dict.values():
    print(value)

# 4. დიქშენერი და სეტები (კომენტარები)
# Dictionary არის მონაცემთა ტიპი რომელიც ინახავს keys და values წყვილებს
# გასაღებები უნდა იყოს უნიკალური და უცვლელი 
# მნიშვნელობები შეიძლება იყოს ნებისმიერი ტიპის.


# Set არის მონაცემთა ტიპი რომელიც ინახავს უნიკალურ ელემენტებს
# სეტი არ არის დალაგებული და არ უშვებს დუბლიკატებს


# 5. 
new_dict = {"x": 100, "y": 200, "z": 300}
my_list = []

for key, value in new_dict.items():
    my_list.append((key, value))

print(f"სია: {my_list}")

# 6. 
my_dict2 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

new_key = input("შეიყვანეთ გასაღები: ")
new_value = input("შეიყვანეთ მნიშვნელობა: ")

if new_key not in my_dict2:
    my_dict2[new_key] = new_value
    print(f"დამატებულია: {new_key}: {new_value}")
    print(my_dict2)
else:
    print("Key already exists!")