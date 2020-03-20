import matplotlib.pyplot as plt

# y = mx+b
# x = (y-b)/m

def calc_y(m,x,b):
    return m*x+b

def calc_x(m,y,b):
    return (y-b)/m
    

def mbline(M,B,xlim=[-5,5],ylim=[-5,5],**kwargs):
    
    x_lo = xlim[0]
    y_lo = ylim[0]
    
    x_hi = xlim[1]
    y_hi = ylim[1]
    
    for m,b in zip(M,B):
        
        x0 = x_lo
        y0 = calc_y(m,x_lo,b)
        
        if y0 < y_lo:
            x0 = calc_x(m,y_lo,b)
            y0 = y_lo
        
        x1 = x_hi
        y1 = calc_y(m,x_hi,b)
        
        if y1 > y_hi:
            x1 = calc_x(m,y_hi,b)
            y1 = y_hi

        plt.plot([x0,x1],[y0,y1],**kwargs)

if __name__ == '__main__':
    
    
    fig = plt.figure()
    fig.set_size_inches(16,16)
    ax = plt.axes(xlim=(-7,7), ylim=(-7,7))
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
    
    mbline([-.6,1,1.2],[1,1,1])
    plt.plot([-5,-5,5,5,-5],[-5,5,5,-5,-5])