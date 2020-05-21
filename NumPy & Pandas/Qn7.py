# Create a numpy array having NaN (Not a Number) and print it.
# array([ nan, 1., 2., nan, 3., 4., 5.])
# Print the same array omitting all elements which are nan


import numpy as np

a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
i = [x for x in a if str(x) != 'nan']

print('Numpy array having NaN =', a)

print('\nNumpy array without NaN =', i)
