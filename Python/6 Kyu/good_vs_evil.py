def good_vs_evil(good, evil):
    good_list = good.split()
    evil_list = evil.split()
    good_value = [1, 2, 3, 3, 4, 10]
    evil_value = [1, 2, 2, 2, 3, 5, 10]
    good_total = 0
    evil_total = 0
    for i in range(len(good_list)):
        if good_list[i] != "0": good_total += good_value[i] * int(good_list[i])
    for i in range(len(evil_list)):
        if evil_list[i] != "0": evil_total += evil_value[i] * int(evil_list[i])
    if good_total > evil_total: return "Battle Result: Good triumphs over Evil"
    elif good_total < evil_total: return "Battle Result: Evil eradicates all trace of Good"
    else: return "Battle Result: No victor on this battle field"
