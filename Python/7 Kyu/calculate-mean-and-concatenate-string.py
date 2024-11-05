def mean(lst):
    total, letters = 0, ""
    for i in lst:
        if i in "1234567890": total += int(i)
        else: letters += i
    return [total / 10, letters]
