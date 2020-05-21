# Write a program that accepts a comma separated sequence of words as input
# and prints the words in a comma-separated sequence after sorting them
# alphabetically

lst = [x for x in input('Enter 4 Comma Separated words: ').split(',')]
lst.sort()
print(','.join(lst))