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

binarydec = XRG(rules,"-.01","SAB")

print(binarydec.compact_rules())
print()

random_system_example("S",binarydec)

print()

print(binarydec.language(5,"S"))



rules = [("S","1A"),
         ("A","2B"),
         ("A",""),
         ("B","3C"),
         ("B",""),
         ("C","4"),
         ("C",""),]

counter = XRG(rules,"1234","SABC")

for n,i in enumerate(counter.full_language("S")):
    if n > 20:
        break
    print(i)