def enough(cap, on, wait):
    left = cap - on
    if left - wait >= 0:
        return 0
    else:
        return abs(left - wait)
