#Ɔ⅁ꞱⱯ

lower_to_upper = {"A":"Ɐ", "T":"Ʇ", "G":"⅁", "C":"Ɔ", " ":" "}
upper_to_lower = {"Ɐ":"A", "Ʇ":"T", "⅁":"G", "Ɔ":"C", " ":" "}

class STRAND:
    
    def __init__(self,lower=""):
        for c in lower:
            if c not in "ATGC ":
                raise Exception(f"{c} is not a valid base")
        self.lower = lower        
        self.upper = " "*len(lower)
    
    def __str__(self):
        return f"{self.upper}\n{self.lower}"
    
    # Rotates the STRAND by 180 degrees
    def switch(self):
        new_lower = "".join([upper_to_lower[s] for s in self.upper[::-1]])
        new_upper = "".join([lower_to_upper[s] for s in self.lower[::-1]])
        
        self.lower = new_lower
        self.upper = new_upper

#def ENZYME(strand,start,instructions):
#    copy_mode = False
    

gene = STRAND("ACAGGGT")
gene.upper =  "Ʇ⅁     "
print(gene)
gene.switch()
print(gene)
