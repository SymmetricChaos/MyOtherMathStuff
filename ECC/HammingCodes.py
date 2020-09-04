from functools import reduce
import operator as op

def parity(D):
    return reduce(op.xor,D)


def hamming_err_pos(D):
    return reduce(op.xor,[i for i, bit in enumerate(D) if bit])


def check_hamming(D):
    """
    Correct a single if found
    Raise an exception of multiple errors exist
    Do nothing if the block is correct
    """
    p = parity(D)
    e = hamming_err_pos(D)
    if e:
        if p:
            D[e] = op.xor(D[e],1)
        else:
            raise Exception("Multiple Errors Detected")


def make_hamming_block(D,n):
    B = [0]
    t = iter(D)
    for i in range(n):
        B.append(0)
        for p in range(2**i-1):
            B.append(next(t))
    
    
    
    return B


# P H H D
# H D D D
# H D D D
# D D D D

#    0
#  011
#  001
# 1110

if __name__ == '__main__':
    
    # data = [0,0,1,1,0,0,1,1,1,1,0]
    
    # D = make_hamming_block(data,4)
    
    D = [0,0,1,0,1,0,1,1,1,0,0,1,1,1,1,0]
    print(D)
    check_hamming(D)
    print(D)