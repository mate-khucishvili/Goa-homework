# Task-1 - Remove duplicates from list
def distinct(seq):
    result = []  # ვქმნით ცარიელ სიას  რომელიც შეინახავს ელემენტებს

    for item in seq:  # გადავირბენთ მოცემული სიიდან ყველა ელემენტზე
        if item not in result:  # თუ ელემენტი ჯერ არ არის დამატებული საბოლოო სიაში
            result.append(item)  # ვამატებთ სიაში

    return result  # ვაბრუნებთ სიას უნიკალური ელემენტებით

# Task-2 - Get Planet Name By ID
def get_planet_name(id):
    return {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
    }.get(id)  # აბრუნებს პლანეტას თუ ID არსებობს მერე კი თუ არა — აბრუნებს None-ს

# Task-3 - Switch it Up!

def switch_it_up(number):
    return ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'][number]

# Task-4 - 5 without numbers !!
def unusual_five():
    return(len('Goooa'))
 
