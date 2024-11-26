def string_clean(s):
    new = ""
    for i in s:
        if i not in "1234567890": new += i
    return new
