# By using list comprehension, please write a
# program to print the list after removing the value 24

lst = [12, 24, 35, 24, 88, 120, 155]

lst = [i for i in lst if i != 24]

print(lst)
