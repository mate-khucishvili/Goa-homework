# 1) ფუნქცია რომელიც იღებს ორ რიცხვს და ბეჭდავს მათ ჯამს
def sum_numbers(a, b):
    print(a + b)

sum_numbers(5, 7)  


# 2) ფუნქცია რომელიც აბრუნებს ლუწია თუ კენტი რიცხვი
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

print(even_or_odd(10))
print(even_or_odd(15))


# 3) ფუნქცია რომელიც აბრუნებს დადებითია თუ უარყოფითი რიცხვი
def positive_or_negative(number):
    return "Positive" if number >= 0 else "Negative"

print(positive_or_negative(10))
print(positive_or_negative(-5))


# 4) ფუნქცია რომელიც იღებს სახელს და ბეჭდავს მისალმებას
def words(name):
    print(f"Hello {name}")

words("Giorgi")
words("Nino")


# 5) ფუნქცია რომელიც იღებს ორ სტრინგს და აბრუნებს მათ კონკატენაციას
def strings(str1, str2):
    return str1 + str2

print(strings("Hello ", "world!"))
