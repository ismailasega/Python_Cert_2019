# Write  a  program  that  accepts  a  sentence  and  calculate  the  number  of  upper
# case letters and lower case letters.

string = input("Enter 3 Names: ")
upper = 0
lower = 0
for x in string:
    if x.isupper():
        upper += 1
    if x.islower():
        lower += 1

print("\nUPPER CASE: ", upper)
print("\nLOWER CASE: ", lower)
