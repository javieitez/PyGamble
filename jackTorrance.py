#######################################################
# Print a sentence, indefinitley, with random 
# indentations and styles
#######################################################
w = 'All Work And No Play Makes Jack A Dull Boy'
x = 9999
# termcolor needs to be installed via apt or pip
from termcolor import colored as c
import random as r
import time as t

aa = 55
interline = '*' * aa
randCharz = ['*', '+', '-', '_', '¡']

# type one char at a time
# type it at slightly different speeds to look a bit human
def p(a):
    for char in a:
        q = [.011, .066, .022, .055] 
        rtime = r.choice(q)
        print(char, end='', flush=True)
        t.sleep(rtime)

while x > 0:
    # generate random lines to choose from
    myStylz= [w.capitalize(), w.lower(), w.upper(), w.rjust(aa), w.ljust(aa), 
              w.center(aa), w.swapcase(), r.choice(randCharz) * aa, '\n']
    z = str(r.choice(myStylz)) # choose a random style
    aa = int(r.randint(30, 80)) # randomize the justification value
    p(z) # type the sentence
    print('\r') # add a line break
    x -=1
