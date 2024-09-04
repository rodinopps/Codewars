def cube_checker(volume, side):
    if volume >= 1 and side >= 1 and ((volume / side) / side) / side == 1:
        return True
    else:
        return False
