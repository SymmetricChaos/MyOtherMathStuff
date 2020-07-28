from RewriteRule import rewrite_rule, random_system, random_left_system

def decimal_string():
    
    rules = [rewrite_rule("S","-A"),
             rewrite_rule("S","A"),
             rewrite_rule("A","0B"),
             rewrite_rule("A","1B"),
             rewrite_rule("B","0B"),
             rewrite_rule("B","1B"),
             rewrite_rule("B","C"),
             rewrite_rule("B",".C"),
             rewrite_rule("C","0D"),
             rewrite_rule("C","1D"),
             rewrite_rule("D","0D"),
             rewrite_rule("D","1D"),
             rewrite_rule("D",""),]
    
    random_system("S",rules)


decimal_string()