# You are given a dataset, which is present in the LMS, containing the number of
# hurricanes occurring in the United States along the coast of the Atlantic. Load the
# data from the dataset into your program and plot a Bar Graph of the data, taking
# the Year as the x-axis and the number of hurricanes occurring as the Y-axis.

import pandas as pd
import matplotlib.pyplot as plt

data_set = pd.read_csv("Hurricanes.csv")
print(data_set)
height = [3, 12, 5, 18, 45]
plt.bar(data_set, height=height)
plt.title(' Hurricanes Bar Graph')
plt.xlabel('Year')
plt.ylabel('The number of hurricanes occurring')
plt.show()

