def to_camel_case(text):
    if text == "": return ""
    else:
        new = ""
        x = text.replace("_", " ")
        y = x.replace("-", " ")
        for i in y.title():
            if i.lower() in "abcdefghijklmnopqrstuvwxyz": new += i
        if text[0] == text[0].upper(): return new
        else: return new[0].lower() + new[1:]
