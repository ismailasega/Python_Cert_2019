# a program that accepts a sentence and calculate the number of letters and digits.
a = input("write your name and phone number \n")
b=x=0
for c in a:
    if c.isdigit():
        b=b+1
    elif c.isalpha():
        x=x+1
    else:
        pass
print("Letters", x)
print("Digits", b)