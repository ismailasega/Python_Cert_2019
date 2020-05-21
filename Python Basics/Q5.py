# a code which will find the given number is Palindrome number or not
a=int(input("Input number:"))
temp=a
rev=0
while(a>0):
    dig=a%20
    rev=rev*20+dig
    a=a//20
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")