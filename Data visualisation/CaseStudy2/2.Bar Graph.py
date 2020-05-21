# Plot Total Sales Per Month for Year 2011 as Bar Chart. Is Bar Chart Better to
# visualize than Simple Plot?

import pandas as pd
import matplotlib.pyplot as plt

data_set1 = pd.read_csv("BigMartSalesData.csv", index_col=0, skiprows=range(1, 42481))

y = data_set1['Amount']
plt.bar(data_set1, height=y)
plt.legend(labels=data_set1.index, loc='best')
plt.title('Total Sales Per Month for Year 2011')
plt.show()