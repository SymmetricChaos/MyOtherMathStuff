import matplotlib.pyplot as plt

def mbline(M,B,xlim=[-5,5],**kwargs):
    
    
    for m,b in zip(M,B):
        
        x0 = xlim[0]
        y0 = m*x0+b
        
        x1 = xlim[1]
        y1 = m*x1+b

        plt.plot([x0,x1],[y0,y1],**kwargs)
