## https://programmingdesignsystems.com/color/perceptually-uniform-color-spaces/
## https://matplotlib.org/users/artists.html

import matplotlib as mpl
from matplotlib.colors import hsv_to_rgb
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from numpy import linspace
import numpy as np


fig = plt.figure()
fig.set_size_inches(15,15)
ax1 = fig.add_subplot(2,2,2)
circ1 = Circle((-1,0),.5,fc=(1,0,0))
circ2 = Circle((1,-.5),.5,fc=(.5,.25,0))
ax1.add_patch(circ1)
ax1.add_patch(circ2)
ax1.annotate('Pure Red (255,0,0)', xy=(-2, .75),fontsize=20)
ax1.annotate('Brown (128,64,0)', xy=(0, .25),fontsize=20)
ax1.axis('equal')
ax1.axis([-3,3,-3,3])
ax1.axis('off')
ax1.set_title("How RGB Color Works")

ax2 = fig.add_subplot(2,2,1)
circ1 = Circle((-1.2,1),.4,fc=(1,0,0))
circ2 = Circle((-.5,.5),.4,fc=(.3,0,0))
circ3 = Circle((.2,0),.4,fc=(0,0,.3))
ax2.add_patch(circ1)
ax2.add_patch(circ2)
ax2.add_patch(circ3)
ax2.axis('equal')
ax2.axis([-3,3,-3,3])
ax2.axis('off')
ax2.set_title("Which pair feels most similar?")
ax2.text(-3.5,-2,"First and second have idential hue.\nSecond and third have identical bightness.",fontsize=20)

ax3 = fig.add_subplot(4,2,6)
ax4 = fig.add_subplot(4,2,8)
gradient = linspace(0, 1, 256)
grad = np.vstack((gradient, gradient))
ax3.imshow(grad, aspect='auto', cmap='hsv')
ax4.imshow(grad, aspect='auto', cmap='rainbow')
ax3.axis('off')
ax4.axis('off')

ax5 = fig.add_subplot(2,2,3)
ax5.axis('off')
ax5.axis('equal')
ax5.axis([-1,7,-1,7])
ax5.set_title("HSV Color space")

for i in range(1,8):
    for j in range(1,8):
        col = hsv_to_rgb([1,i/7,j/7])
        ax5.add_artist(Circle((i-1,j-1),.4,fc=col))


plt.savefig("COLORS.png")



## What is color?
## It is easy to name color. Red, green, blue, black, and so on but we quickly run into confusion! Is turquiose a color all its own or is it a kind of blue? Maybe a kind of green? How about pink? Is it just light red? Is dark red a color or just a shade?
## What we're driving at here, of course, is that when we talk about color in our everyday lives we aren't very precise about what we mean. In order to understand color more deeply we need to study the various components of colors in order to develop a sense of what a color is. This is more important than it seems. Cultures do not universally agree on their informal definition of colors. In Russian for instance the words goluboy and siniy both refer to what is called blue in English. Meanwhile in traditional Japanese the word ao covers both blue and green.
## Perhaps the most famous Western example of differences in how color is described comes from the works of Homer in which the sea is said to be the color of wine and the sky is described as bronze among many other strange color descriptions. By tradition Homer was blind but there is no evidence for that and regardless it seems unlikely an oral tradition would preseve bizarre color classifications. Colorblindless also doesn't work as an explanation since there is no such thing as yellow-green or blue-brown colorblindness. There is a simpler explanation. Homer did not divide up colors the same way that we do.
## While we would not say that the sea is the color of wine it does resemble wine in its visual texture both are dark saturated colors. The sky likewise shares a visual trait in common with bronze, they are both bright. Indeed a psychologist who made a point of not telling is daughter the color of the sky found that when he asked she said it was white rather than blue. Like Homer she focused in on the brightness rather than what we would call color This probably should not be too surprising. A dark red and a dark blue have more immediately in common to the eye than a dark red and a bright red.
## Lets begin with hue. It is easily understood concept but difficult to define well. Hue is what makes red visually distinct from green. However these two colors actually have a few differences. Fundamentally hue can only real be defined in terms of physics and biology. When a photon with a wavelength of about 700nm interacts with the cone cells in the eye we percieve the color red. Lower wavelength photons move through the rainbow. Red, orange, yellow, green, indigo, violet. The biology of the eye also allows us to see mixtures of photons as colors like brown which occurs when we see a mix of yellow and red photons. In total the typical person can percieve between two and three million different hues. A small part of the population has much smaller (colorblindness) or much greater (tetrachromia) ability to distigush colors due to mutations.
## In order to define hue a variety of methods can be used. The most common of these for mathematical purposes is the RGB color space. The idea is that red, green, and blue, can be mixed in varying amounts to poduce the whole gamut of colors that humans can percieve. The colors are always used in that order and usually are defined as ranging from 0 to 255. So pure bright red is the point (255,0,0) and brown is (128,64,0), a dark mix of red and green and thus a shade of orange. While the RGB color space is very useful it is not a natural way of thinking about colors. 
## An alternative is the HSV color space which is designed to be more intuitive to think about. This space is shaped like a cylinder. Around the edges are the colors in rainbow order, wrapping back around from red to violet and back again. Moving toward the center of the cylinder adds white. Moving down the cylinder adds blacks. Ultimately this produces all of the same colors as the RGB model but it seperates out the important properties of hue (percieved color), saturation (colorfullness), and lightness.
## Consider the following image which shows rainbow as it exists in the HSV color space. All the colors have the same saturation and lightness. While it clear runs through the whole range of colors there is a problem. Notice the brighter bands of color. So far we have limited our understand of color to physics but to understand this we need to look at the biology of color perception. The human eye does not detect the precise wavelengths of photons. Instead
