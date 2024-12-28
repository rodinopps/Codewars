def is_triangle(a, b, c):
    list = sorted([a, b, c])
    return list[0] + list[1] > list[2]
