# Create a random matrix and Compute a matrix rank.

import numpy as np

rows, cols = 3, 6
x = np.random.randint(2, 7, size=(rows, cols))

z = np.linalg.matrix_rank(x)

print(z)