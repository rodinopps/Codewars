def calculate_years(principal, interest, tax, desired):
    year = 0
    while principal < desired:
        principal += principal * interest * (1 - tax)
        year += 1
    return year
