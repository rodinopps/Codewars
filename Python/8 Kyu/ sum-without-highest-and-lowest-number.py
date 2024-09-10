def sum_array(arr):
    if arr == None or len(arr) == 1 or arr == []:
        return 0
    else:
        big = max(arr)
        small = min(arr)
        return sum(arr) - small - big
