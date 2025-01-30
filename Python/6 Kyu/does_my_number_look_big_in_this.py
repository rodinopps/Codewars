def narcissistic( value ):
    total = 0
    for i in str(value):
        total += int(i) ** len(str(value))
    return total == value
