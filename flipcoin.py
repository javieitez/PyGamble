##################################################################
# 	Flip Coin 						##  github.com/javieitez   ##
#
# Exercise on randomness: flip a coin many times, 
# then generate some facts on the results
##################################################################

# init some defaults
from termcolor import colored
import random
coinSides = ['heads','tails']
headsCount = 0
tailsCount = 0
prevFlip = 'nothing'
consecutiveHeads = 0
consecutiveTails = 0
maxConsecutiveHeads = 0
maxConsecutiveTails = 0

a = False

# keep track of consecutive matches
def checkConsecutive():
    global consecutiveTails, consecutiveHeads
    if coinFlip == prevFlip == 'heads':
        consecutiveHeads += 1
        singConsecutive(consecutiveHeads, 'heads')
    elif coinFlip == prevFlip == 'tails':
        consecutiveTails += 1
        singConsecutive(consecutiveTails, 'tails')
    else:
        consecutiveHeads = 1
        consecutiveTails = 1

# keep track of max consecutive matches
def recordMaxConsecutives():
    global consecutiveTails, consecutiveHeads
    global maxConsecutiveTails, maxConsecutiveHeads
    if maxConsecutiveHeads < consecutiveHeads:
        maxConsecutiveHeads = consecutiveHeads
    elif maxConsecutiveTails < consecutiveTails:
        maxConsecutiveTails = consecutiveTails

# blink if two or more consecutive matches
def singConsecutive(a, b):
    if a > 5:
        print(a, 'consecutive', b, '!!!')

# better color output
def p(a):
    if a == 'heads':
        print(colored(a, 'yellow'))
    elif a == 'tails':
        print(colored(a, 'cyan'))
    else:
        print(colored(a, 'green'))

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
        checkConsecutive()
    else:
        tailsCount += 1 
        checkConsecutive()
    flipTimes -=1
    # update counters
    recordMaxConsecutives()
    prevFlip = coinFlip

p('*********************')
# Show some funny stats about the flips
print('Coin was flipped', headsCount+tailsCount, 'times')
print(headsCount, 'heads,', tailsCount, 'tails')

p('*********************')
def showMeStats(a, b, whatMore):
    countDiff = a-b
    print(countDiff, 'more', whatMore)
    print((100*countDiff)/a, '% more', whatMore)

if headsCount > tailsCount:
    showMeStats(headsCount, tailsCount, 'heads')
else:
    showMeStats(tailsCount, headsCount, 'tails')
p('*********************')
print('Maximum number of consecutive heads:', maxConsecutiveHeads)
print('Maximum number of consecutive tails:', maxConsecutiveTails)
