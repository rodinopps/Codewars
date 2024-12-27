def accum(st):
    result = []
    for i in range(len(st)):
        result.append(st[i].upper() + st[i].lower() * i)
    return '-'.join(result)
