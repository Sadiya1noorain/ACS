UserInput = input('Enter the desired statement : \n')
n = len(UserInput)
space = 0
words = 1
for i in range(n):
    if(UserInput[i] == ' '):
        space += 1
        words += 1
print('Total no. of Spaces = ', space)
print('Total no. of Words = ', words)
print('Total no. of Characters = ', n)