def duplicate_count(text):
    list, letters, total, new = [], [], 0, text.lower()
    for i in new:
        if i not in letters: letters.append(i)
    for i in letters:
        list.append(new.count(i))
    for i in list:
        if i != 1: total += 1
    return total
