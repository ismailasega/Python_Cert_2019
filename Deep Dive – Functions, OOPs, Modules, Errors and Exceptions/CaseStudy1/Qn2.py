# Data of XYZ company is stored in sorted list.
# Write a program for searching specific data from that list.

XYZ_company = [2, 3, 4, 10, 40]


def search(a, b, c):
    for i in range(0, b):
        if a[i] == c:
            return i
    return -1


x = int(input('Enter a number: '))
n = len(XYZ_company)
result = search(XYZ_company, n, x)
if result == -1:
    print("Number is not present in array")
else:
    print("Number is present at index", result)
