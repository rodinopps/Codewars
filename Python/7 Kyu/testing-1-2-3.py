def number(lines):
    list = []
    if lines == []:
        return list
    else:
        for i in range(len(lines)):
            list.append(str(i + 1) + ": " + lines[i])
    return list
