def calculator(txt):
    new = txt.split(" ")
    if new[1] == "+": return new[0] + new[2]
    elif new[1] == "*": return new[0] * len(new[2])
    elif new[1] == "-": return (len(new[0]) - len(new[2])) * "."
    elif new[1] == "//": return (len(new[0]) // len(new[2])) * "."
