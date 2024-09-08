def check_exam(arr1,arr2):
    score = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            score += 4
        elif arr2[i] == "":
            continue
        else:
            score -= 1
    return max(score, 0)
