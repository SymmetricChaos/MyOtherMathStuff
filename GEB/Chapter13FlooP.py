# Valid FlooP programs:
# A function with a finite number of inputs
# They can contain the following symbols and terms
#    if, return, break, =, ==, +, <
# They can also contain any other valid FlooP or BlooP program
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
from Utils.StringManip import innermost, left_string
import time

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
    
    def __str__(self):
        s = ""
        for k,v in self.CELLS.items():
            s += f"{k}: {v}\n"
        return s


def FACTORIAL(N):
    cell = Cell()

    cell[0] = 1
    cell[1] = 1
    
    while True:
        if N < cell[0]:
            return cell[1]
        
        cell[1] = cell[0]*cell[1] # <- performs the operation at a given level of "recusion"
        cell[0] = 1+cell[0]       # <- essentially tracking the level of "recusion"
        

from Chapter13BlooP import MINUS,POWER,DIVIDE,REMAINDER,ROOT

        





# The Ackerman function is general recursive but not primitive recursive so
# there must be a FlooP program for it but not a BlooP program
# Its not obvious what that is so lets investigate

def A(M,N):
    if M == 0:
        return N+1
    if N == 0:
        return A(M-1,1)
    return A(M-1,A(M,N-1))

# We can Godel number each input to the Ackerman function as 2**M * 3**N
def ack_g_code(M,N):
    return 2**M*3**N

def ack_g_code_rev(G):
    M,N = 0,0
    while G%2 == 0:
        M += 1
        G //= 2
    while G%3 == 0:
        N += 1
        G //= 3
    return M,N

def A_coded(M,N):
    print(f"A({M},{N}) → cell[{ack_g_code(M,N)}]")
    if M == 0:
        return N+1
    
    if N == 0:
        return A_coded(M-1,1)
    
    return A_coded(M-1,A_coded(M,N-1))

def A_expand(M,N):
    if M == 0:
        return f"{N+1}"
    if N == 0:
        return f"A({M-1},1)"
    return f"A({M-1},A({M},{N-1}))"

def A_expand_recur(M,N):
    S = f"A({M},{N})"
    print(S)
    while "A" in S:
        bottom,_,_ = innermost(S,"A",")")[0]
        m = int(left_string(bottom,"(",",",inner=True)[0])
        n = int(left_string(bottom,",",")",inner=True)[0])
        bottom_ex = A_expand(m,n)
        S = S.replace(bottom,bottom_ex)
        print(S)


# Start with creating the simplest loop when N = 0
def M_loop(M):
    return ack_g_code(M-1,1)

def MN_loop(M,N):
    return ack_g_code(M,N-1)
        

def A_loop(M,N):

    aux = []
    while True:
#        print("\nstate",M,N)
        if M == 0 and aux == []:
            print(M,N,aux)
            return N+1
        elif M == 0 and aux != []:
#            print("Nloop",M,N)
            print(M,N,aux)
            N += 1
            M = aux.pop()
        elif N == 0:
            goto = M_loop(M)
            M,N = ack_g_code_rev(goto)
#            print("Mloop",M,N)
            print(M,N,aux)
        else:
            aux.append(M-1)
            goto = MN_loop(M,N)
            M,N = ack_g_code_rev(goto)
#            print("MNloop",M,N)
            print(M,N,aux)

    
        
def TWO_THREE_CODE(M,N):
    return POWER(2,M)*POWER(3,N)

#def GCODE_M(G):
#    DIVIDE,REMAINDER

#def ACKERMAN(M,N):
#    cell = Cell()
#    
#    cell[0] = M
#    cell[1] = N
#    cell[2] = 3 # Stack counter
#
#    while True:
#        if cell[2] == 0:
#            if cell[0] == 1:
#                return cell[1]+1
#        
#        if cell[0] == 0 and 1 < cell[2]
#            cell[1] = 1+cell[1]
#            M = cell[cell[2]]
#            cell[2] = MINUS(cell[2],1)
#            
#        elif cell[1] == 0:
#            goto = TWO_THREE_CODE(MINUS(cell[0],1),1)
#            cell[0]
#            cell[1]
#            M,N = ack_g_code_rev(goto)
#
#        else:
#            aux.append(M-1)
#            goto = MN_loop(M,N)
#            M,N = ack_g_code_rev(goto)




if __name__ == '__main__':
    
#    print(f"MINUS(56,27) = {MINUS(56,27)}")
#    print(FACTORIAL(5))
#    print(POWER(3,4))
#    A(2,4)
    M,N = 3,2
#    A_expand_recur(M,N)
    print()
#    A_coded(M,N)
    print(A_loop(3,1))