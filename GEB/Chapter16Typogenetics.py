# These don't work because ⅁ is the wrong width
#Ɔ⅁ꞱⱯ
#lower_to_upper = {"A":"Ɐ", "T":"Ʇ", "G":"⅁", "C":"Ɔ", " ":" ", "_":"_"}
#upper_to_lower = {"Ɐ":"A", "Ʇ":"T", "⅁":"G", "Ɔ":"C", " ":" ", "_":"_"}

class STRAND:
    
    def __init__(self,lower="",upper=""):

        for c in lower:
            if c not in "ATGC ":
                raise Exception(f"{c} is not a valid base")
        for c in upper:
            if c not in "ATGC ":
                raise Exception(f"{c} is not a valid base")
        
        if upper == "":
            self.upper = " "*len(lower)
        else:
            self.upper = upper
        self.lower = lower        
    
    def __str__(self):
        return f"\n{self.upper}\n{self.lower}"
    
    # Rotates the STRAND by 180 degrees
    def switch(self):
        new_lower = self.upper[::-1]
        new_upper = self.lower[::-1]
        
        self.lower = new_lower
        self.upper = new_upper
        
    def cut(self,n):
        L = STRAND(self.lower[:n],self.upper[:n])
        R = STRAND(self.lower[n:],self.upper[n:])
        return L,R


#def ENZYME(strand,start,instructions):
#    copy_mode = False
    

gene = STRAND("ACAGGGT",
              "TG     ")

print(gene)
gene.switch()
print(gene)
gene.switch()
print(gene)

L,R = gene.cut(4)
print(L)
print(R)