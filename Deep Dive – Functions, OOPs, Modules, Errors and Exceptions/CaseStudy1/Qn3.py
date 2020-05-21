# Weather forecasting organization wants to show is it day or night. So, write a program for such organization to find
# whether is it dark outside or not

import time

my_time = time.localtime()

if my_time.tm_hour < 6 or my_time.tm_hour > 18:
    print('It is Dark Outside')
    print('And it is PM')
else:
    print('It is not Dark Outside')
    print('And it is AM')
