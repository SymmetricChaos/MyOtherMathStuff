from RewriteRule import rewrite_rule, random_system_example, CFG, SRS
from random import choices


def random_palindrome():
    rules = [rewrite_rule("S","aSa"),
             rewrite_rule("S","bSb"),
             rewrite_rule("S","a"),
             rewrite_rule("S","b"),
             rewrite_rule("S","")]
    
    sys = CFG(rules,"ab","S")
    print(sys)
    print()
    random_system_example("S",sys)


def random_nesting():
    rules = [rewrite_rule("S","SS"),
             rewrite_rule("S","()"),
             rewrite_rule("S","(S)"),
             rewrite_rule("S","[]"),
             rewrite_rule("S","[S]"),
             rewrite_rule("S","{}"),
             rewrite_rule("S","{S}")]
    
    sys = CFG(rules,"()[]{}","S")
    print(sys)
    print()
    random_system_example("SSS",sys)


def random_distinct():
    rules = [rewrite_rule("S","T"),
             rewrite_rule("S","U"),
             rewrite_rule("T","VaT"),
             rewrite_rule("T","VaV"),
             rewrite_rule("T","TaV"),
             rewrite_rule("U","VbU"),
             rewrite_rule("U","VbV"),
             rewrite_rule("U","UbV"),
             rewrite_rule("V","aVbV"),
             rewrite_rule("V","bVaV"),
             rewrite_rule("V","")]
    
    sys = CFG(rules,"ab","STUV")
    print(sys.compact_rules())
    print()
    random_system_example("S",sys,lim=20)


def random_AB_game_1(k=15):
    
    S = choices("AB",k=k)
    S = "".join(S)
    
    rules = [rewrite_rule("AB","A"),
             rewrite_rule("BA","A"),
             rewrite_rule("AA","B"),
             rewrite_rule("BB","B")]
    
    sys = SRS(rules,"AB")
    print(sys.rules)
    print()
    random_system_example(S,sys)


def random_AB_game_2(k=15):
    
    S = choices("AB",k=k)
    S = "".join(S)
    
    rules = [rewrite_rule("AB","BBBA"),
             rewrite_rule("BA","A"),
             rewrite_rule("AA","BBBB"),
             rewrite_rule("BB","B")]
    
    sys = SRS(rules,"AB")
    print(sys)
    print()
    random_system_example(S,sys)


# Context sensitive grammar
def random_CSG():
    rules = [rewrite_rule("S","aBC"),
             rewrite_rule("S","aSBC"),
             rewrite_rule("CB","CZ"),
             rewrite_rule("CZ","WZ"),
             rewrite_rule("WZ","WC"),
             rewrite_rule("WC","BC"),
             rewrite_rule("aB","ab"),
             rewrite_rule("bB","bb"),
             rewrite_rule("bC","bc"),
             rewrite_rule("cC","cc")]
    
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