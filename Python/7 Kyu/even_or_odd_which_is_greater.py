def even_or_odd(s):
    even, odd = 0, 0
    for i in s:
        if int(i) % 2 == 0: even += int(i)
        else: odd += int(i)
    if even > odd: return "Even is greater than Odd"
    elif even < odd: return "Odd is greater than Even"
    else: return "Even and Odd are the same"
