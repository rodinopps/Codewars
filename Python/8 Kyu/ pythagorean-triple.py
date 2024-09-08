def pythagorean_triple(integers):
    integers.sort()
    if integers[2] ** 2 == integers[0] ** 2 + integers[1] ** 2:
        return True
    else:
        return False
