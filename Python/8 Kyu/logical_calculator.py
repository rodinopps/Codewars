def logical_calc(array, op):
    if op == "AND": return False not in array
    elif op == "OR": return True in array
    elif op == "XOR": return sum(array) % 2 == 1
