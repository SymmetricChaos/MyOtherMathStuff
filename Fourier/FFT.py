import numpy as np
from Utils import make_canvas,plot_points
from numpy.fft import fft, ifft

x = np.arange(0,6,.1)
y1 = np.sin(x)
y2 = np.sin(2*x)
y = y1+y2

print(x)
print(y)

f = ifft(fft(y))

make_canvas([0,6],[-2,2],5)
plot_points([i for i in zip(x,f)])
plot_points([i for i in zip(x,y)])