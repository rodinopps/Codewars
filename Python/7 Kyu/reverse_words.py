def reverse_words(text):
    list, new = text.split(" "), []
    for i in list:
        new.append(i[::-1])
    return " ".join(new)
