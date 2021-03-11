# Demonstration of Variable Number of Arguments
def add(*a):
    return sum(a)

print(add(3, 5, 8))
print(add(2, 4, 6, 8))

# Demonstration of Keyword Arguments
def  hello(msg, name):
    print('\nHi', name, ',', msg)

hello(name = 'Emma', msg = 'Good Morning\n')

# Demonstration of Default Arguments
def fav(lang = 'Python'):
    print('I prefer using', lang)

fav('Java')
fav('C++')
fav()
fav('C#')
fav('HTML')
print('\n')

# Demonstration of Lambda Function
test = lambda a, b: a if a > b else b
print(test(47,10))
print(test(50, 56))