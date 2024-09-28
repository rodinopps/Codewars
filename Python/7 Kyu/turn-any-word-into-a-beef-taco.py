def tacofy(word):  
    new = ["shell"]
    for i in word.lower():
        if i == "t":
            new.append("tomato")
        elif i == "l":
            new.append("lettuce")
        elif i == "c":
            new.append("cheese")
        elif i == "g":
            new.append("guacamole")
        elif i == "s":
            new.append("salsa")
        elif i in "aeiou":
            new.append("beef")
    new.append("shell")
    return new
