def solve(s):
    up, low = 0, 0
    for i in s:
        if i == i.upper(): up += 1
        elif i == i.lower(): low += 1
    if up > low: return s.upper()
    else: return s.lower()
    
