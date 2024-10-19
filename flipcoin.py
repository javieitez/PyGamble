import random

coinSides = ['heads','tails']
headsCount = 0
tailsCount = 0

flipTimes = int(input('How many times do you want to flip the coin: '))

# Flip the coin as much times as previously specified
while flipTimes > 0:
    coinFlip = random.choice(coinSides)
    print(coinFlip)
    if coinFlip == 'heads':
        headsCount += 1
    else:
        tailsCount += 1 
    print(headsCount, 'heads,', tailsCount, 'tails')
    flipTimes -=1

# Show some funny stats about the flips
print('Coin was flipped', headsCount+tailsCount, 'times')

def showMeStats(a, b, whatMore):
    countDiff = a-b
    print(countDiff, 'more', whatMore)
    print(round(( 100 * countDiff )/a), '% more', whatMore)

if headsCount > tailsCount:
    showMeStats(headsCount, tailsCount, 'heads')
else:
    showMeStats(tailsCount, headsCount, 'tails')
