def fix(paragraph):
    text = paragraph.split(". ")
    new = []
    for i in text:
        new.append(i.capitalize())
    return ". ".join(new)
