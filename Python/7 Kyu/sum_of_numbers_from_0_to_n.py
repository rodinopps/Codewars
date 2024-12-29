def show_sequence(n):
    if n == 0: return "0=0"
    elif n < 0: return f"{n}<0"
    else:
        list, sum = [], 0
        for i in range(n + 1):
            list.append(str(i))
            sum += i
        return f"{'+'.join(list)} = {sum}" 
