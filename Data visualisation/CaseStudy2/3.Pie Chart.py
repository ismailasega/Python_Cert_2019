# Plot Pie Chart for Year 2011 Country Wise. Which Country contributes highest
# towards sales?

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('BigMartSalesData.csv', skiprows=range(1, 42481))
count = df['Country'].value_counts()
print(count)
plt.pie(count, labels=count.index, shadow=True, startangle=90)
plt.axis('equal')
plt.legend(labels=count.index, loc='best')
plt.title("Pie Chart for Year 2011 Country Wise")
plt.show()