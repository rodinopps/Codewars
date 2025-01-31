def factorial(n):
    if 0 <= n <= 12:
        sum = 1
        for i in range(1, n + 1):
            sum *= i
        return sum
    else: raise ValueError("ERROR")
