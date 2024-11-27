def pig_it(text):
    words = text.split()
    for i in range(len(words)):
        word = words[i]
        if word.isalpha():
            words[i] = word[1:] + word[0] + "ay"
    return " ".join(words)
