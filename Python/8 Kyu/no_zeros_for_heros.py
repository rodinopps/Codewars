def no_boring_zeros(n):
    if str(n)[-1] != "0" or len(str(n)) == 1: return n
    else:
        while n % 10 == 0:
            n //= 10
        return n
