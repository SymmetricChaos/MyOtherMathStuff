# Valid FlooP programs:
# A function with a finite number of inputs
# They can contain the following symbols and terms
#    if, return, break, =, ==, +, <
# They can also contain any other valid FlooP program
# There must always be a value returned and it must always be an integer
# Parentheses and colons are allowed for Python's formatting
# + can be used for arithmetic addition
# < can be used for arithmetic less-than
# * can be used for arithmetic multiplication
# Numeric constants are allowed
# The only variables allow are integers assigned to and taken from the Cell dictionary
# The Cell dictionary must be indexed by integers
# A while loop is allowed of the form 'while True:'


# Create an "infinite list of zeroes" to work with

from collections import defaultdict

def zero():
    return 0

class Cell:

    def __init__(self):
        self.CELLS = defaultdict(zero)
        
    def __getitem__(self,n):
        return self.CELLS[n]
    
    def __setitem__(self,n,val):
        if not type(n) == int:
            raise Exception("Cell can be indexed only by integers")
        if not type(val) == int:
            raise Exception("Cell can contain only integers")
        self.CELLS[n] = val





def MINUS(M,N):
    cell = Cell()
    
    if M < N:
        return cell[0]
    
    while True:
        if cell[0]+N == M:
            return cell[0]
        
        cell[0] = cell[0]+1
        




if __name__ == '__main__':
    
    print(f"MINUS(56,27) = {MINUS(56,27)}")
