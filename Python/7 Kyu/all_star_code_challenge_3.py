def remove_vowels(strng):
    new = ""
    for i in strng:
        if i not in "aeiouAEIOU": new += i
    return new
