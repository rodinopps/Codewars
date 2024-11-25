def sum_mul(n, m):
    sum = 0
    if n <= 0 or m <= 0: return "INVALID"
    else:
        for i in range(n, m, n):
            sum += i
    return sum
