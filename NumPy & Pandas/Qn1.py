# Extract data from the given
# SalaryGender CSV file and store the data
# from each column in a separate NumPy array


import numpy as np

a = np.genfromtxt("SalaryGender.csv", delimiter=',', skip_header=1)

print(a)

