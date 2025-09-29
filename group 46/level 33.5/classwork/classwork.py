# 1

def maskify(string):
    if len(string) <= 4:
        return string
    return "#" * (len(string) - 4) + string[-4:]

# 2

def solution(text, ending):
    return text.endswith(ending)

# 3

def remove_url_anchor(url):
    return url.split('#')[0]

# 4

def capitals(word):
    return [i for i in range(len(word)) if word[i].isupper()]

# 5

def sum_cubes(n):
    return sum(i**3 for i in range(1, n+1))

# 6

def solution(nums):
    if not nums:
        return []
    return sorted(nums)

