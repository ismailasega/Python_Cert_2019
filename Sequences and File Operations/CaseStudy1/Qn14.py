# Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  given  n  input  by console (n>0)

n = 5

def sum(n):
    y = 0
    for i in range(1, n + 1):
        x = i / (i + 1)
        y = y + x
    return y


print("Sum is", round(sum(n), 2))
