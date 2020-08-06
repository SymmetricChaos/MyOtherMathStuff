from RewriteRule import rewrite_rule, XRG, random_system_example


rules = [rewrite_rule("S","1A"),
         rewrite_rule("S","-1A"),
         rewrite_rule("S","-0.B"),
         rewrite_rule("S","0.B"),
         rewrite_rule("S","0"),
         rewrite_rule("A","0A"),
         rewrite_rule("A","1A"),
         rewrite_rule("A",".B"),
         rewrite_rule("A",""),
         rewrite_rule("B","0B"),
         rewrite_rule("B","1B"),
         rewrite_rule("B","1"),]

binarydec = XRG(rules,"-.01","SABCD")

print(binarydec.compact_rules())
print()

random_system_example("S",binarydec)

