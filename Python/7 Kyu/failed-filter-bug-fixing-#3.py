def filter_numbers(string):
    return "".join(x for x in string if x not in "1234567890")
