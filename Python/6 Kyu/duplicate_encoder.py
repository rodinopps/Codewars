def duplicate_encode(word):
    new = ""
    for i in word.lower():
        if word.lower().count(i) == 1: new += "("
        else: new += ")"
    return new
