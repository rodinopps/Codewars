def evil(n):
    binary = str(bin(n))
    one = binary.count("1")
    if one % 2 == 0: return "It's Evil!"
    else: return "It's Odious!"
