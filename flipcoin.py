# init some defaults
from termcolor import colored
import random
coinSides = ['heads','tails']
headsCount = 0
tailsCount = 0
a = False

# better color output
def p(a):
    if a == 'heads':
        print(colored(a, 'yellow'))
    else:
        print(colored(a, 'cyan'))

# force the user to input an integer
while a == False:
    b = input('How many times do you want to flip the coin: ')
    a = b.isdigit()
flipTimes = int(b) 

# Flip the coin as much times as previously specified
while flipTimes > 0:
    coinFlip = random.choice(coinSides)
    p(coinFlip)
    if coinFlip == 'heads':
        headsCount += 1
    else:
        tailsCount += 1 
    flipTimes -=1

# Show some funny stats about the flips
print('Coin was flipped', headsCount+tailsCount, 'times')
print(headsCount, 'heads,', tailsCount, 'tails')

def showMeStats(a, b, whatMore):
    countDiff = a-b
    print(countDiff, 'more', whatMore)
    print((100*countDiff)/a, '% more', whatMore)

if headsCount > tailsCount:
    showMeStats(headsCount, tailsCount, 'heads')
else:
    showMeStats(tailsCount, headsCount, 'tails')
