# Create a random array and swap two rows of an array.

import numpy as np

i = np.random.random((5, 3))

x = i[np.random.randint(0, i.shape[0], 2)]

print(i)

print('\n', x)
