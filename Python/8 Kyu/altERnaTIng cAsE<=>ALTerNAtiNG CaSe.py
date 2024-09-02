def to_alternating_case(string):
    new = ""
    for i in string:
        if i == i.lower():
            new += i.upper()
        else:
            new += i.lower()
    return new
