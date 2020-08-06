from RewriteRule import XRG, random_system_example


rules = [("S","1A"),
         ("S","-1A"),
         ("S","-0.B"),
         ("S","0.B"),
         ("S","0"),
         ("A","0A"),
         ("A","1A"),
         ("A",".B"),
         ("A",""),
         ("B","0B"),
         ("B","1B"),
         ("B","1"),]

binarydec = XRG(rules,"-.01","SABCD")

print(binarydec.compact_rules())
print()

random_system_example("S",binarydec)

