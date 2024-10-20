def rad_ladies(name):
    string = ""
    for i in name:
        if i not in "1234567890%$&/£?@":
            string += i
    return string.upper()
