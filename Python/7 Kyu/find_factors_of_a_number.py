def factors(x):
    list = []
    if isinstance(x, int) and x >= 1:
        for i in range(1, x + 1):
            if x % i == 0: list.append(i)
        return list[::-1]
    else:
        return -1
