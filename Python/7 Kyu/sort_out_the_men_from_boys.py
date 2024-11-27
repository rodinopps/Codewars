def men_from_boys(arr):
    even = []
    odd = []
    for i in arr:
        if i % 2 == 0 and i not in even: even.append(i)
        elif i % 2 == 1 and i not in odd: odd.append(i)
    return sorted(even) + (sorted(odd)[::-1])
