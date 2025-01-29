def max_product(lst, n_largest_elements):
    total = 1
    for i in range(n_largest_elements):
        total *= max(lst)
        lst.remove(max(lst))
    return total
