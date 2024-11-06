def remove_duplicate_words(s):
    string = []
    list = s.split()
    for i in list:
        if i not in string:
            string.append(i)
    return " ".join(string)
