s = input('Enter your email address : ')
x = s.find('@')
print('The email address is', s)
print('The domain is', s[x + 1:])
