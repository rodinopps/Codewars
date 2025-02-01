def tidyNumber(n):
    digits = list(str(n))
    return digits == sorted(digits)
