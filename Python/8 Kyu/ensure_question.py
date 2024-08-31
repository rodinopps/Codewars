def ensure_question(s):
    if s and s[-1] == "?":
        return s
    else:
        return s + "?"
