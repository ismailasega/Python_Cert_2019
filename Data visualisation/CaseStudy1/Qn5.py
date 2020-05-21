# Let the x axis data points and y axis data points are
# X = [1,2,3,4]
# y = [20, 21, 20.5, 20.8]


import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [20, 21, 20.5, 20.8]

plt.plot(x, y, figsize=(4, 5), dpi=100)
plt.title('A Graph of Usage')
plt.xlabel('People')
plt.ylabel('Usage')
plt.show()