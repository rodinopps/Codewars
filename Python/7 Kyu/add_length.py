def add_length(str_):
    list = str_.split()
    length = []
    for i in list:
        length.append(i + " " + str(len(i)))
    return length
