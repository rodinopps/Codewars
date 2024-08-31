def shortcut( s ):
    list = ["a", "e", "i", "o", "u"]
    check = ""
    for i in s:
        if i not in list:
            check += i
    return check
