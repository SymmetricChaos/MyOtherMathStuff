import string



def recognize_letter(letter):
    if letter in string.ascii_letters:
        return True
    return False


def recognize_upper_case(letter):
    if letter in string.ascii_uppercase:
        return True
    return False


def recognize_lower_case(letter):
    if letter in string.ascii_lowercase:
        return True
    return False


def recognize_digit(digit):
    if digit in string.digits:
        return True
    return False


def recognize_number(digits):
    for d in digits:
        if not recognize_digit(d):
            return False
    return True


def recognize_simple_name(name):
    if recognize_upper_case(name[0]):
        for letter in name[1:]:
            if not recognize_letter(letter):
                return False
        return True
    return False


def recognize_hypen_name(name):
    parts = name.split("-")
    for part in parts:
        if not recognize_simple_name(part):
            return False
        return True

# Restricted to less than 3999
def recognize_roman_numbeal_3999(numeral):
    
    # Most basic check
    for n in numeral:
        if n not in "IVXLCM":
            return False
    
    # Atomic roman numerals
    units = ("I","II","III","IV","V","VI","VII","VIII","IX")
    tens  = ("X","X","XXX","XL","L","LX","LXX","LXXX","CX")
    hunds = ("C","CC","CCC","CD","D","DC","DCC","DCCC","CM")
    thous = ("M","MM","MMM")
    all_atoms = units+tens+hunds+thous
    
    Roman = {"units": units,
             "tens": tens,
             "hunds": hunds,
             "thous": thous}
    
    ranks = {"units":0,
             "tens":1,
             "hunds":2,
             "thous":3}
    
    left = ""
    right = numeral
    ctr = 4
    while len(right) > 0:
        # print(left,right)
        left += right[0]
        right = right[1:]
        if left in all_atoms:
            continue
        else:
            if left[:-1] in all_atoms:
                for ranking in ("units","tens","hunds","thous"):
                    if left[:-1] in Roman[ranking]:
                        if ranks[ranking] >= ctr:
                            return False
                        ctr = ranks[ranking]
                right = left[-1]+right
                left = ""
            else:
                return False
    return True

# print(recognize_hypen_name("McDermot-West"))
print(recognize_roman_numbeal_3999("MXICCCCMIIV"))