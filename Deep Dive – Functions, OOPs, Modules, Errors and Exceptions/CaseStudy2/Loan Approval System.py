# Loan Approval System

import csv

f = open('bank-data.csv')
csv_f = csv.reader(f)

unique_jobs = []

x = input('Enter a your profession: ')

while True:
    for row in csv_f:
        unique_jobs.append(row[1])
    if x == 'END':
        break
    elif x.lower() not in unique_jobs:
        print('Not Eligible for loan')
        break
    else:
        print('You are Eligible for a loan')
        break
