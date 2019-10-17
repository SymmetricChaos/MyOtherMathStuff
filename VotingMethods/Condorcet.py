# The Condorcet criterion requires that a voting method choose the candidate
# that would win most head-to-head elections against other candidates. It only
# works for ranked voting methods. Its not guaranteed that a Condorcet winner
# exists and practical methods must deal with this.

from numpy import matrix

class Preferences:
    
    def __init__(self,candidates,ranks):
        self.ranking = dict()
        for c,r in zip(candidates,ranks):
            self.ranking[str(c)] = r
        self.longest_name = max( [len(i) for i in candidates] )


    def __str__(self):
        out = ""
        for p in self.ranking.items():
            out += f"{p[0]:{self.longest_name}}   {p[1]}\n"
        return out


    def __repr__(self):
        return str(self.D)


def compare_candidates(voters,candidates):
    out = dict()
    l = len(candidates)
    for i in range(l):
        for j in range(i+1,l):
            wins = 0
            losses = 0
            for v in voters:
                if v.ranking[candidates[i]] > v.ranking[candidates[j]]:
                    wins += 1
                else:
                    losses += 1
            if wins > losses:
                print(candidates[i],"beats",candidates[j])
            if wins < losses:
                print(candidates[j],"beats",candidates[i])
            if wins == losses:
                print(candidates[i],"ties",candidates[j])
                

    
    return out





if __name__ == '__main__':
    import random
    
    candidates = ["Alice","Bob","Carol","Dave","Eve"]
    
    V = []
    for i in range(5):
    
        ranks = [random.randint(0,5) for i in range(len(candidates))]
        
        V.append( Preferences(candidates,ranks) )
        
    for i in V:
        print(i)
    compare_candidates(V,candidates)