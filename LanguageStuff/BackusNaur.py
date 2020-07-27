class BNF_name:
    
    def __init__(self,*args):
        
        if len(args) == 3:
            for i,j in zip(args,[BNF_personal,str,BNF_suffix]):
                if type(i) != j:
                    raise Exception("Not a valid name")
            self.S = f"{args[0]} {args[1]} {args[2]}\n"
        
        elif len(args) == 2:
            for i,j in zip(args,[BNF_personal,BNF_name]):
                if type(i) != j:
                    raise Exception("Not a valid name")
            self.S = f"{args[0]} {args[1]}\n"
        
        else:
            raise Exception("Not a valid name")
            
    def __str__(self):
        return self.S

class BNF_personal:
    
    def __init__(self,*args):
        
        if len(args) == 1:
            if type(args[0]) == BNF_initial:
                self.S = f"{args[0]}."
            elif type(args[0]) == str:
                self.S = f"{args[0]}"
            else:
                raise Exception("Not a valid personal name")
        else:
            raise Exception("Not a valid personal name")
            
    def __str__(self):
        return self.S



class BNF_initial:
    
    def __init__(self,*args):
        if len(args) == 1:
            if args[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                self.S = f"{args[0]}"
            else:
                raise Exception("Not a valid initial")
        else:
            raise Exception("Not a valid initial")
            
        
    def __str__(self):
        return self.S

class BNF_suffix:
    
    def __init__(self,*args):
        if len(args) == 1:
            if args[0] in ("Sr.","Jr.",""):
                self.S = f"{args[0]}"
            else:
                raise Exception("Not a valid suffix")
        else:
            raise Exception("Not a valid suffix")
            
        
    def __str__(self):
        return self.S

suffix = BNF_suffix("")
personal = BNF_personal("George")
initial = BNF_personal(BNF_initial("R"))
last = "Martin"
print(BNF_name(personal,BNF_name(initial,BNF_name(initial,last,suffix))))