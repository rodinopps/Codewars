def spin_words(sentence):
    list = sentence.split()
    for i in range(len(list)):
        if len(list[i]) >= 5:
            list[i] = list[i][::-1]
    return " ". join(list)
