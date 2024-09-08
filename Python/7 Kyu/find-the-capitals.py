def capitals(word):
    list = []
    for i in range(len(word)):
        if word[i] == word[i].upper():
            list.append(i)
    return list
