def has_unique_chars(string):
    special = ""
    for i in string:
        if i in special: return False
        else: special += i
    return True
