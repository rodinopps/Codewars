def find_multiples(integer, limit):
    list = []
    for i in range(integer, limit + 1, integer):
        list.append(i)
    return list
