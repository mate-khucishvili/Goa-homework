# 1-Rock Paper Scissors!
def rps(p1, p2):
    yvela_varianti = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if yvela_varianti[p1] == p2:
        return "Player 1 won!"
    if yvela_varianti[p2] == p1:
        return "Player 2 won!"
    return "Draw!"

# 2-Quarter of the year
def quarter_of(month):
    return (month + 2) // 3

# 3-altERnaTIng cAsE <=> ALTerNAtiNG CaSe
def to_alternating_case(string):
    result = ""
    for i in string:
        if i.isupper():
            result += i.lower()
        else:
            result += i.upper()
    return result

# 4-Growth of a Population
def nb_year(p0, percent, aug, p):
    year = 0
    while p0 < p:
        p0 = p0 + p0 * percent // 100 + aug # ახალი p0 = ძველი p0 + პროცენტული ზრდა + დამატება
        year += 1
    return year

# 5-Count the Monkeys!
def monkey_count(n):
    return list(range(1, n+1))

# 7-Count the divisors of a number
def divisors(n):
    result = [] 
    for i in range(1,n + 1): 
        if n % i == 0: 
            result.append(i) 
    return len(result) 