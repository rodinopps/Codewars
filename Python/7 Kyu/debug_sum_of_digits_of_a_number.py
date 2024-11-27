def get_sum_of_digits(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum
