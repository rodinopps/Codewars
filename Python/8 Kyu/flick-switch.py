def flick_switch(lst):
    list = []
    current = True
    for i in lst:
        if i == "flick":
            current = not(current)
            list.append(current)
        else:
            list.append(current)
    return list
