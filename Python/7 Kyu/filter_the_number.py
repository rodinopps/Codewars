def filter_string(st):
    str = ""
    for i in st:
        if i in "1234567890": str += i
    return int(str)
