#!/usr/bin/python3
############################################################
# Jack Torrance text generator     ## github.com/javieitez #
#
# Print a sentence, indefinitley, with random 
# indentations and styles
############################################################
w = 'All Work And No Play Makes Jack A Dull Boy'
x = 99999 # not actually endless, just so many times
import random as r
import time as t

aa = 55
randCharz = ['*', '+', '-', '_', '¡', '#']

# type one char at a time
# type it at slightly different speeds to look a bit human
def p(a):
    for char in a:
        q = [.011, .044, .022, .055] 
        rtime = r.choice(q)
        print(char, end='', flush=True)
        t.sleep(rtime)

while x > 0:
    # generate the sentence with different styles, also generate charlines and line breaks
    myStylz= [w.capitalize(), w.lower(), w.upper(), w.rjust(aa), 
              w.center(aa), w.swapcase(), r.choice(randCharz) * aa, '\n']
    # then choose from the previously generated values
    z = str(r.choice(myStylz)) # choose a random style
    aa = int(r.randint(30, 80)) # randomize the justification value
    p(z) # type the sentence
    print('\r') # add a line break
    x -=1
