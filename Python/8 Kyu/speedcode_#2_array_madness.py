def array_madness(a,b):
    total_a, total_b  = 0, 0
    for i in a:
        total_a += i ** 2
    for i in b:
        total_b += i ** 3
    return total_a > total_b
