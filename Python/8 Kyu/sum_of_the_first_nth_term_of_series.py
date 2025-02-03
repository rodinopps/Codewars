def series_sum(n):
    denom, sum = 1, 0
    for i in range(1, n + 1):
        sum += 1 / denom
        denom += 3
    return f"{sum:.2f}"
