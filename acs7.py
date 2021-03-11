names = []
marks = []
for i in range(3):
    print('Enter the name of student' + str(i + 1))
    stdnt = input()
    names.append(stdnt)
    print('Enter marks of student ' +stdnt)
    score = input()
    marks.append(score)

print('Names of all students\n',names)
print('Marks of students respectively\n',marks)

SearchStudent = input('Enter name whose marks you want to access : ')
for i in range(3):
    if (SearchStudent == names[i]):
        print('The marks of ', SearchStudent, 'are ', marks[i])
    