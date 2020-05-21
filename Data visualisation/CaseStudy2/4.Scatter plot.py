# Plot Scatter Plot for the invoice amounts and see the concentration of amount.
# In which range most of the invoice amounts are concentrated


import matplotlib.pyplot as plt
import pandas as pd

data_set1 = pd.read_csv("BigMartSalesData.csv")

x = data_set1['InvoiceNo']
y = data_set1['Amount']

plt.scatter(x, y, color='red')
plt.title('Scatter Plot for the invoice amounts')
plt.show()