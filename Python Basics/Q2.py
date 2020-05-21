#accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically.
str = input("type 7 names, then press enter: \n ")

names = str.split()
names.sort()

print("The names in alphabetic order:")
for name in names:
   print(name)