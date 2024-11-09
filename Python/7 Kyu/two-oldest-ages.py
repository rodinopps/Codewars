def two_oldest_ages(ages):
    big1 = max(ages)
    ages.remove(big1)
    big2 = max(ages)
    return [big2, big1]
