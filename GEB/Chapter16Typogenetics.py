# These don't work because ⅁ is the wrong width
#Ɔ⅁ꞱⱯ
#lower_to_upper = {"A":"Ɐ", "T":"Ʇ", "G":"⅁", "C":"Ɔ", " ":" ", "_":"_"}
#upper_to_lower = {"Ɐ":"A", "Ʇ":"T", "⅁":"G", "Ɔ":"C", " ":" ", "_":"_"}


complement = {"A":"T", "T":"A", "G":"C", "C":"G"}

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
        # The internal upper and lower are lists so that they are mutable
        if B == "":
            self.upper = [" "]*len(A)
            self.lower = [a for a in A]
        else:
            self.upper = [a for a in A]
            self.lower = [b for b in B]
    
    # No __repr__ method because the string has to be multiple lines
    def __str__(self):
        if all([u == " " for u in self.upper]):
            return f"{''.join(self.lower)}"
        return f"{''.join(self.upper)}\n{''.join(self.lower)}"
    
    # Rotates the STRAND by 180 degrees
    def switch(self):
        new_lower = self.upper[::-1]
        new_upper = self.lower[::-1]
        
        self.lower = new_lower
        self.upper = new_upper
        
    def cut(self,pos):
        L = STRAND(self.lower[:pos+1],self.upper[:pos+1])
        R = STRAND(self.lower[1+pos:],self.upper[1+pos:])
        return L,R
    
    def insert(self,base,pos,copy_mode):
        if base not in "ATGC":
            raise Exception(f"{base} is not a valid base")
        
        new_lower = self.lower[:pos] + [base] + self.lower[pos:]
        if copy_mode:
            new_upper = self.upper[:pos] + [complement[base]] + self.upper[pos:]
        else:
            new_upper = self.upper[:pos] + [" "] + self.upper[pos:]
        self.lower = new_lower
        self.upper = new_upper
    
    def copy(self,pos):
        self.upper[pos] = complement[self.lower[pos]]
 
    def delete(self,pos):
        del self.lower[pos]
        del self.upper[pos]
        
    def __len__(self):
        return len(self.lower)
    
    
def split_strand(strand):
    up = "".join(strand.lower[::-1])
    lo = "".join(strand.upper)
    
    U = [STRAND(s) for s in up.split(" ") if s != ""]
    L = [STRAND(s) for s in lo.split(" ") if s != ""]
    
    return U+L





# Deal with duplets and amino acids
amino_acids = ["cut","del","swi","mvr","mvl","cop","off","ina","inc",
               "ing","int","rpy","rpu","lpy","lpu"]

duplet_to_amino = {"AA":"   ", "AC":"cut", "AG":"del", "AT":"swi",
                   "CA":"mvr", "CC":"mvl", "CG":"cop", "CT":"off",
                   "GA":"ina", "GC":"inc", "GG":"ing", "GT":"int",
                   "TA":"rpy", "TC":"rpu", "TG":"lpy", "TT":"lpu"}

amino_to_duplet = {"   ":"AA", "cut":"AC", "del":"AG", "swi":"AT",
                   "mvr":"CA", "mvl":"CC", "cop":"CG", "off":"CT",
                   "ina":"GA", "inc":"GC", "ing":"GG", "int":"GT",
                   "rpy":"TA", "rpu":"TC", "lpy":"TG", "lpu":"TT"}

amino_to_fold = {          "cut": 0, "del":0,  "swi":-1,
                 "mvr": 0, "mvl": 0, "cop":-1, "off": 1,
                 "ina": 0, "inc":-1, "ing":-1, "int": 1,
                 "rpy":-1, "rpu": 1, "lpy":1,  "lpu": 1}

direct_to_binding = {0:"A", 1:"C", 2:"T", 3:"G"}

def chunk_by_size(L,n):
    return [L[i * n:(i + 1) * n] for i in range((len(L) + n - 1) // n )]

def string_to_amino(S):
    duplets = chunk_by_size(S,2)
    return [duplet_to_amino[d] for d in duplets if len(d) == 2 ]

def aminos_to_binding(aminos):
    direct = 0
    for a in aminos[1:-1]:
        direct = (direct+amino_to_fold[a])%4
    return direct_to_binding[direct]





class ENZYME:
    
    def __init__(self,aminos):

        for i in aminos:
            if i not in amino_acids:
                raise Exception(f"{i} is not a valid instruction")

        self.aminos = aminos
        self.copy_mode = False
        self.binding = aminos_to_binding(aminos)
    
#    def __str__(self):
#        S = str(self.strand) + "\n"
#        S += " "*pos + "^"
#        return S
    
    def evaluate(self,strand,pos):
        
        if type(strand) != STRAND:
            raise Exception("not a valid strand")
        
        if type(pos) != int:
            raise Exception("pos must be an integer")

        snips = []
        for a in self.aminos:
#            print(self)
#            print()
            # Set copy mode
            if a == "cop":
                self.copy_mode = True
                strand.copy(pos)
            if a == "off":
                self.copy_mode = False
            
            # Delete the base being worked on but NOT its complement if present
            if a == "del":
                self.strand.lower[pos] = " "
                
            if a == "cut":
                strand, R = strand.cut(pos)
                snips.append(R)
            
            # Insert rules
            if a == "ing":
                strand.insert("G",pos+1,self.copy_mode)
                pos += 1
            if a == "int":
                strand.insert("T",pos+1,self.copy_mode)
                pos += 1
            if a == "inc":
                strand.insert("C",pos+1,self.copy_mode)
                pos += 1
            if a == "ina":
                strand.insert("A",pos+1,self.copy_mode)
                pos += 1
            
            # Switch sides
            if a == "swi":
                strand.switch()
                pos = len(strand)-pos-1
                
            # Move one unit left or right
            if a == "mvr":
                pos += 1
                if pos == len(strand):
                    break
                if self.copy_mode:
                    strand.copy(pos)
            
            if a == "mvl":
                pos -= 1
                if pos == -1:
                    break
                if self.copy_mode:
                    strand.copy(pos)
            
            # Scan to find a purine or pyrimidine
            if a == "rpy":
                if strand.lower[pos] in "TC":
                    pos += 1
                    if self.copy_mode:
                        strand.copy(pos)
                while strand.lower[pos] not in "TC":
                    pos += 1
                    if self.copy_mode:
                        strand.copy(pos)
                        
            if a == "rpu":
                if strand.lower[pos] in "AG":
                    pos += 1
                    if self.copy_mode:
                        strand.copy(pos)
                while strand.lower[pos] not in "AG":
                    pos += 1
                    if self.copy_mode:
                        strand.copy(pos)
                        
            if a == "lpy":
                if strand.lower[pos] in "TC":
                    pos -= 1
                    if self.copy_mode:
                        strand.copy(pos)
                while strand.lower[pos] not in "TC":
                    pos -= 1
                    if self.copy_mode:
                        strand.copy(pos)
            if a == "lpu":
                if strand.lower[pos] in "AG":
                    pos -= 1
                    if self.copy_mode:
                        strand.copy(pos)
                while strand.lower[pos] not in "AG":
                    pos -= 1
                    if self.copy_mode:
                        strand.copy(pos)
            
#        print(self)
        out = split_strand(strand)
        # seperate out everything
        for s in snips:
            out += split_strand(s)
        return out





if __name__ == '__main__':
    

    
    gene = STRAND("CAAAGAGAATCCTCTTTGAT")
    E = ENZYME(["rpy","cop","rpu","cut"])
    
    print(f"gene:\n{gene}\n\nenzyme:{E.aminos}")
    
    out = E.evaluate(gene,2)
    print(["".join(o.lower) for o in out])


#    gene = STRAND("TAGATCCAGTCCATCGA")
#    E = ENZYME(["rpu","inc","cop","mvr","mvl","swi","lpu","int"])
#    out = E.evaluate(gene,8)
#    for i in out:
#        print(i)