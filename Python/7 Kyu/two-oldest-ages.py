def two_oldest_ages(ages):
    old1 = max(ages)
    ages.remove(old1)
    old2 = max(ages)
    ages.remove(old2)
    return [old2, old1]
