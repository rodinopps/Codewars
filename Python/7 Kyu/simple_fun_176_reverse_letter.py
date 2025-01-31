def reverse_letter(st):
    new = ""
    for i in st:
        if i in "abcdefghijklmnopqrstuvwxyz": new += i
    return new[::-1]
