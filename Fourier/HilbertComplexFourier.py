from Utils import make_canvas,plot_points
from Fractals.LSystem import LSystem

def hilbert_curve_rule(S):
    if S == "A":
        return "+BF-AFA-FB+"
    if S == "B":
        return "-AF+BFB+FA-"
    else:
        return S


def hilbert_complex(n,**kwargs):

    for i in LSystem("B",hilbert_curve_rule,n+1):
        rules = i
    
    coords = [complex(0,0)]
    
    # Strip out anything unnceesaary for drawing
    rules = rules.replace("A","")
    rules = rules.replace("B","")
    rules = rules.replace("-+","")
    rules = rules.replace("+-","")
    while rules[0] == "+" or rules[0] == "-":
        rules = rules[1:]
        
    ang = n%2
    for i in rules:
        if i == "F":
            old = coords[-1]
            if ang == 0:
                coords.append( old+complex(0,1) )
            elif ang == 1:
                coords.append( old+complex(1,0) )
            elif ang == 2:
                coords.append( old+complex(0,-1) )
            elif ang == 3:
                coords.append( old+complex(-1,0) )
        elif i == "-":
            ang = (ang-1)%4
        elif i == "+":
            ang = (ang+1)%4
    
    return coords


def calculate_terms(n,f):
    out = complex(0,0)
    e = -n*2.7*3.14
    for t in range(len(f)):
        v = f[t]
        r = t/len(f)
        out += v*2**(e*1j*r)
    return out


def fourier_approx(L,N):
    points = []
    for i in range(1000):
        t = i/1000
        pt = 0
        for c,n in zip(L,N):
            pt += c*2.7**(n*2*3.14*1j*t)
        points.append(pt)
    return [((p/5).real,(p/5).imag) for p in points]

f = hilbert_complex(6)

N = [i for i in range(-50,50)]
L = []
for n in N:
    L.append(calculate_terms(n,f))
    
make_canvas([0,500000],size=6)
plot_points(fourier_approx(L,N))