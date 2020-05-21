# Design a software for bank system.
# There should be options like cash withdraw, cash credit and change password.
# According to user input, the software should provide required output.


def cash_withdrawal():
    pin = input('Enter PIN to proceed:')
    if pin == 1234:
        print('Please Wait!\n Your Transaction is Being Processed')
    else:
        print('Wrong PIN\n Try Again')


def cash_credit():
    pin = input('Enter PIN to proceed:')
    if pin == 1234:
        print('Please wait as we validate your PIN')
    else:
        print('Wrong PIN. Try Again')


def change_password():
    pin = input('Enter PIN to proceed:')
    if pin == 1234:
        print('PIN has been Changed, your new pin is: ',  )
    else:
        print('Invalid PIN. Try Again')


def menu():
    print('Welcome to ASEGA Bank!.. Select options')
    print('1. Cash withdrawal\n2. Cash Credit\n3. Change Password')
    selected_option = input('Enter your option:')
    if selected_option == 1:
        cash_withdrawal()
    if selected_option == 2:
        cash_credit()
    if selected_option == 3:
        change_password()


menu()
