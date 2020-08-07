from RewriteRule import random_system_example, CFG, SRS
from random import choices


def random_palindrome():
    rules = [("S","aSa"),
             ("S","bSb"),
             ("S","a"),
             ("S","b"),
             ("S","")]
    
    sys = CFG(rules,"ab","S")
    print(sys)
    print()
    random_system_example("S",sys)



def random_nesting():
    rules = [("S","SS"),
             ("S","()"),
             ("S","(S)"),
             ("S","[]"),
             ("S","[S]"),
             ("S","{}"),
             ("S","{S}")]
    
    sys = CFG(rules,"()[]{}","S")
    print(sys)
    print()
    random_system_example("SSS",sys)


def random_distinct():
    rules = [("S","T"),
             ("S","U"),
             ("T","VaT"),
             ("T","VaV"),
             ("T","TaV"),
             ("U","VbU"),
             ("U","VbV"),
             ("U","UbV"),
             ("V","aVbV"),
             ("V","bVaV"),
             ("V","")]
    
    sys = CFG(rules,"ab","STUV")
    print(sys.compact_rules())
    print()
    random_system_example("S",sys,lim=20)


def random_AB_game_1(k=15):
    
    S = choices("AB",k=k)
    S = "".join(S)
    
    rules = [("AB","A"),
             ("BA","A"),
             ("AA","B"),
             ("BB","B")]
    
    sys = SRS(rules,"AB")
    print(sys.rules)
    print()
    random_system_example(S,sys)


def random_AB_game_2(k=15):
    
    S = choices("AB",k=k)
    S = "".join(S)
    
    rules = [("AB","BBBA"),
             ("BA","A"),
             ("AA","BBBB"),
             ("BB","B")]
    
    sys = SRS(rules,"AB")
    print(sys)
    print()
    random_system_example(S,sys)


# Context sensitive grammar
def random_CSG():
    rules = [("S","aBC"),
             ("S","aSBC"),
             ("CB","CZ"),
             ("CZ","WZ"),
             ("WZ","WC"),
             ("WC","BC"),
             ("aB","ab"),
             ("bB","bb"),
             ("bC","bc"),
             ("cC","cc")]
    
    sys = SRS(rules,"abcSBCWZ")
    string = sys.apply_ordered("aaaBCBCBC")
    print(sys)
    print()
    print(string)
    for i in range(17):
        string = sys.apply_ordered(string)
        print(string)





if __name__ == '__main__':
    
    random_palindrome()
    print()
    random_nesting()
    print()
    random_distinct()
    print()
    random_AB_game_1(10)
    print()
    random_AB_game_2(10)
    print()
    random_CSG()