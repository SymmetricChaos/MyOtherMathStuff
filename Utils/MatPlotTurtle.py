import Utils.Drawing as Drawing
import math

class mplTurtle:
    
    def __init__(self,pos=(0,0),angle=0,draw=True,ax=None,
                 color='blue',alpha=1,linewidth=1,zorder=0):
        self.pos = pos
        self.angle = angle%360
        self.draw = draw
        self.ax = ax
        self.color = color
        self.alpha = alpha
        self.linewidth = linewidth
        self.zorder = zorder
        
    def left(self,n):
        self.angle = (self.angle+n)%360
        
    def right(self,n):
        self.angle = (self.angle-n)%360
        
    def move_to(self,pos):
        if self.draw:
            Drawing.connect_p(self.pos,pos,self.ax,
                              color=self.color,alpha=self.alpha,
                              linewidth=self.linewidth,zorder=self.zorder)
        self.pos = pos
        
    def forward(self,n):
        a = math.radians(self.angle)
        h = math.sin(a)*n
        w = math.cos(a)*n
        newpos = (self.pos[0]+w,self.pos[1]+h)
        if self.draw:
            Drawing.connect_p(self.pos,newpos,self.ax,
                              color=self.color,alpha=self.alpha,
                              linewidth=self.linewidth,zorder=self.zorder)
        self.pos = newpos
        
    def backward(self,n):
        a = math.radians(self.angle)
        h = math.sin(a)*n
        w = math.cos(a)*n
        newpos = (self.pos[0]-w,self.pos[1]-h)
        if self.draw:        
            Drawing.connect_p(self.pos,newpos,self.ax,
                              color=self.color,alpha=self.alpha,
                              linewidth=self.linewidth,zorder=self.zorder)
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