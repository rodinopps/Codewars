def descending_order(num):
    list = []
    for i in str(num):
        list.append(i)
    x = sorted(list, reverse = True)
    return int("".join(x))
