# These don't work because ⅁ is the wrong width
#Ɔ⅁ꞱⱯ
#lower_to_upper = {"A":"Ɐ", "T":"Ʇ", "G":"⅁", "C":"Ɔ", " ":" ", "_":"_"}
#upper_to_lower = {"Ɐ":"A", "Ʇ":"T", "⅁":"G", "Ɔ":"C", " ":" ", "_":"_"}

class STRAND:
    
    def __init__(self,A="",B=""):

        # Check validity
        for string in [A,B]:
            for c in string:
                if c not in "ATGC ":
                    raise Exception(f"{c} is not a valid base")
    
        # If B isn't given then make A the lower string
        # If B is given then make A the upper string and B the lower string
        # This allows the common scenario where we just want the specify the lower
        # string and also lets us specify both an upper and lower string in a 
        # readable way
        if B == "":
            self.upper = " "*len(A)
            self.lower = A
        else:
            self.upper = A
            self.lower = B
    
    # No __repr__ method because the string has to be multiple lines
    def __str__(self):
        return f"{self.upper}\n{self.lower}"
    
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

 
def split_strand(strand):
    up = strand.lower
    lo = strand.upper
    
    U = [STRAND(s) for s in up.split(" ") if s != ""]
    L = [STRAND(s) for s in lo.split(" ") if s != ""]
    
    return U+L


amino_acids = ["cut","del","swi","mvr","mvl","cop","off","ina","inc",
               "ing","int","rpy","rpu","lpy","rpu"]

duplet_to_amino = {"AA":"   ", "AC":"cut", "AG":"del", "AT":"swi",
                   "CA":"mvr", "CC":"mvl", "CG":"cop", "CT":"off",
                   "GA":"ina", "GC":"inc", "GG":"ing", "GT":"int",
                   "TA":"rpy", "TC":"rpu", "TG":"lpy", "TT":"lpu"}

amino_to_duplet = {"   ":"AA", "cut":"AC", "del":"AG", "swi":"AT",
                   "mvr":"CA", "mvl":"CC", "cop":"CG", "off":"CT",
                   "ina":"GA", "inc":"GC", "ing":"GG", "int":"GT",
                   "rpy":"TA", "rpu":"TC", "lpy":"TG", "lpu":"TT"}

def chunk_size(L,n):
    return [L[i * n:(i + 1) * n] for i in range((len(L) + n - 1) // n )]

def string_to_amino(S):
    duplets = chunk_size(S,2)
    return [duplet_to_amino[d] for d in duplets if len(d) == 2 ]




class ENZYME:
    
    def __init__(self,strand,pos,instructions):
        if type(strand) != STRAND:
            raise Exception("not a valid strand")
        if type(pos) != int:
            raise Exception("pos must be an integer")
        for i in instructions:
            if i not in amino_acids:
                raise Exception(f"{i} is not a valid instruction")
        
        self.strand = strand
        self.pos = pos
        self.instructions = instructions
        self.copy_mode = False
        
    
    


#def ENZYME(strand,start,instructions):
#    copy_mode = False
    

gene = STRAND("TAGATCCAGTCCACATCGA",
              "GA  TTT            ")

print(gene)


for s in split_strand(gene):
    print(s,string_to_amino(s.lower))