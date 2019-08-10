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
    
    def copy(self):
        return Bitstring(self.bits[:])