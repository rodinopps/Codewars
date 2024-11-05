def to_acronym(inp):
    words = inp.split()
    emp = ""
    for i in words:
        emp += i[0]
    return emp.upper()
