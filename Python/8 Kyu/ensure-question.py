def ensure_question(s):
    if len(s) > 0 and s[-1] == "?": return s
    else: return s + "?"
