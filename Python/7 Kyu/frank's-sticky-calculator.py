def sticky_calc(operation, val1, val2):
    stick = str(round(val1)) + str(round(val2))
    if operation == "-": return round(int(stick) - round(val2))
    elif operation == "+": return round(int(stick) + round(val2))
    elif operation == "*": return round(int(stick) * round(val2))
    elif operation == "/": return round(int(stick) / round(val2))
