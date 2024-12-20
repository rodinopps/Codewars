def same_case(a, b): 
    letter = "abcdefghijklmnopqrstuvwxyz"
    if a.lower() not in letter or b.lower() not in letter: return -1
    elif a == a.upper() and b == b.lower() or a == a.lower() and b == b.upper(): return 0
    else: return 1
