def multi_table(number):
    table = ""
    for i in range(1, 11):
        if i < 10:
            table += f"{i} * {number} = {i * number}\n"
        else: 
            table += f"{i} * {number} = {i * number}"
    return table
