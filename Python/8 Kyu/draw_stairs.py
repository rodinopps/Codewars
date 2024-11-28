def draw_stairs(n):
    space = " "
    string = ""
    for i in range(1, n):
        string += "I\n" + space * i
    return string + "I"
