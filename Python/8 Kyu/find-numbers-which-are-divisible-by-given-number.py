def divisible_by(numbers, divisor):
    list = []
    for i in numbers:
        if i % divisor == 0: list.append(i)
    return list
