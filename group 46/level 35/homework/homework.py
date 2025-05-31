# 1

def to_jaden_case(string):
    # გაყოფა სიტყვებად
    words = string.split()
    

    capitalized_words = [word.capitalize() for word in words]
    
    # დაბრუნდება გაერთიანებული სია
    return ' '.join(capitalized_words)

# 2

def sequence_sum(begin_number, end_number, step):
    # თუ begin_number უფრო მეტია end_number-ზე, დაბრუნე 0
    if begin_number > end_number:
        return 0
    
    total_sum = 0
    
    # გამავლობა sequence-ში და გადამოწმება ყოველი ნაბიჯისთვის
    for num in range(begin_number, end_number + 1, step):
        total_sum += num
    
    return total_sum

# 3

def lowercase_count(strng):
    # სულ მცირე ასოების რაოდენობის გადათვლას აკეთებს
    count = 0
    for char in strng:
        if char.islower():
            count += 1
    return count

# 4

def better_than_average(class_points, your_points):
    # კლასი ქულების საშუალო რაოდენობა
    average_score = sum(class_points) / len(class_points)
    
    # შეადარე შენი ქულა საშუალო ქულას
    return your_points > average_score

# 5

def grow(arr):
    result = 1  # იწყებთ 1-ით რადგან გამრავლების შედეგად 1-დან დაწყება არ ცვლის შედეგს
    for num in arr:
        result *= num  # ყოველ ელემენტს გამოვივლით
    return result

# 6

def smash(words):
    return " ".join(words)

# 7

def manual_join(words):
    result = ""  # სტრინგი სადაც შევკრავთ სიტყვებს
    for i, word in enumerate(words):
        if i > 0:
            result += " "  
        result += word  # დაამატე სიტყვა
    return result


