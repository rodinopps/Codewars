def repeats(arr):
    new = []
    for i in arr:
        if arr.count(i) == 1: new.append(i)
    return sum(new)
