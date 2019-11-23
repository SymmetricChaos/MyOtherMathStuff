from collections import Counter
import numpy as np

def FPTP(votes):
    C = Counter(votes)
    s = C.most_common()[0]
    if C.most_common()[0][1] == C.most_common()[1][1]:
        print("THERE HAS BEEN A TIE")
    print(f"The Winner is {s[0]} with {s[1]} votes")
    return C


candidate = ["Alice","Bob","Carol","Dave"]
votes = np.random.choice(candidate,20)

FPTP(votes)

