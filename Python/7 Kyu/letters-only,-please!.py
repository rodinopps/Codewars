def remove_chars(s):
    letters = ""
    for i in s:
        if i.lower() in "abcdefghijklmnopqrstuvwxyz ": letters += i
    return letters
