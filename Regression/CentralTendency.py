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


def harmonic_mean(L):
    S = sum([1/l for l in L])
    return len(L)/S





if __name__ == '__main__':
    
    # Make some graphics showing different measures
    
    import Utils.Drawing as draw
    import numpy as np



    def weighted_mean_example():
        canvas, plot = draw.make_blank_canvas([-1,1],box=True)
        draw.title("The Weighted Mean is the Point of Balance",size=25)
        
        n = 20
        X = np.random.uniform(-.8,.8,n//2)
        X = np.append(X,np.random.uniform(.2,.8,n//2))
        W = np.random.exponential(5,n)+1
        # Sized reduced by square root to show weight by area
        Sz = np.sqrt(W)/85
        
        C = draw.draw_circles(X,Sz,Sz)
        C.set_alpha(.5)
        draw.connect([-.8,0],[.8,0],color="black")
        draw.draw_dots_xy([weighted_mean(X,W)],[-.035],color="red",marker="^",s=200)



    def median_mean_example():
        canvas, plot = draw.make_blank_canvas(size=[16,8])
        draw.canvas_title("The Median is the Point of Typicality\nThe Mean is the Point of Balance",size=25,y=1.05)
        
        n = 20
        X = np.random.uniform(-8,8,n//2)
        X = np.append(X,np.random.uniform(5,8,n//2))
        
        draw.make_blank_subplot(1,2,1,[-10,10])
        draw.draw_circles(X,[.2]*n,[.2]*n)
        draw.connect([-8,-.01],[8,-.01],color="black")
        draw.draw_dots_xy([mean(X)],[-.35],color="black",marker="^",s=200)
        draw.draw_dots_xy([median(X)],[-.35],color="lightgray",marker="^",s=200)
        draw.title("Mean",size=25)
        
        draw.make_blank_subplot(1,2,2,[-10,10])        
        draw.draw_circles(X,[.2]*n,[.2]*n)
        draw.connect([-8,-.01],[8,-.01],color="black")
        draw.draw_dots_xy([median(X)],[-.35],color="black",marker="^",s=200)
        draw.draw_dots_xy([mean(X)],[-.35],color="lightgray",marker="^",s=200)
        draw.title("Median",size=25)


 
    def harmonic_mean_example():
        canvas, plot = draw.make_blank_canvas(size=[16,8])
        draw.canvas_title("The Harmonic Mean is Relevant to Rates",size=25,y=1.05)
        
        th = np.linspace(0,2*np.pi,8)
        X = np.sin(th)[:-1]
        Y = np.cos(th)[:-1]
        
        draw.draw_dots_xy(X,Y)
        draw.draw_closed_curve_xy(X,Y,linewidth=.5,color="black")

#    weighted_mean_example()
#    median_mean_example()
    harmonic_mean_example()