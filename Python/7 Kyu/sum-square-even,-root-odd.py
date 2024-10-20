def sum_square_even_root_odd(nums):
    new = []
    for i in nums:
        if i % 2 == 0: new.append(i ** 2)
        else: new.append(i ** 0.5)
    return round(sum(new), 2)
