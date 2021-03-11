names = []
marks = []
for i in range(3):
    print('Enter the name of student' + str(i + 1))
    stdnt = input()
    names.append(stdnt)
    print('Enter marks(2 subjects) of ' +stdnt)
    score = input()
    marks.append(score)

for i in range(3):
    print('Name of student = ', names[i])
    print('---> Marks = ', marks[i])

SearchStudent = input('Enter name whose marks you want to access : ')
for i in range(3):
    if (SearchStudent == names[i]):
        print('The marks of ', SearchStudent, 'are ', marks[i])
    
    
