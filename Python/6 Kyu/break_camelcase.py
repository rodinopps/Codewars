def solution(s):
    word = ""
    for i in s:
        if i == i.upper(): word += " " + i
        else: word += i
    return word
