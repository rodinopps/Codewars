def nickname_generator(name):
    if len(name) < 4: return "Error: Name too short"
    elif name[2] in "aeiou": return name[:4]
    else: return name[:3]
