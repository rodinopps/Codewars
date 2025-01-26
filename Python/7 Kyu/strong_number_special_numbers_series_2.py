def strong_num(number):
    sum = 0
    for i in str(number):
        fact = 1
        for j in range(1, int(i) + 1):
            fact *= j
        sum += fact
    if sum == number: return "STRONG!!!!"
    else: return "Not Strong !!"
