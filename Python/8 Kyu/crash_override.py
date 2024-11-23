def alias_gen(f_name, l_name):
    check = "1234567890"
    if f_name[0] in check or l_name[0] in check: return "Your name must start with a letter from A - Z."
    else: return f"{FIRST_NAME[f_name[0].upper()]} {SURNAME[l_name[0].upper()]}"
