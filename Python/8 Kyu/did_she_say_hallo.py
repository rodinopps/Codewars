def validate_hello(greetings):
    lang = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    for i in lang:
        if i in greetings.lower(): return True
    return False
