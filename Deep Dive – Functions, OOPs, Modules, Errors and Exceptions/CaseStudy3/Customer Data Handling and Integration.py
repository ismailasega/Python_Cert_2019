# Customer Data Handling and Integration System

import csv

x = []

y = []

blacklisted = 1


class CustomerNotAllowed(Exception):
    pass


with open('FairDealCustomerData.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        name = row[1]
        order = row[0]
        if name:
            x.append(name.split())
        if order:
            y.append(''.join(order))
    print('\nCustomer Class =', x)
    print('\nOrder Class =', y)
    a = input('\nEnter product_name from order class above: ')
    b = int(input('Enter product_code: '))
    if b == blacklisted:
        raise CustomerNotAllowed
    else:
        print('Order Type: ', a)
