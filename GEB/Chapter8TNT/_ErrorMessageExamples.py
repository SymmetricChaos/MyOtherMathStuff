from Rules import specify, successor, predecessor, generalize, existence, \
                  transitivity, symmetry, interchange_AE, interchange_EA, \
                  SUCC, MUL, EQ, EXISTS, NOT
from Deduction import PeanoAxioms

def _show_err_message(func,*args):
    try:
        func(*args)
    except Exception as e:
        print(e)
        return 0
    print("NO ERROR OCCURED")
    

#for i in PeanoAxioms:
#    print(i)
       
S1 = "∀a:~Sa=0"
_show_err_message(specify,S1,"a","b=b")
_show_err_message(specify,S1,"b","a")
_show_err_message(specify,S1,"0","a")

print("\n") 
S2 = "∀a:~Sa=b"
_show_err_message(generalize,S2,"a")
_show_err_message(generalize,S2,"c")

print("\n") 
S3 = "~∃b:∀a:~Sa=b"
_show_err_message(interchange_EA,S3,'a',1)
_show_err_message(interchange_AE,S3,'b',1)