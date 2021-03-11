import sys
marksList = []
zero = 0
marks = input('Enter the marks of 5 students :')

marks = marks.split()
marksList = list(map(int, marks))
avg = sum(marksList)/5

if len(marksList) != 5:
    sys.exit("No. of marks != 5")

print('The entered numbers = ',marksList)    
print('The highest scored mark = ',max(marksList))
print('The least scored mark = ',min(marksList))
print('The average of the students marks = ',avg)

marksList.sort(reverse=True)

print('The top three marks are ', marksList[0 : 3])
print('The second highest scored mark = ', marksList[1])

for f in marksList:
    if(f == 0):
        zero += 1
if(zero != 0):
    print('The number of student(s) scored 0 mark = ',zero)
