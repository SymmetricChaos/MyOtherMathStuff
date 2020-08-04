from RewriteRule import rewrite_rule, XRG, random_system_example

def binary_decimals():
    
    rules = [rewrite_rule("S","1A"),
             rewrite_rule("S","-1A"),
             rewrite_rule("S","0.C"),
             rewrite_rule("S","-0.C"),
             rewrite_rule("A","0B"),
             rewrite_rule("A","1B"),
             rewrite_rule("B","0B"),
             rewrite_rule("B","1B"),
             rewrite_rule("B","C"),
             rewrite_rule("B",".C"),
             rewrite_rule("C","1"),
             rewrite_rule("C","0D"),
             rewrite_rule("C","1D"),
             rewrite_rule("D","0D"),
             rewrite_rule("D","1D"),
             rewrite_rule("D","1")]
    
    grammar = XRG(rules,"-.01","SABCD")
    
    random_system_example("S",grammar)


binary_decimals()