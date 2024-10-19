def remainder(a,b):
    small = min(a, b)
    if small == a:
        if a == 0: return None
        else: return b % a
    elif small == b:
        if b == 0: return None
        else: return a % b
