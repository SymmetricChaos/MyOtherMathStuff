from Drawing import *
import numpy as np
import os

### Subplots example ###
canvas1 = make_blank_canvas([15,15],facecolor="lightgray")

# Make and use a subplot
sp1 = make_blank_plot(2,2,1,[-3,3])

# mbline takes ylim and xlim from axes to automatically appear infinite
mbline(-.5,0)
# mbline or mblines can be manually limited
slopes = np.linspace(0,5,10)
mblines(slopes,[0]*20,xlim=[-2,1],ylim=[-2,1],color='red')

# Subplots of different layouts can coexist
sp2 = make_blank_plot(4,4,4,[-2,2],facecolor='yellow')
draw_closed_curve_xy([1,2,3],[0,1,0],color='salmon')
# Create an mbline on the most recently created axes
mbline(1,1)

# Plots can be created out of order
# When subplots are not square shapes are warped
sp3 = make_blank_plot(2,2,4,[-3,3],[-5,5])
draw_circle_xy(1.5,-.5,1,fc='white',ec='black')
text(-.8,3.5,"Shapes and lines on this plot are skewed\nbut not text\nthat's a circle down there",ha="center")

# Show automatic xlim and ylim settings
sp4 = make_blank_plot(4,4,7)
x = np.random.uniform(-2,2,200)
y = x+np.random.uniform(-2,2,200),
draw_dots_xy(x,y,alpha=.5,color='limegreen')
title("BLOOPS",size=30)

# Add lines to a chosen axes
mblines([1,2,3],[0,0,0],ax=sp3)

# Make some circles
draw_circles_xy([0,1,2],[0,0,0],[.5,.3,1],sp2,ec='black',fc='green')

# Title on selected axis
title(r'We can use LaTeX $\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}$',ax=sp1,size=16,pad=20)
canvas_title("A Title for the whole Canvas")

# Show how to put an image into a plot
cur_dir = os.getcwd()
tree_pic = cur_dir+"\\Tree.png"
image(tree_pic,-2,1,scale=.3,ax=sp1)
image_box(tree_pic,2,-1,scale=.3,ax=sp1)

sp5 = make_blank_plot(4,4,9)
table([["A","B","C"],
       ["1","2","3"],
       ["x","y","z"],
       ["{}"," ","NULL"]],
      loc='center',colWidths=[.2,.2,.2],yscale=2)

canvas1.savefig('fig1.png', dpi=canvas1.dpi)





### Statistical plots ###
canvas2 = make_blank_canvas([15,15])
canvas_title("Some Satistical Plots",size=25)

make_plot(3,3,1)
histogram(np.random.gamma(9,3,900),fc="orange",ec="black")
title("Histogram")

# For some reason a pie chart will automatically supress the frame of the 
# plot that contains it
make_blank_plot(3,3,2)
pie_chart([1,1,2,2,5],explode=[0,.1,0,0,.05],frame=True,
          radius=.3,center=(.5,.5))
title("Pie Chart")

fake_data = [np.random.exponential(1,50),
              np.random.exponential(2,50),
              np.random.standard_normal(50)]

make_plot(3,3,3)
boxplot(fake_data,labels=["A","B","C"])
title("Boxplot")

make_blank_plot(3,3,4)
violin_plot(fake_data,labels=["A","B","C"],vert=False)
title("Violin Plot")

X, Y = np.meshgrid(np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2))
U = np.cos(X)
V = np.sin(Y)

make_blank_plot(3,3,5)
quiver_plot(X,Y,U,V)
title("Quiver Plot")

canvas2.savefig('fig2.png', dpi=canvas2.dpi, pad=0)