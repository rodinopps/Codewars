def seq_to_one(n):
    list = []
    if n > 0:
        for i in range(n, 0, -1):
            list.append(i)
    else:
        for i in range(n, 2):
            list.append(i)
    return list
