import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import numpy as np
import numpy.polynomial.polynomial as poly
from itertools import product

## The polyroots function takes a vector as an input and returns the roots of the polynomial it describes
## with coefficiens in increasing order (starting from x^0)

## Range of coefficients starting with 0
c = 6
## Degree
d = 6
## Number of polynomials to evaluate in total
trn = 10000

## All possible complex coefficients from zero to c (inclusive)
z = []
for a in range(c+1):
    for b in range(c+1):
        z.append(complex(a,b))

fig = plt.figure()
plt.axis('off')
plt.axes().set_aspect('equal', 'datalim')
fig.set_size_inches(10,10)
ax = plt.Axes(fig,[0.,0.,1.,1.])
ax.set_axis_off()
fig.add_axes(ax)

cols = cm.rainbow(np.linspace(0,1,c))

for lead in range(1,c+1):
    for i,j in enumerate(product(z,repeat=d)):
        if j[-1] == lead:
            r = poly.polyroots(j)
            x = (real(r),-real(r))
            y = (imag(r),imag(r))
            plt.scatter(x,y,c = [cols[lead-1]], s = 2, alpha = .3)
            if i >= trn:
                print("Truncating Execution")
                break

print("DONE!")

tit = "PolyStars (Degree {}, Coef up to {}, Truncated at {}).png".format(d,c,trn)

plt.savefig(tit,dpi=100)