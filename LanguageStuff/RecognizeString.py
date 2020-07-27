import string


# Restricted to less than 3999 because standard conventions only go that far
def recognize_roman_numeral_3999(numeral):
    
    # Atomic roman numerals
    units = ("I","II","III","IV","V","VI","VII","VIII","IX")
    tens  = ("X","X","XXX","XL","L","LX","LXX","LXXX","CX")
    hunds = ("C","CC","CCC","CD","D","DC","DCC","DCCC","CM")
    thous = ("M","MM","MMM")
    all_atoms = units+tens+hunds+thous
    
    # Roman numeral rank
    # Returns 4 if invalid to catch order errors
    def RNR(S):
        Roman = {"units": units,
                 "tens": tens,
                 "hunds": hunds,
                 "thous": thous}
        
        ranks = {"units":0,
                 "tens":1,
                 "hunds":2,
                 "thous":3}
        
        for k,v in Roman.items():
            if S in v:
                return ranks[k]
        return 4
    
    headptr = 0
    tailptr = 0
    cur_rank = 5
    while tailptr <= len(numeral)+1:
        tailptr += 1
        segment = numeral[headptr:tailptr]
        if segment in all_atoms:
            continue
        else:
            prev_num = numeral[headptr:tailptr-1]
            if prev_num in all_atoms:
                new_rank = RNR(prev_num)
                if new_rank >= cur_rank:
                    # Catch out of order substring
                    return False
                else:
                    cur_rank = new_rank
                    headptr = tailptr-1
            else:
                # Catch invalid characters
                return False
    
    # Catch final out of order substring
    if RNR(segment) >= cur_rank:
        return False
        
    return True



# print(recognize_hypen_name("McDermot-West"))
print(recognize_roman_numeral_3999("MIXX"))