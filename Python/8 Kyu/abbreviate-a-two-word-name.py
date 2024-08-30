def abbrev_name(name):
    first, last = name.split()
    initial = first[0].upper() + "." + last[0].upper()
    return initial
