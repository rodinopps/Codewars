def binary_array_to_number(arr):
    bit, total = 2 ** (len(arr) - 1), 0
    for i in arr:
        if i == 1:
            total += bit
            bit //= 2
        else: bit //= 2
    return total
