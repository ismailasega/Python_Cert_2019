# Create a 10x10 array with random values and find the minimum and maximum
# values.

import numpy as np

x = np.random.random((10, 10))

x_min, x_max = x.min(), x.max()

print('Created array = ', x)
print('\nMinimum Values: =', x_min)
print('\nMaximum Values: = ', x_max)
