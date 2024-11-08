def calc(x):
    new = ""
    total1 = 0
    total2 = 0
    for i in x:
        new += str(ord(i))
    old = new
    new = new.replace("7", "1")
    for i in old:
        total1 += int(i)
    for i in new:
        total2 += int(i)
    return total1 - total2
