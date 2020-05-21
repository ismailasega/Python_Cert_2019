# Plot a pie-chart of the number of models released by every manufacturer,
# recorded in the data provide. Also mention the name of the manufacture with
# the largest releases.


import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Cars2015.csv')
count = df['Make'].value_counts()
print(count)
plt.pie(count, labels=count.index)
plt.axis('equal')
plt.legend(labels=count.index, loc='best')
plt.title("A Pie-chart of the number of models released by every manufacturer")
plt.show()
