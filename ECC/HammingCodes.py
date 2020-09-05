from functools import reduce
from itertools import zip_longest
import operator as op

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


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
    else:
        if p:
            D[0] = op.xor(D[0],1)


def make_hamming_block(D,n):
    
    B = [0]
    t = iter(D)
    
    for i in range(n):
        B.append(0)
        for p in range(2**i-1):
            B.append(next(t))
    
    pbits = [2**i for i in range(n)]
    
    for i in range(2**n):
        for p in pbits:
            if (i//p)%2:
                B[p] ^= B[i]
    
    B[0] = parity(B)
    
    return B


def make_hamming_blocks(D,n):
    
    l = 2**n-(n+1)
    Bs = []
    G = grouper(D,l)
    
    for i in G:
        Bs.append(make_hamming_block(i,n))
    
    return Bs


def extract_hamming_data(D,n):
    
    B = []
    pbits = [2**i for i in range(n)]
    
    for n,i in enumerate(D[1:],1):
        if n in pbits:
            continue
        B.append(i)
    
    return B


def bitstring(D,sep=""):
    return sep.join([str(i) for i in D])





if __name__ == '__main__':
    
    M1 = [0,0,1,1,0,0,0,1,1,1,0]
    
    D = make_hamming_block(M1,4)
    
    D[7] ^= 1
    check_hamming(D)
    
    M2 = extract_hamming_data(D,4)
    
    print(bitstring(M1))
    print(bitstring(M2))
