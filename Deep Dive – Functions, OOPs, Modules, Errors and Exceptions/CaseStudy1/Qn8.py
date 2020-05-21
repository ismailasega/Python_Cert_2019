# Write a program that calculates and prints the value according to the given formula:Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H: C is 50. H is 30.D  is  the  variable  whose  values  should
# be  input  to  your  program  in  a  comma-separated sequence.

import math

C, H = 50, 30

value = []
Dv = input('Enter Values of D: ')
Ds = Dv.split(",")
Ds = [int(i) for i in Ds]
i = 0
x = len(Ds)
while i < x:
    Q = round(math.sqrt((2 * C * Ds[i]) / H))
    value.append(Q)
    i += 1
print("The output is: ", value)
