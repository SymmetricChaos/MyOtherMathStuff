import Drawing as draw
from MatPlotTurtle import mplTurtle
import numpy as np
import os
import random
from PointManip import midpoint


def general_example(save=False):
    canvas1 = draw.make_blank_canvas([15,15],facecolor="lightgray")
    
    # Make and use a subplot
    sp1 = draw.make_blank_plot(2,2,1,[-3,3])
    
    # mbline takes ylim and xlim from axes to automatically appear infinite
    draw.mbline(-.5,0)
    # mbline or mblines can be manually limited
    slopes = np.linspace(0,5,10)
    draw.mblines(slopes,[0]*20,xlim=[-2,1],ylim=[-2,1],color='red')
    
    # Subplots of different layouts can coexist
    sp2 = draw.make_blank_plot(4,4,4,[-2,2],facecolor='yellow')
    draw.closed_curve_xy([1,2,3],[0,1,0],color='salmon')
    # Create an mbline on the most recently created axes
    draw.mbline(1,1)
    
    # Plots can be created out of order
    # When subplots are not square shapes are warped
    sp3 = draw.make_blank_plot(2,2,4,[-3,3],[-5,5])
    draw.circle_xy(1.5,-.5,1,fc='white',ec='black')
    draw.text_xy(-.8,3.5,"Shapes and lines on this plot are skewed\nbut not text\nthat's a circle down there",
            ha="center")
    
    # Show automatic xlim and ylim settings
    sp4 = draw.make_blank_plot(4,4,7)
    x = np.random.uniform(-2,2,200)
    y = x+np.random.uniform(-2,2,200),
    draw.dots_xy(x,y,alpha=.5,color='limegreen')
    draw.title("BLOOPS",size=30)
    
    # Add lines to a chosen axes
    draw.mblines([1,2,3],[0,0,0],ax=sp3)
    
    # Make some circles
    draw.circles_xy([0,1,2],[0,0,0],[.5,.3,1],sp2,ec='black',fc='green')
    
    # Title on selected axis
    draw.title(r'We can use LaTeX $\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}$',ax=sp1,size=16,pad=20)
    draw.canvas_title("A Title for the whole Canvas")
    
    # Show how to put an image into a plot
    cur_dir = os.getcwd()
    tree_pic = cur_dir+"\\Tree.png"
    draw.image(tree_pic,-2,1,scale=.3,ax=sp1)
    draw.image_box(tree_pic,2,-1,scale=.3,ax=sp1)
    
    sp5 = draw.make_blank_plot(4,4,9)
    draw.table([["A","B","C"],
           ["1","2","3"],
           ["x","y","z"],
           ["{}"," ","NULL"]],
          loc='center',colWidths=[.2,.2,.2],yscale=2)
    
    draw.arrow_p([0,0],[.5,-.5],head_width=.2,ax=sp3)
    
    if save:
        canvas1.savefig('fig1.png', dpi=canvas1.dpi)





def statistical_plots(save=False):
    canvas2 = draw.make_blank_canvas([15,15])
    draw.canvas_title("Some Satistical Plots",size=25)
    
    draw.make_plot(3,3,1)
    draw.histogram(np.random.gamma(9,3,900),fc="orange",ec="black")
    draw.title("Histogram")
    
    # For some reason a pie chart will automatically supress the frame of the 
    # plot that contains it
    draw.make_blank_plot(3,3,2)
    draw.pie_chart([1,1,2,2,5],explode=[0,.1,0,0,.05],frame=True,
              radius=.3,center=(.5,.5))
    draw.title("Pie Chart")
    
    fake_data = [np.random.exponential(1,50),
                  np.random.exponential(2,50),
                  np.random.standard_normal(50)]
    
    draw.make_plot(3,3,3)
    draw.boxplot(fake_data,labels=["A","B","C"])
    draw.title("Boxplot")
    
    draw.make_blank_plot(3,3,4)
    draw.violin_plot(fake_data,labels=["A","B","C"],vert=False)
    draw.title("Violin Plot")
    
    X, Y = np.meshgrid(np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2))
    U = np.cos(X)
    V = np.sin(Y)
    
    draw.make_blank_plot(3,3,5)
    draw.quiver_plot(X,Y,U,V)
    draw.title("Quiver Plot")
    
    if save:
        canvas2.savefig('fig2.png', dpi=canvas2.dpi, pad=0)





def turtle_plots(save=False):
    canvas3 = draw.make_blank_canvas([15,15])
    draw.canvas_title("Turtle Graphics",size=25)
    
    draw.make_blank_plot(2,2,1,xlim=[-12,12])
    draw.title("A Cesaro Tree")
    
    def my_tree(turt,level):
        turt.linewidth = level
        turt.left(45)
        turt.forward(level/4)
        
        if level > 0:
            my_tree(turt,level-1)
        turt.linewidth = level
        turt.backward(level/4)
        turt.right(90)
        turt.forward(level/4)
    
        if level > 0:
            my_tree(turt,level-1)
        turt.linewidth = level
        turt.backward(level/4)
        turt.left(45)
    
    my_turtle = mplTurtle(color='brown',angle=90,alpha=.4)
    my_tree(my_turtle,10)
    
    
    draw.make_plot(2,2,2,xlim=[-5,5])
    draw.title("Change Lines to Arrows")
    turtle1 = mplTurtle(linewidth=2,arrow_headwidth=.2)
    for i in range(40):
        turtle1.forward(.5+.03*i)
        turtle1.left(33)
    
    
    draw.make_plot(2,2,3,xlim=[-5,5])
    draw.title("Stamps Only\nNo Lines")
    P = [(-4,-4),(4,-4),(0,4)]
    
    turtle2 = mplTurtle(draw=False,color="gray")
    for i in range(1000):
        newpos = midpoint(turtle2.pos,random.choice(P))
        turtle2.move_to(newpos)
        turtle2.stamp(.02)
        
    
    draw.make_plot(2,2,4,xlim=[-5,5])
    draw.title("Bounded in a Nutshell")
    P = [(-4,-4),(4,-4),(4,4),(-4,4)]
    
    turtle3 = mplTurtle(color='green')
    for i in range(500):
        target = random.choice(P)
        turtle3.point_to(target)
        turtle3.forward(1)

    if save:
        canvas3.savefig('fig3.png', dpi=canvas3.dpi, pad=0)


if __name__ == '__main__':
    general_example()
    statistical_plots()
    turtle_plots()