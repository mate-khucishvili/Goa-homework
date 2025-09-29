# 1. append() - სიის ბოლოში ელემენტის დამატება
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  



# 2. remove() - სიიდან ელემენტის წაშლა
my_list = [1, 2, 3, 4]
my_list.remove(3)
print("remove():", my_list) 



# 3. sort() - სიის დალაგება
my_list = [4, 2, 1, 3]
my_list.sort()
print(my_list)  



# 4. pop() - სიის ბოლო ელემენტის წაშლა და დაბრუნება
my_list = [1, 2, 3, 4]
last_element = my_list.pop()
print(last_element)  
print(my_list)  



# 5. count() - ელემენტის რაოდენობის დათვლა სიაში
my_list = [1, 2, 2, 3, 2]
count = my_list.count(2)
print(count)  



# 6. extend() - სიის გაფართოება სხვა სიით
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  



# 7. index() - ელემენტის ინდექსის პოვნა
my_list = [10, 20, 30, 40]
index = my_list.index(30)
print(index) 



# 8. insert() - ელემენტის ჩასმა კონკრეტულ ინდექსზე
my_list = [1, 2, 3]
my_list.insert(1, 99)
print(my_list)  



# 9. reverse() - სიის შებრუნება
my_list = [1, 2, 3, 4]
my_list.reverse()
print(my_list) 



# 10. clear() - სიის გასუფთავება
my_list = [1, 2, 3, 4]
my_list.clear()
print( my_list) 