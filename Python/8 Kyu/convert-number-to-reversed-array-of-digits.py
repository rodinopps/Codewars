def digitize(n):
    list = []
    reverse = str(n)[::-1]
    for i in reverse:
        list.append(int(i))
    return list
