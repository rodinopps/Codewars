def solve(a,b):
    while True:
        if a == 0 or b == 0:
            return [a, b]
            break
        elif a >= 2 * b: a = a - 2 * b
        elif b >= 2 * a: b = b - 2 * a
        else:
            return [a, b]
            break
