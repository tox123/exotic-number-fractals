from math import sqrt
from pylab import *
from numpy import NaN
from dualNum import *
 
def m(a):
	z = 0
	for n in xrange(1, 1500):
		z = z**2 + a
		if abs(z) > 7.5:
			return n
	return NaN
 
X = arange(-2, .5, .0002)
Y = arange(-1,  1, .0002)
Z = zeros((len(Y), len(X)))
 
for iy, y in enumerate(Y):
	print str(iy) + " of " + str(len(Y))
	for ix, x in enumerate(X):
		Z[iy,ix] = m(x + epsilon * y)
 
imshow(Z, cmap = plt.cm.prism, interpolation = 'none', extent = (X.min(), X.max(), Y.min(), Y.max()))
xlabel("Re(c)")
ylabel("Im(c)")
savefig("mandelbrot_python.svg")
show()  
