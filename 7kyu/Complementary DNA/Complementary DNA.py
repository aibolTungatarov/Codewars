def DNA_strand(dna):
    res = ""
    dict = {"A":"T","T":"A","C":"G","G":"C"}
    for letter in dna:
        res += dict[letter]
    return res 
