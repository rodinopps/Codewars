def DNA_strand(dna):
    string = ""
    for i in dna:
        if i == "A": string += "T"
        elif i == "T": string += "A"
        elif i == "C": string += "G"
        elif i == "G": string += "C"
    return string
