import Utils.Drawing as Drawing
import matplotlib.pyplot as plt
import math

def _draw_helper(turtle,pos):
    if turtle.arrow_headwidth != 0:
        Drawing.arrow_p(turtle.pos,pos,turtle.ax,
                        color=turtle.color,alpha=turtle.alpha,
                        linewidth=turtle.linewidth,zorder=turtle.zorder,
                        head_width=turtle.arrow_headwidth,length_includes_head=True)
    else:
        Drawing.connect_p(turtle.pos,pos,turtle.ax,
                          color=turtle.color,alpha=turtle.alpha,
                          linewidth=turtle.linewidth,zorder=turtle.zorder)

class mplTurtle:
    
    def __init__(self,pos=(0,0),angle=0,draw=True,ax=None,
                 color='black',alpha=1,linewidth=1,arrow_headwidth=0,zorder=0):
        self.pos = pos
        self.angle = angle%360
        self.draw = draw
        if ax == None:
            self.ax = plt.gca()
        else:
            self.ax = ax
        self.color = color
        self.alpha = alpha
        self.linewidth = linewidth
        self.zorder = zorder
        self.arrow_headwidth = arrow_headwidth
        
    def left(self,n):
        self.angle = (self.angle+n)%360
        
    def right(self,n):
        self.angle = (self.angle-n)%360
        
    def move_to(self,pos):
        if self.draw:
            _draw_helper(self,pos)
        self.pos = pos
        
    def point_to(self,pos):
        self.angle = math.degrees(math.atan2(pos[1]-self.pos[1],pos[0]-self.pos[0]))%360

    def forward(self,n):
        a = math.radians(self.angle)
        h = math.sin(a)*n
        w = math.cos(a)*n
        newpos = (self.pos[0]+w,self.pos[1]+h)
        if self.draw:
            _draw_helper(self,newpos)
        self.pos = newpos
        
    def backward(self,n):
        a = math.radians(self.angle)
        h = math.sin(a)*n
        w = math.cos(a)*n
        newpos = (self.pos[0]-w,self.pos[1]-h)
        if self.draw:
            _draw_helper(self,newpos)
        self.pos = newpos
        
    def stamp(self,r=None,color=None,alpha=None,zorder=None):
        if r == None:
            r = self.linewidth/2
        if color == None:
            color = self.color
        if alpha == None:
            alpha = self.alpha
        if zorder == None:
            zorder = self.zorder
        Drawing.draw_circle_p(self.pos,r,ax=self.ax,
                              color=color,alpha=alpha)