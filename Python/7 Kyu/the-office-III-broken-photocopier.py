def broken(inp):
    new = ""
    for i in inp:
        if i == "1": new += "0"
        else: new += "1"
    return new
