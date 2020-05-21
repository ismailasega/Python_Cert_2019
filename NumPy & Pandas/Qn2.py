# Find The number of men with a PhD
# The number of women with a PhD

import csv

with open('SalaryGender.csv') as file:
    m, f = 0, 0
    for row in csv.DictReader(file):
        if row["Gender"] == "1":
            m += 1
        else:
            f += 1

print("Number of Men = {}".format(m))
print("Number of Women = {}".format(f))
