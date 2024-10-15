def square_or_square_root(arr):
    new = []
    for i in arr:
        if i **0.5 == int(i **0.5): new.append(i **0.5)
        else: new.append(i ** 2)
    return new
