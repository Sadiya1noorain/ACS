UserList = []
evenList = []
oddList = []
n = int(input('Number of elements in the list = '))
print('Enter the elements of list : ')
for i in range(n):
    ele = int(input())
    UserList.append(ele)
    if (UserList[i] > 0):
        if ele % 2 == 0 :
            evenList.append(ele)
        else:
            oddList.append(ele)
    
print(UserList)
print(evenList)
print(oddList) 
