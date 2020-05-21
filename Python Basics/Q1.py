#a program which will find factors of given number and find whether the factor is even or odd.
x = int(input("Input a Number: "))
if (x % 2) != 0:
   print("{0} is Odd".format(x))
else:
   print("{0} is Even".format(x))