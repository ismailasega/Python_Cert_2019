# write a program to print this list after removing
# all duplicate values with original order reserved.

a = (12, 24, 35, 24, 88, 120, 155, 88, 120, 155)

def removeDuplicate(values):

    new_list = []
    seen = set()
    for num in values:
        if num not in seen:
            seen.add(num)
            new_list.append(num)

    return new_list


print(removeDuplicate(a))
