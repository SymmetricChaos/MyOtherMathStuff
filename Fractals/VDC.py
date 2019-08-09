# The Van de Corput sequences are quasirandom sequences on the unit interval
# guaranteed to be equidistributed. They are a simple replacement for random
# or psuedrorandom numbers when equidistribution is needed.

def vdcSeq(b,ra):
    for n in range(ra):
        vdc, denom = 0,1
        while n != 0:
            denom *= b
            n, r = divmod(n,b)
            vdc += r/denom
        yield vdc
        

# Fill a unit square using VDC sequences
import matplotlib.pyplot as plt

# Small coprime numbers don't show significant patterns.
X = [i for i in vdcSeq(2,500)]
Y = [i for i in vdcSeq(3,500)]
plt.axes().set_aspect('equal')
plt.scatter(X,Y,color="black")
plt.show()

# If we don't chose coprime values the square will be filled in an obvious
# pattern.

X = [i for i in vdcSeq(2,500)]
Y = [i for i in vdcSeq(4,500)]
plt.axes().set_aspect('equal')
plt.scatter(X,Y,color="black")
plt.show()

# We also run into problems with larger numbers which also cause large scale
# patterns.
X = [i for i in vdcSeq(11,500)]
Y = [i for i in vdcSeq(19,500)]
plt.axes().set_aspect('equal')
plt.scatter(X,Y,color="black")
plt.show()