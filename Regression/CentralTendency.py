#import numpy as np
from Utils.Math import sort_by_nth, prod

def median(L):
    L = sorted(L)
    parity = len(L)%2
    half_range = len(L)//2
    
    if parity == 1:
        return L[half_range]
    else:
        return (L[half_range-1]+L[half_range])/2
    

# Crude weighted median
# Weighted median should be equivalent of having extra entries corresponding to
# the weights
# Should return the lower median on an even set
def weighted_median(L,W):
    LW = [(l,w) for l,w in zip(L,W)]
    LW = sort_by_nth(LW,0)
    
    s = sum(W)
    
    t = 0
    ctr = 0
    while t <= s/2:
        t += LW[ctr][1]
        ctr += 1
    
    return LW[ctr-1][0]
    

def mean(L):
    return sum(L)/len(L)


# Arithmetic mean with quartiles beyond t and 1-t removed
#def truncated_mean(L,t=.05):

    
def weighted_mean(L,W=[]):
    if len(W) == 0:
        W = [1]*len(L)
    T = [l*w for l,w in zip(L,W)]
    return sum(T)/sum(W)


def geometric_mean(L):
    P = prod(L)
    return P**(1/len(L))


#def harmonic_mean(L):





if __name__ == '__main__':
    
    # Make some graphics showing different measures
    
    from Utils.Drawing import make_blank_canvas, draw_dots_xy, connect, draw_circles
    import numpy as np
    
    def simple_mean_example():
        make_blank_canvas([-10,10],box=True)
        plt.title("The Arithmetic Mean is the Point of Balance",size=25)
        
        n = 20
        X = np.random.uniform(-8,8,n//2)
        X = np.append(X,np.random.uniform(-2,8,n//2))
        Y = [0]*n
        
        draw_circles(X,[.2]*n,[.2]*n)
        connect([-8,-.01],[8,-.01],color="black")
        draw_dots_xy([mean(X)],[-.2],color="red",marker="^",s=200)
        
        
    def weighted_mean_example():
        make_blank_canvas([-1,1],box=True)
        plt.title("The Weighted Mean is the Point of Balance",size=25)
        
        n = 20
        X = np.random.uniform(-.8,.8,n//2)
        X = np.append(X,np.random.uniform(-.2,.8,n//2))
        W = np.random.exponential(5,n)+1
        Sz = np.sqrt(W)/85
        
        # Using weight for sizes of dots IS correct, the underlying MLP rules
        # scale the area of the dot not the radius
        C = draw_circles(X,Sz,Sz)
        C.set_alpha(.5)
        connect([-.8,0],[.8,0],color="black")
        draw_dots_xy([weighted_mean(X,W)],[-.035],color="red",marker="^",s=200)
        
    simple_mean_example()
    weighted_mean_example()