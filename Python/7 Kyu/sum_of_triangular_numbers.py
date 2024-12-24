def sum_triangular_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += 0.5 * i ** 2 + 0.5 * i
    return sum
