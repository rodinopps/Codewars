def caffeine_buzz(n):
    if n % 12 == 0:
        if n % 2 == 0: return "CoffeeScript"
    elif n % 3 == 0:
        if n % 2 == 0: return "JavaScript"
        else: return "Java"
    else: return "mocha_missing!"
