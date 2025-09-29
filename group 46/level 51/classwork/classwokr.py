# 1) კომენტარის სახით ახსნა

# List-ები(სია): ცვალებადია კვადრატულ ფრჩხილებში [].
# Tuple-ები: უცვლელია მრგვალ ფრჩხილებში ().

#  2) 5 საყვარელი ფილმის Tuple და პირველი/ბოლო ელემენტის დაბეჭდვა:

fav_movies = ("Lamborghini: The Man Behind the Legend", "World War Z", "Interstellar", "The Godfather", "Gran Turismo")

print("პირველი ფილმი:", fav_movies[0])
print("ბოლო ფილმი:", fav_movies[-1])


# 3) კვირის დღეების Tuple და მათი unpacking:

weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

monday, tuesday, wednesday, thursday, friday, saturday, sunday = weekdays

print("ორშაბათი:", monday)
print("სამშაბათი:", tuesday)
print("ოთხშაბათი:", wednesday)
print("ხუთშაბათი:", thursday)
print("პარასკევი:", friday)
print("შაბათი:", saturday)
print("კვირა:", sunday)

# 4) ელემენტის არსებობის შემოწმება Tuple-ში:

tuple = (1, 2, 3, 4, 5)

if 3 in tuple:
    print("3 არსებობს tuple-ში")
else:
    print("3 არ არსებობს tuple-ში")

if 6 in tuple:
    print("6 არსებობს tuple-ში")
else:
    print("6 არ არსებობს tuple-ში")

# 5) მოცემულია tuple და შედეგი რა გამოვა

fruits = ("banana", "cherry", "strawberry", "raspberry")
(first, *second, third) = fruits

print(first) # Output: banana
print(second) # Output: ['cherry', 'strawberry']
print(third) # Output: raspberry
