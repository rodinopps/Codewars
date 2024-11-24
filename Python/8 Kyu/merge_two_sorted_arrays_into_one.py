def merge_arrays(arr1, arr2):
    list = (arr1 + arr2)
    list.sort()
    new = []
    for i in list:
        if i not in new: new.append(i)
    return new
