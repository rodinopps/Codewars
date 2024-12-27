def to_jaden_case(string):
    list, old = [], string.split()
    for i in old:
        list.append(i.capitalize())
    return " ".join(list)
