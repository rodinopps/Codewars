def greatest_common_factor(seq):
    big = max(seq)
    while True:
        list = []
        for i in seq:
            if i % big != 0:
                list.append(False)
                big -= 1
        if False not in list: return big
