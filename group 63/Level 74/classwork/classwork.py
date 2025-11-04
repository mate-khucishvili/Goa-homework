# 1 - Ensure question
def ensure_question(s):
    if s == "":
        return "?"
    elif s[-1] == "?":
        return s
    else:
        return s + "?"
# 2 - Shortest Word
def find_short(s):
    return min(len(i) for i in s.split())

# 3 - Create Phone Number
def create_phone_number(array):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*array)