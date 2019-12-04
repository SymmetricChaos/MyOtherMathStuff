class Surreal:
    
    def __init__(self,L=[],R=[]):
        self.L = L
        self.R = R
    
    def __str__(self):
        S = "{ " + f"{self.L} | {self.R}" + " }"
        S = S.replace("[","")
        S = S.replace("]","")
        return S
    
if __name__ == '__main__':
    print(Surreal([1,2,3],[1]))