
def levenshtein(s1,s2):
    i, j = len(s1), len(s2)
    if min(i,j) == 0:
        return max(i,j)
    A = levenshtein(s1[:-1],s2) + 1
    B = levenshtein(s1,s2[:-1]) + 1
    C = levenshtein(s1[:-1],s2[:-1]) + (1 if s1[-1] != s2[-1] else 0)
    return min(A,B,C)

print(levenshtein("kitten","sitting"))
