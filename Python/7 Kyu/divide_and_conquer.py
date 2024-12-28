def div_con(x):
    non, string = 0, 0
    for i in x:
        if i == int(i): non += i
        else: string += int(i)
    return non - string
