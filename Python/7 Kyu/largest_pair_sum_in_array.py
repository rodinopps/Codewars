def largest_pair_sum(numbers): 
    big1 = max(numbers)
    numbers.remove(big1)
    big2 = max(numbers)
    return big1 + big2
