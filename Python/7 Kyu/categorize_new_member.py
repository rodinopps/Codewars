def open_or_senior(data):
    list = []
    for i in data:
        if i[0] >= 55 and i[1] > 7: list.append("Senior")
        else: list.append("Open")
    return list
