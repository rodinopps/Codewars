def calculate(num1, operation, num2):
    if operation == "+": return num1 + num2
    elif operation == "-": return num1 - num2
    elif operation == "*": return num1 * num2
    elif operation == "/":
        if num2 == 0 or num1 == 0: return None
        else: return num1 / num2
        
