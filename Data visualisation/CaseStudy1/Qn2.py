# The dataset given, records data of city temperatures over the years 2014 and
# 2015. Plot the histogram of the temperatures over this period for the cities of
# San Francisco and Moscow.

import pandas as pd
import matplotlib.pyplot as plt

data_set = pd.read_csv("CityTemps.csv", usecols=['San Francisco', 'Moscow'])

print(data_set)

plt.hist(data_set)
plt.title('A histogram of the Temperatures')
plt.show()
