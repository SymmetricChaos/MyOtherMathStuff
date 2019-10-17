# The Condorcet criterion requires that a voting method choose the candidate
# that would win most head-to-head elections against other candidates. It only
# works for ranked voting methods. Its not guaranteed that a Condorcet winner
# exists and practical methods must deal with this.

from collections import Counter

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

    l = len(candidates)
    
    hth_winners = []
    
    for i in range(l):
        
        for j in range(i+1,l):
            
            c1 = candidates[i]
            c2 = candidates[j]
            
            wins = 0
            losses = 0
            
            for v in voters:
                if v.ranking[c1] > v.ranking[c2]:
                    wins += 1
                else:
                    losses += 1
                    
            if wins > losses:
                print(f"{c1:<5}  beats  {c2:<5}  {wins:>2} to {losses}")
                hth_winners.append(c1)
            if wins < losses:
                print(f"{c2:<5}  beats  {c1:<5}  {losses:>2} to {wins}")
                hth_winners.append(c2)
            if wins == losses:
                print(f"{c1:<5}  ties  {c2:<5}")
                
    C = Counter(hth_winners)
    print("\n\n",C.most_common())



if __name__ == '__main__':
    import random
    
    candidates = ["Alice","Bob","Carol","Dave","Eve"]
    
    V = []
    for i in range(30):
    
        ranks = [random.randint(0,5) for i in range(len(candidates))]
        
        V.append( Preferences(candidates,ranks) )
        
#    for i in V:
#        print(i)
        
    compare_candidates(V,candidates)