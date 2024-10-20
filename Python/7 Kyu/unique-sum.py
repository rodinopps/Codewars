def unique_sum(lst):
    new = []
    for i in lst:
        if i not in new: new.append(i)
    if new == []: return None
    else: return sum(new)
