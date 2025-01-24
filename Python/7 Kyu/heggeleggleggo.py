def heggeleggleggo(word):
    new = ""
    for i in word:
        new += i
        if i.lower() not in "aioue ": new += "egg"
    return new
