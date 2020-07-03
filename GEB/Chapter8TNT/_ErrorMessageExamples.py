from Rules import specify, successor, predecessor, generalize, existence, \
                  transitivity, symmetry, interchange_AE, interchange_EA
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
       
S1 = "∀b:∀a:~Sa=b"
_show_err_message(specify,S1,"a","b=b")
_show_err_message(specify,S1,"a","b")
_show_err_message(specify,S1,"0","a")


print("\n") 
S2 = "∀a:~Sa=b"
_show_err_message(generalize,S2,"a")
_show_err_message(generalize,S2,"c")


print("\n") 
S3 = "~∃b:∀a:~Sa=b"
_show_err_message(interchange_EA,S3,'a',1)
_show_err_message(interchange_AE,S3,'b',1)
_show_err_message(interchange_AE,S3,'a',2)


print("\n") 
S4a = "~Sa=b"
S4b = "Sa=b"
_show_err_message(successor,S4a)
_show_err_message(predecessor,S4b)


print("\n") 
S5 = "∀c':Sa=(b+c')"
_show_err_message(existence,S5,"Sb","d")
_show_err_message(existence,S5,"Sa=b","c")
_show_err_message(existence,S5,"b","SS0")
_show_err_message(existence,S5,"(b+c')","c'")


print("\n") 
S6 = "∀a:Sa=a"
_show_err_message(symmetry,S6)
