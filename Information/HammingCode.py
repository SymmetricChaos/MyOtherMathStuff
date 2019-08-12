from BitstringType import Bitstring, text_to_bitstring, bitstring_to_text
import numpy as np


code_mat  = np.matrix([[1,1,0,1],
                       [1,0,1,1],
                       [1,0,0,0],
                       [0,1,1,1],
                       [0,1,0,0],
                       [0,0,1,0],
                       [0,0,0,1]])

check_mat = np.matrix([[1,0,1,0,1,0,1],
                       [0,1,1,0,0,1,1],
                       [0,0,0,1,1,1,1]])




def encode_with_mat(B):
    return code_mat.dot(B)%2

def hamming_encode(B):
    assert type(B) == Bitstring
    out = Bitstring("")
    chunks = [B.bits[i * 4:(i + 1) * 4] for i in range((len(B.bits) + 5) // 4 )]
    for i in chunks:
        if len(i) == 4:
            print(encode_with_mat(i))
            out += Bitstring(encode_with_mat(i))
            
    return out
#
##def hamming_decode(B):
#
#
#
b = text_to_bitstring("Thefoxes")
print(b)
ecc = hamming_encode(b)
print(ecc)