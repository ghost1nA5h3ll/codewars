def DNA_strand(dna):
    if dna:
        result = ""
        for i in dna:
            if i == "A":
                result += "T"
            if i == "T":
                result += "A"
            if i == "G":
                result += "C"
            if i == "C":
                result += "G"
        return result
    else:
        return False
