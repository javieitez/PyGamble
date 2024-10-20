##################################################
#
#         Demonstration of the different 
#         string methods
#
##################################################

# termcolor needs to be installed via apt or pip
from termcolor import colored

# print with 2 different formats
def pr(a):
    print(colored(a, 'yellow'))
def p(a):
    print(colored(a, 'cyan'))

# define a line of text to work with
#myStr = 'Lorem Ipsum Dolor sit amet'
myStr = 'all work and no play makes jack a dull boy'

# let's go!
p('capitalize() makes the first Character uppercase:')
pr(myStr.capitalize())

p('lower/upper makes everything lower or uppercase:')
pr(myStr.lower())
pr(myStr.upper())

p('Title Makes Every Word Start With Uppercase')
pr(myStr.title())

p('Combined with swapcase, it does that crazy thing')
myTitle = myStr.title()
pr(myTitle.swapcase())

p('count("a") returns the number of times "a" appears')
pr(myStr.count('a'))

p('center/rjust/ljust justifies to the right or left')
pr(myStr.rjust(52))
