def get_number_from_string(st):
    num = ""
    for i in st:
        if i in "1234567890": num += i
    return int(num)
