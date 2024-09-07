def count_positives_sum_negatives(arr):
    pos = 0
    neg = 0
    if arr == []:
        return []
    else:
        for i in arr:
            if i > 0:
                pos += 1
            else:
                neg += i
        return [pos, neg]
