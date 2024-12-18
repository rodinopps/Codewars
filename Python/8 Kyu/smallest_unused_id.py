def next_id(arr):
    n = 0
    while True:
        if n not in arr: return n
        else: n += 1
