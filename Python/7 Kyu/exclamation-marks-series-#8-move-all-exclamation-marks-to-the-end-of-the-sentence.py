def remove(string : str) -> str:
    mark = string.count("!")
    new = string.replace("!", "")
    return new + "!" * mark
