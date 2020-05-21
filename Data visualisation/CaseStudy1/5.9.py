# 5.9: Create a dataframe from following data
# 'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
# 'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
# 'female': [0, 1, 1, 0, 1],
# 'age': [42, 52, 36, 24, 73],
# 'preTestScore': [4, 24, 31, 2, 3],
# 'postTestScore': [25, 94, 57, 62, 70]
# Draw a Scatterplot of preTestScore and postTestScore, with the size of each point
# determined by age

import matplotlib.pyplot as plt
first_name = ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
last_name = ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
female = [0, 1, 1, 0, 1],
age = [42, 52, 36, 24, 73],
preTestScore = [4, 24, 31, 2, 3],
postTestScore= [25, 94, 57, 62, 70]
plt.scatter(preTestScore, postTestScore, size=300)
plt.show()