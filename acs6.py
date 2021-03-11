common = []
unique = []
list1 = input('Enter first list of countries ')
list2 = input('Enter second list of countries ')

list1 = list(list1.split())
list2 = list(list2.split())
m = len(list1)
n = len(list2)
list1 = list(set(list1))
list2 = list(set(list2))

for i in range (m):
    for j in range (n):
        if list1[i] == list2[j]:
            common.append(list1[i])
        else:
            unique.append(list1[i])
            unique.append(list2[j])
            
unique = list(set(unique))
for ele in unique:
    if ele in common:
        unique.remove(ele)
        
print('The common countries from the two lists are', common)
print('The unique countries from the two lists are', unique)
