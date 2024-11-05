def vowel_one(s):
    binary = ""
    for i in s:
        if i.lower() in "aeiou": binary += "1"
        else: binary += "0"
    return binary
