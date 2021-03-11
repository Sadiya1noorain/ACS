common = []
unique = []
list1 = input('Enter first list of countries ')
list2 = input('Enter second list of countries ')

list1 = list(list1.split())
list2 = list(list2.split())

list1 = list(set(list1))
list2 = list(set(list2))

for m in list1:
    if m in list2:
        common.append(m)
    else:
        unique.append(m)
for m in list2:
    if m not in list1:
        unique.append(m)

print('The common countries from the two lists are', common)
print('The unique countries from the two lists are', unique)
