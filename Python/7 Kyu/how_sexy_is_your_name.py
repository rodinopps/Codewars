def sexy_name(name):
    score = 0
    for i in name.upper():
        if i in SCORES:
            score += SCORES[i]
    if score <= 60: return "NOT TOO SEXY"
    elif 61 <= score <= 300: return "PRETTY SEXY"
    elif 301 <= score <= 599: return "VERY SEXY"
    elif score >= 600: return "THE ULTIMATE SEXIEST"
