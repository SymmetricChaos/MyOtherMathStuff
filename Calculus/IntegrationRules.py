## The rectangular rule
def rect_rule(func,a,b,s):
    out = 0
    while a < b:
        out += s*func((2*a+s)/2)
        a += s
    return out

## The trapezoidal rule
def trap_rule(func,a,b,s):
    out = 0
    while a < b:
        out += s*(func(a)+func(a+s))/2
        a += s
    return out

