from collections import Counter

def FPTP(votes):
    C = Counter(votes)
    for candidate in C.items():
        print(candidate)
    
FPTP(["Alice","Bob","Alice","Carol","Bob","Bob","Alice","Bob"])

