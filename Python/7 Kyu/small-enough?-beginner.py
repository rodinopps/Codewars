def small_enough(array, limit):
    list = []
    for i in array:
        if i <= limit:
            list.append(True)
        else:
            list.append(False)
    if False in list:
        return False
    else:
        return True
