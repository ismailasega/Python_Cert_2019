# Calculate the total number of people who have a PhD degree from SalaryGender
# CSV file.

import pandas

PhD_Holders = pandas.read_csv('SalaryGender.csv', usecols=['PhD'])

people = PhD_Holders[PhD_Holders['PhD'] == 0].index

PhD_Holders.drop(people, inplace=True)

print(PhD_Holders.count())
