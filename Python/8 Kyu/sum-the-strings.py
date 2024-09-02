def sum_str(a, b):
    if a == "" and b == "":
        return "0"
    elif a == "":
        return str(int(b))
    elif b == "":
        return str(int(a))
    else:
        return str(int(a) + int(b))
