from RewriteRule import rewrite_rule, random_system, random_left_system
from random import choices


def random_AB_game_1(k=15):
    
    S = choices("AB",k=k)
    S = "".join(S)
    
    rules = [rewrite_rule("AB","A"),
             rewrite_rule("BA","A"),
             rewrite_rule("AA","B"),
             rewrite_rule("BB","B")]
    
    random_system(S,rules)


def random_AB_game_2(k=15):
    
    S = choices("AB",k=k)
    S = "".join(S)
    
    rules = [rewrite_rule("AB","BBBA"),
             rewrite_rule("BA","A"),
             rewrite_rule("AA","BBBB"),
             rewrite_rule("BB","B")]
    
    random_system(S,rules)


def random_improper():
    rules = [rewrite_rule("S",""),
             rewrite_rule("S","aSa"),
             rewrite_rule("S","bSb"),]
    
    random_system("S",rules)

def random_nesting():
    rules = [rewrite_rule("S","SS"),
             rewrite_rule("S","()"),
             rewrite_rule("S","(S)"),
             rewrite_rule("S","[]"),
             rewrite_rule("S","[S]"),
             rewrite_rule("S","{}"),
             rewrite_rule("S","{S}"),]
    
    random_system("S",rules)


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
             rewrite_rule("V",""),]
    
    random_system("S",rules,lim=20)


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
    
    random_left_system("S",rules)

if __name__ == '__main__':

    
    random_AB_game_1(15)
    print()
    random_AB_game_2(15)
    print()
    random_improper()
    print()
    random_nesting()
    print()
    random_CSG()
    print()
    random_distinct()