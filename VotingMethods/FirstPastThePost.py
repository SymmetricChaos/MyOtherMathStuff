from collections import Counter

def FPTP(votes):
    C = Counter(votes)
    s = C.most_common()[0]
    print(f"The Winner is {s[0]} with {s[1]} votes")
    return C
    
FPTP(["Alice","Bob","Alice","Carol","Bob","Bob","Alice","Bob"])

