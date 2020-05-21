# Create a four dimensions array get sum over the last two axis at once.

import numpy

a = numpy.arange(2*3*4*5).reshape((2, 3, 4, 5))

x = a.sum(axis=(-2, -1))

print(x)

