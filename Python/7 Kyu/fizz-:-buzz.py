def solution(number):
    three, five, both = 0, 0, 0
    for i in range(number):
        if i % 3 == 0 and i % 5 == 0:
            both += 1
        elif i % 5 == 0:
            five += 1
        elif i % 3 == 0:
            three += 1
    return [three, five, both - 1]
