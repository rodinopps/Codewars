def find_short(s):
    list = s.split()
    new = []
    for i in list:
        new.append(len(i))
    return min(new)
