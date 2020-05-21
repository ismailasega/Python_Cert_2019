# a program which count and print the numbers of each character
# in a string input by console.

a = 'abcdefgabc'
x = {}
for char in a:
    if char not in x:
        x[char] = 1
    else:
        x[char] += 1
for key in x:
    print(key, ",", x[key])
