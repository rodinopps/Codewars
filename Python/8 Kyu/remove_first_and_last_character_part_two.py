def array(string):
    x = string.split(",")
    if len(x) > 2: return " ".join(x[1:-1])
    else: return None
