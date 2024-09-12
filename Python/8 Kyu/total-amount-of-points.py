def points(games):
    score = 0
    for i in games:
        if i[0] > i[2]:
            score += 3
        elif i[0] == i[2]:
            score += 1
    return score
