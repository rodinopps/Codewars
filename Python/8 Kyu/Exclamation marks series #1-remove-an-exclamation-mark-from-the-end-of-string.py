def remove(s):
    if s == "":
        return ""
    elif s[-1] != "!":
        return s
    else:
        return s[:-1]
