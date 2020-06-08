# Valid BlooP programs:
# A function with a finite number of inputs
# They can contain the following symbols and term
#    if, return, break, =, ==, +, <
# They can also contain any other valid BlooP program
# There must always be a value returned and it must always be an integer
# Parentheses and colons are allowed for Python's formatting
# + can be used for arithmetic addition
# < can be used for arithmetic less-than
# * can be used for arithmetic multiplication
# Numeric constants are allowed
# The only variables allow are integers assigned to and taken from the Cell dictionary
# The Cell dictionary must be indexed by integers
# A for loop is allowed but its can only loop over either an input or over an
# element of cell, the iteration variable must be discarded

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
    
    for _ in range(M):
        if cell[0]+N == M:
            return cell[0]
        
        cell[0] = cell[0]+1


def POWER(M,N):
    cell = Cell()
    
    cell[0] = 1
    
    for _ in range(N):
        cell[0] = M*cell[0]
    
    return cell[0]


def TWO_TO_THE_THREE_TO_THE(N):
    cell = Cell()
    
    cell[0] = POWER( 2, POWER(3,N) )
    return cell[0]


def DIVIDE(M,N):
    cell = Cell()
    
    if M < N:
        return cell[0]
    
    if N == 0:
        return cell[0]

    cell[0] = M
    cell[1] = 1
    
    for _ in range(M):
        cell[0] = MINUS(cell[0],N)
        
        if cell[0] < N:
            return cell[1]
        
        cell[1] = 1+cell[1]


def REMAINDER(M,N):
    cell = Cell()
    
    if M < N:
        return cell[0]
    
    if N == 0:
        return cell[0]

    cell[0] = M
    cell[1] = 1
    
    for _ in range(M):
        cell[0] = MINUS(cell[0],N)
        
        if cell[0] < N:
            return cell[0]


def PRIME(N):
    cell = Cell()
    
    if N < 2:
        return 0
    
    cell[0] = 1
    for _ in range(MINUS(N,2)):
        cell[0] = 1+cell[0]
        
        if REMAINDER(N,cell[0]) == 0:
            return 0
        
    return 1


def FACTORIAL(N):
    cell = Cell()
    
    cell[0] = 1
    cell[1] = 1
    
    for _ in range(N):
        cell[0] = cell[0] * cell[1]
        cell[1] = 1+cell[1]
    
    return cell[0]


def FIBONACCI(N):
    cell = Cell()
    
    cell[0] = 0
    cell[1] = 1
    cell[2] = 1
    
    if N == 0:
        return 0
    
    if N < 2:
        return 1
    
    for _ in range(N):
        cell[0] = cell[1]
        cell[1] = cell[2]
        cell[2] = cell[0]+cell[1]
    
    return cell[2]


def GOLDBACH(N):
    cell = Cell()
    
    for _ in range(N):
        cell[0] = 1+cell[0]
        if PRIME(cell[0]) == 1:
            if PRIME( MINUS( N, cell[0] ) ):
                return 1
    return 0


def PYTHAGOREAN(A,B,C):
    cell = Cell()
    
    cell[0] = A*A+B*B
    cell[1] = C*C
    
    if cell[0] == cell[1]:
        return 1
    
    return 0


if __name__ == '__main__':
    
    print(f"MINUS(56,9) = {MINUS(56,9)}")
    print(f"POWER(7,7) = {POWER(7,7)}")
    print(f"TWO_TO_THE_THREE_TO_THE(3) = {TWO_TO_THE_THREE_TO_THE(3)}")
    print(f"DIVIDE(71,8) = {DIVIDE(71,8)}")
    print(f"REMAINDER(71,8) = {REMAINDER(71,8)}")
    print(f"PRIME(131) = {PRIME(131)}")
    print(f"FACTORIAL(9) = {FACTORIAL(9)}")
    print(f"FIBONACCI(16) = {FIBONACCI(16)}")
    print(f"GOLDBACH(76) = {GOLDBACH(76)}")
