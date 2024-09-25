def vaporcode(s):
    string = ""
    for i in s.replace(" ", ""):
        string += i.upper() + "  "
    return string[:-2]
