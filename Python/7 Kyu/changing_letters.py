def swap(st):
    new = ""
    for i in st:
        if i in "aeiou": new += i.upper()
        else: new += i
    return new
