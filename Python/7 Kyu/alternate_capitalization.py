def capitalize(s):
    new1, new2 = "", ""
    count = 0
    for i in s:
        if count % 2 == 0:
            new1 += i.upper()
            new2 += i
        else:
            new1 += i
            new2 += i.upper()
        count += 1
    return [new1, new2]
