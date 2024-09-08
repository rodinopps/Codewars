def divisors(integer):
    list = []
    for i in range(2, integer):
        if integer % i == 0:
            list.append(i)
    if list == []:
        return str(integer) + " is prime"
    else:
        return list
