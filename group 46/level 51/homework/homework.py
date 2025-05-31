# 1) საყიდლების სიის tuple-ის შექმნა და unpacking
shopping_list = ("პური", "რძე", "კვერცხი", "ყველი")
item1, item2, item3, item4 = shopping_list
print(item1)
print(item2)
print(item3)
print(item4)

# 2) Fast food პროდუქტების tuple-ის შექმნა და შემდეგ ჯანსაღი პროდუქტების დამატება (ახალი tuple-ის შექმნით)
fast_food = ("ბურგერი", "პიცა", "კარტოფილი ფრი")
healthy_food = ("ვაშლი", "ბანანი", "სალათის ფურცლები")
all_food = fast_food + healthy_food
print(all_food)

# 3) Asterisk-ის ფუნქციის ახსნა კომენტარის სახით
# Asterisk (*) გამოიყენება tuple-ის (და სხვა iterable-ების) unpacking-ის დროს,
# რათა მოხდეს დარჩენილი ელემენტების შეგროვება ერთ ცვლადში, რომელიც იქნება სია (list).
# ის აღინიშნება სიმბოლოთი: *.

# 4) მოცემული tuple-ის unpacking
months = ("January", "February", "March", "April", "May")
first, second, third, *fourth = months

print(first)
print(second)
print(third)
print(fourth) 
