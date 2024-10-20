def largest(n, xs):
    new = sorted(xs)
    if n == 0: return []
    else: return new[-n:]
