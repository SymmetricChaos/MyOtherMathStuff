from random import uniform, choices

class Bitstring:
    
    def __init__(self,bits=[]):
        assert type(bits) == list
        for i in bits:
            if i not in [0,1]:
                raise Exception(f"{i} {type(i)} is not a valid bit")
        self.bits = bits

    def __str__(self):
        out = ""
        for i in self.bits:
            out += str(i)
        return out
    
    def __len__(self):
        return len(self.bits)
    
    def __getitem__(self,n):
        return self.bits[n]
    
    def __eq__(self,other):
        return self.bits == other.bits
    
    def copy(self):
        return Bitstring(self.bits[:])
    
    def corrupt(self,p):
        for i in range(len(self)):
            x = uniform(0,1)
            if x < p:
                self.bits[i] = (self.bits[i]+1)%2
                
def random_bitstring(n):
    B = choices([0,1],k=n)
    return Bitstring(B)

#def text_to_bitstyring(s):