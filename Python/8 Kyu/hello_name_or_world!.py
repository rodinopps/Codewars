def hello(name = ""):
    name = name.strip()
    if name == "":
        return "Hello, World!"
    else:
        return "Hello, " + name.capitalize() + "!"
