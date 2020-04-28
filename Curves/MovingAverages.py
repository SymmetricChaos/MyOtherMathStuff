import numpy as np
from Drawing import make_blank_canvas, make_blank_subplot
from WeightFunctions import triangular_weights, exponential_weights

# Moving averages for equally spaced data like time-series


def simple_moving_average(Y,radius=1):
    # Number of values considered at each step
    N = 2*radius+1
    
    # Padded version of Y
    y = Y[:]
    y = [y[0]]*radius + y + [y[-1]]*radius

    m_av = []
    for i in range(len(Y)):
        m_av.append(sum(y[i:N+i])/N)
    
    return m_av


def weighted_mean(X,W):
    s = sum([x*w for x,w in zip(X,W)])
    n = sum(W)
    return s/n
        
    
def weighted_moving_average(Y,radius=1,weights=[]):
    # Number of values considered at each step
    N = (2*radius)+1
    
    # Padded version of Y
    y = Y[:]
    y = [y[0]]*radius + y + [y[-1]]*radius
    
    if not weights:
        weights = triangular_weights(np.linspace(-1,1,N))
    elif len(weights) != N:
        raise Exception("Invalid weights")
        
    
    m_av = []
    for i in range(len(Y)):
        m_av.append(weighted_mean(y[i:N+i],weights))
    
    return m_av


def simple_moving_median(Y,radius=1):
    # Number of values considered at each step
    N = 2*radius+1
    
    # Padded version of Y
    y = Y[:]
    y = [y[0]]*radius + y + [y[-1]]*radius

    m_av = []
    for i in range(len(Y)):
        m_av.append(np.median(y[i:N+i]))
    
    return m_av





if __name__ == '__main__':
    
    import matplotlib.pyplot as plt
    
    x1 = np.linspace(2,7,200)
    y1 = list(np.cos(x1)+np.random.normal(0,.3,200))
    
    w = exponential_weights(np.linspace(-1,1,15))

    radius = 7
    av1 = simple_moving_average(y1,radius)
    av2 = simple_moving_median(y1,radius)
    av3 = weighted_moving_average(y1,radius)
    av4 = weighted_moving_average(y1,radius,w)
    
    make_blank_canvas(size=(16,16))
    
    for vals,title,ctr in zip([av1,av2,av3,av4],
                          [f"Simple Moving Average (radius {radius})",
                           f"Moving Median (radius {radius})",
                           f"Triangular Weighted Moving Average (radius {radius})",
                           f"Exponential Weighted Moving Average (radius {radius})"],
                          [1,2,3,4]):
    
        make_blank_subplot(2,2,ctr)
        plt.scatter(x1,y1,color="lightgray")
        plt.plot(x1,vals,linewidth=3)
        plt.title(title,size=16)
        