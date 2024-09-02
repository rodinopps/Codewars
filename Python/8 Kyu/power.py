def number_to_pwr(number, p):
    total = 1
    for i in range(p):
        total *= number
    return total
