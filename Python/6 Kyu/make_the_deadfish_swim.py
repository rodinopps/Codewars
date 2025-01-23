def parse(data):
    sum, list = 0, []
    for i in data:
        if i == "i": sum += 1
        elif i == "d": sum -= 1
        elif i == "s": sum **= 2
        elif i == "o": list.append(sum)
    return list
