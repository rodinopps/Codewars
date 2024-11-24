geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    list = []
    for i in birds:
        if i not in geese: list.append(i)
    return list
