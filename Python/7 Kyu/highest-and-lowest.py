def high_and_low(numbers):
    check = list(map(int, numbers.split()))
    return str(max(check)) + " " + str(min(check))
