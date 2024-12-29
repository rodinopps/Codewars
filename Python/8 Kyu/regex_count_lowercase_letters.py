def lowercase_count(strng):
    count = 0
    for i in strng:
        if i in "abcdefghijklmnopqrstuvwxyz": count += 1
    return count
