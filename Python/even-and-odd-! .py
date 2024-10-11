def even_and_odd(n): 
    odd = ""
    even = ""
    for i in str(n):
        if int(i) % 2 == 0:
            even += i
        else:
            odd += i
    if even == "":
        return 0, int(odd)
    elif odd == "":
        return int(even), 0
    else:
        return int(even), int(odd)
