def fold_to(distance):
    paper, count = 0.0001, 0
    if distance < 0: return None
    elif distance < paper: return 0
    else:
        while distance > paper:
            paper *= 2
            count += 1
    return count
