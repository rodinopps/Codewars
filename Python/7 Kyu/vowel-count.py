def get_count(sentence):
    total = 0
    for i in sentence:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            total += 1
    return total
