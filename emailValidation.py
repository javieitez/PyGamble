############################
# quick and dirty ref for email 
# address validation
############################
a = False
while a == False:
    b = input('Enter your email address: ')
    a = '@' in b and '.' in b

print(b, 'seems to be a valid email address')
