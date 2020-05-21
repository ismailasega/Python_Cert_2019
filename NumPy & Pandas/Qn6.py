# Create a numpy array [[0, 1, 2], [ 3, 4, 5], [ 6, 7, 8],[ 9, 10, 11]]) and filter the elements
# greater than 5.

import numpy as np

x = np.array([[0, 1, 2], [2, 4, 5], [6, 7, 8], [9, 10, 11]])

print('Values greater than 5 =', x[x > 5])



