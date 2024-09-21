def square_digits(num):
    total = ""
    for i in str(num):
        total += str(int(i) ** 2)
    return int(total)
