def two_highest(arg1):
    new = []
    for i in arg1:
        if i not in new: new.append(i)
    new.sort(reverse = True)
    return new[:2]
