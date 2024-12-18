def find_outlier(integers):
    check = []
    for i in integers:
        check.append(i % 2 == 0)
    if check.count(True) == 1:
        for i in integers:
            if i % 2 == 0: return i
    else:
        for i in integers:
            if i % 2 != 0: return i
