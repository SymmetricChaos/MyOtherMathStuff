from random import uniform, choices
import re

r = re.compile("[^01]+")
a = "[[0 1 1 0 0 1 1]]"
print()

class Bitstring:
    
    def __init__(self,bits=""):
        
        # Coerce input to string then strip everything except 0s and 1s
        # This lets us ingest strings, lists, and even numpy objects
        S = re.sub("[^01]+","",str(bits))
        
        self.bits = [int(i) for i in S]

    def __str__(self):
        out = ""
        for i in self.bits:
            out += str(i)
        return out
    
    def __add__(self,other):
        return Bitstring(self.bits+other.bits)
    
    def __int__(self):
        return int(str(self), 2)
    
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
    B = choices(["0","1"],k=n)
    return Bitstring("".join(B))

def text_to_bitstring(s):
    out = ""
    for let in s:
        out += bin(ord(let))[2:]
    return Bitstring(out)

def bitstring_to_text(B):
    a = [B.bits[i * 7:(i + 1) * 7] for i in range((len(B.bits) + 8) // 7 )]
    a = a[:-1]
    out = ""
    for let in a:
        bs = Bitstring("".join([str(i) for i in let]))
        out += chr(int(bs))
    return out