def filter_list(l):
    list = []
    for i in l:
        if type(i) == int or type(i) == float: list.append(i)
    return list
