def solve(s):
    upper, lower, num, special = 0, 0, 0, 0
    for i in s:
        if i in "1234567890": num += 1
        elif i in "!@#$%^&*()_+-=[]{}|;':\",.<>/?`~": special += 1
        elif i == i.upper(): upper += 1
        else: lower += 1
    return [upper, lower, num, special]
