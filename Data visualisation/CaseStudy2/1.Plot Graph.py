# Plot Total Sales Per Month for Year 2011. How the total sales have increased
# over months in Year 2011. Which month has lowest Sales?

import pandas as pd
import matplotlib.pyplot as plt

data_set1 = pd.read_csv("BigMartSalesData.csv", skiprows=range(1, 42481))

x = data_set1['Amount']
y = data_set1['Month']

plt.plot(x, y)
plt.legend(labels=y, loc='best')
plt.title('Total Sales Per Month for Year 2011')
plt.show()