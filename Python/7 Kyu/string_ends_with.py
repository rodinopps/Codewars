def solution(text, ending):
    return text[len(text) - len(ending):] == ending
