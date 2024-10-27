import re

myRegex = '^(A|J|Q|K|[2-7])$'
a = 'nothing'
print(len(a))
while not re.match(myRegex, a)  :
    a = input('Enter a poker value (A, 2 to 7, J, Q or K):  >> ').upper() 
print(a, 'is a correct value. Well Done ;)')
