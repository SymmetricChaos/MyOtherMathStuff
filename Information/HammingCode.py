from BitstringType import Bitstring, text_to_bitstring, bitstring_to_text
import numpy as np


code_mat  = np.matrix([[1,1,0,1],
                       [1,0,1,1],
                       [1,0,0,0],
                       [0,1,1,1],
                       [0,1,0,0],
                       [0,0,1,0],
                       [0,0,0,1]])

decode_mat  = np.matrix([[0,0,1,0,0,0,0],
                         [0,0,0,0,1,0,0],
                         [0,0,0,0,0,1,0],
                         [0,0,0,0,0,0,1]])

check_mat = np.matrix([[1,0,1,0,1,0,1],
                       [0,1,1,0,0,1,1],
                       [0,0,0,1,1,1,1]])




def encode_with_mat(B):
    return code_mat.dot(B)%2

def decode_with_mat(B):
    return decode_mat.dot(B)%2

def check_with_mat(B):
    return check_mat.dot(B)%2


def hamming_encode(B):
    assert type(B) == Bitstring
    out = Bitstring("")
    chunks = [B.bits[i * 4:(i + 1) * 4] for i in range((len(B.bits) + 5) // 4 )]
    for i in chunks:
        if len(i) == 4:
            out += Bitstring(encode_with_mat(i))
            
    return out

def hamming_decode(B):
    assert type(B) == Bitstring
    out = Bitstring("")
    chunks = [B.bits[i * 7:(i + 1) * 7] for i in range((len(B.bits) + 8) // 7 )]
    for i in chunks:
        if len(i) == 7:
            C = check_with_mat(i)
            if str(C) != "[[0 0 0]]":
                print("ERROR",i,C)
            out += Bitstring(decode_with_mat(i))
            
    return out


b = text_to_bitstring("Thefoxes")
print(b)
print()
ecc = hamming_encode(b)
print(ecc)
ecc[10] = (ecc[10]+1)%2
print()
dec = hamming_decode(ecc)
print(dec)