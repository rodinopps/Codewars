def calculator(x,y,op):
    digits = "1234567890+-*/"
    if str(x) in digits and str(y) in digits and op in digits:
        if op == "+": return x + y
        elif op == "-": return x - y
        elif op == "*": return x * y
        elif op == "/": return x / y
    else: return "unknown value"
