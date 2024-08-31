def find_it(seq):
    for i in seq:
        num = seq.count(i)
        if num % 2 == 1:
            return i
        
