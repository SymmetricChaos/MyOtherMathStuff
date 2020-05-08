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
    
    from Utils.Drawing import make_blank_canvas, draw_dots_xy, connect, \
                              draw_circles, title, make_blank_subplot, \
                              canvas_title
    import numpy as np



    def weighted_mean_example():
        canvas, plot = make_blank_canvas([-1,1],box=True)
        title("The Weighted Mean is the Point of Balance",size=25)
        
        n = 20
        X = np.random.uniform(-.8,.8,n//2)
        X = np.append(X,np.random.uniform(.2,.8,n//2))
        W = np.random.exponential(5,n)+1
        # Sized reduced by square root to show weight by area
        Sz = np.sqrt(W)/85
        
        C = draw_circles(X,Sz,Sz)
        C.set_alpha(.5)
        connect([-.8,0],[.8,0],color="black")
        draw_dots_xy([weighted_mean(X,W)],[-.035],color="red",marker="^",s=200)
    


    def median_mean_example():
        canvas, plot = make_blank_canvas(size=[16,8])
        canvas_title("The Median is the Point of Typicality\nThe Mean is the Point of Balance",size=25,y=1.05)
        
        n = 20
        X = np.random.uniform(-8,8,n//2)
        X = np.append(X,np.random.uniform(5,8,n//2))
        
        make_blank_subplot(1,2,1,[-10,10])
        draw_circles(X,[.2]*n,[.2]*n)
        connect([-8,-.01],[8,-.01],color="black")
        draw_dots_xy([mean(X)],[-.35],color="black",marker="^",s=200)
        draw_dots_xy([median(X)],[-.35],color="lightgray",marker="^",s=200)
        title("Mean",size=25)
        
        make_blank_subplot(1,2,2,[-10,10])        
        draw_circles(X,[.2]*n,[.2]*n)
        connect([-8,-.01],[8,-.01],color="black")
        draw_dots_xy([median(X)],[-.35],color="black",marker="^",s=200)
        draw_dots_xy([mean(X)],[-.35],color="lightgray",marker="^",s=200)
        title("Median",size=25)

    weighted_mean_example()
    median_mean_example()