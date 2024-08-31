def reverse_words(s):
    list = s.split()
    list.reverse()
    result = ' '. join(list)
    return result
