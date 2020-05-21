# Create a random array of 3 rows and 3 columns and sort it according to 1st column,
# 2nd column or 3rd column

import numpy as np

x = np.random.randint(10, size=(3, 3))

i = x[x[:, 1].argsort()]
print('Array: ', x)

print('\nSorting according to 2nd Column: ', i)
