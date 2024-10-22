def replace_exclamation(st):
    new = ""
    for i in st:
        if i in "aeiouAEIOU": new += "!"
        else: new += i
    return new
