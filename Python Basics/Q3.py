#Write a program, which will find all the numbers between 1000 and 3000 (both
#included) such that each digit of a number is an even number. The numbers
#obtained should be printed in a comma separated sequence on a single line

num = []

for a in range(1000, 3000):
    b = str(a)
    if (int(b[0])%2==0) & (int(b[1])%2==0) & (int(b[2])%2==0):
        num.append(b)

print( ",".join(num))