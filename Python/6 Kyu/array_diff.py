def array_diff(a, b):
    new = []
    for i in a:
        if i not in b: new.append(i)
    return new
