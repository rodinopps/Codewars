def check_vowel(strng, position):
    if len(strng) < position or position < 0:
        return False
    else:
        return strng[position] in "AEIOUaeiou"
