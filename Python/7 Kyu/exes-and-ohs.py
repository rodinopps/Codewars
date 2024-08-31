def xo(s):
    x = s.count("x")
    x2 = s.count("X")
    o = s.count("o")
    o2 = s.count("O")
    if x + x2 == o + o2:
        return True
    else:
        return False
