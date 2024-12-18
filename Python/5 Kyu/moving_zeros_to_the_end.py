def move_zeros(lst):
    list = []
    zero = lst.count(0)
    for i in lst:
        if i != 0: list.append(i)
    for i in range(zero):
        list.append(0)
    return list
