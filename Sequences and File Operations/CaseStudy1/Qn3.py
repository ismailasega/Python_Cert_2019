#A website requires a user to input username and password to register.
#Write a program to check the validity of password given by user.
#Following are the criteria for checking password:

from re import search

username = input('Registrations Form\n Create username: ')
password = input(' Create password: ')

p = True
while p:
    if len(password) < 6 or len(password) > 12:
        break
    elif not search('[a-z]', password):
        break
    elif not search('[0-9]', password):
        break
    elif not search('[A-Z]', password):
        break
    elif not search('[$#@]', password):
        break
    else:
        print('Valid Password')
        p = False
        break

if p:
    print('Invalid Password')