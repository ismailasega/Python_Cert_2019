# Store the “Age” and “PhD”
# columns in one DataFrame and delete the data of all people who don’t have a PhD

import pandas

df = pandas.read_csv('SalaryGender.csv', usecols=['Age', 'PhD'])
index_names = df[df['PhD'] == 0].index
df.drop(index_names, inplace=True)

print(df)
