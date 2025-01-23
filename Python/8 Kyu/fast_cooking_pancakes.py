def cook_pancakes(n, m):
    total = n * 2
    if n == 1: return 2
    elif n < m: return 2
    else: return (total + m - 1) // m
