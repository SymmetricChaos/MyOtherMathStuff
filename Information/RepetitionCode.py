from BitstringType import Bitstring, text_to_bitstring, bitstring_to_text

def repetition_encode(B):
    assert type(B) == Bitstring
    out = ""
    for b in B.bits:
        out += str(b)*3
    return Bitstring(out)

def repetition_decode(B):
    assert type(B) == Bitstring
    out = [B.bits[i * 3:(i + 1) * 3] for i in range((len(B.bits) + 2) // 3 )]
    out = ["0" if sum(i) < 2 else "1" for i in out]
    return Bitstring("".join(out))

b = text_to_bitstring("Thefox")
ecc = repetition_encode(b)
ecc.corrupt(.15)
dec = repetition_decode(ecc)
print(b)
print(dec)
print(bitstring_to_text(b))
print(bitstring_to_text(dec))