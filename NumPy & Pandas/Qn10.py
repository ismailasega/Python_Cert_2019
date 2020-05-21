# Create numpy array having elements 0 to 10 And negate all the elements between
# 3 and 9

import numpy as np

x = np.arange(10)

condition = np.logical_and(x > 3, x < 9)
b = np.select([~condition, condition], [x, -x])

print(b)
