def distinct(seq):
    list = []
    for i in seq:
        if i not in list: list.append(i)
    return list
