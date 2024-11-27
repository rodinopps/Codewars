def correct_polish_letters(st): 
    new = ""
    char = {
    'ą': 'a','ć': 'c','ę': 'e',
    'ł': 'l','ń': 'n','ó': 'o',
    'ś': 's','ź': 'z','ż': 'z'
    }
    for i in st:
        if i in char: new += char[i]
        else: new += i
    return new
