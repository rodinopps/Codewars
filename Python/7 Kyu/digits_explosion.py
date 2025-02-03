def explode(s):
    string = ""
    for i in s:
        string += i * int(i)
    return string
