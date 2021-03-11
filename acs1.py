n = int(input("Number of numbers in Series = "))
print('Enter the numbers')
a = []
for i in range(0, n):
    numbers = int(input())
    a.append(numbers)
print('The average of the numbers is ', sum(a)/n)
