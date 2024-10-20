####################################################
#
# quick demo for forced inputs and screen colors
# the user is forced to enter a certain type of string, 
# the promp repeats if the input is invalid
#
####################################################

# termcolor needs to be installed via apt or pip
from termcolor import colored
a = False

# print with format
def p(x):
    print(colored('you entered:', 'yellow'), colored(x, 'cyan'))
    global a 
    a = False

while a == False:
    b = input('Enter a number, no decimals:')
    a = b.isdigit()
p(b)

while a == False:
    b = input('Enter a string, only a-z and A-Z letters allowed:')
    a = b.isalpha()
p(b)
while a == False:
    b = input('Enter a string, this time letters and digits are allowed:')
    a = b.isalnum()
p(b)
