def neutralise(s1, s2):
    new = ""
    for i in range(len(s1)):
        if s1[i] == s2[i]: new += s1[i]
        else: new += "0"
    return new
