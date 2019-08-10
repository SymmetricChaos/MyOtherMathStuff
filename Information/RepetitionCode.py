from BitstringType import Bitstring, random_bitstring

def repetition_encode(bits):
    assert type(bits) == Bitstring
    out = Bitstring()
    for b in bits.bits:
        out.bits += [b]*3
    return out

def repetition_decode(B):
    assert type(B) == Bitstring
    out = [B.bits[i * 3:(i + 1) * 3] for i in range((len(B.bits) + 2) // 3 )]
    out = [0 if sum(i) < 2 else 1 for i in out]
    return Bitstring(out)

b = random_bitstring(10)
print(b)
ecc = repetition_encode(b)
ecc.corrupt(.1)
dec = repetition_decode(ecc)
print(dec)
print(b==dec)