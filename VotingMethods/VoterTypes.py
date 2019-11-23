def sort_by_nth(L,n,func=None):
    if func == None:
        f = lambda x: x[n]
        return sorted(L,key=f)
    else:
        f = lambda x: func(x[n])
        return sorted(L,key=f)



def prefs_to_dict(cands,ranks):
    pairs = [(x,y) for x,y in zip(cands,ranks)]
    pairs = sort_by_nth(pairs,1)
    return dict(pairs)



class Voter:
    
    def __init__(self,cands,ranks):
        self.prefs = prefs_to_dict(cands,ranks)


    def __str__(self):
        out = ""
        for c,r in self.prefs.items():
            out += f"{c}: {r}\n"
        out = out[:-1]
        return out


    def rank(self,candidate):
        return self.prefs[candidate]


    def favorite(self):
        return next(iter(self.prefs.keys()))


    def prefers(self,A,B):
        if self.rank(A) > self.rank(B):
            return A
        elif self.rank(A) < self.rank(B):
            return B
        else:
            return None


if __name__ == '__main__':
    V = Voter(["Alice","Bob","Carol","Dave","Eve","Frank"],[1,7,2,3,9,3])
    print(V)
    print("\nFavorite")
    print(V.favorite())
    print("\nRank for Bob")
    print(V.rank("Bob"))
    
    print("\nPreference of Alice vs Eve")
    print(V.prefers("Alice","Eve"))
    print("\nPreference of Frank vs Dave")
    print(V.prefers("Frank","Dave"))