import random

coinSides = ['heads','tails']
headsCount = 0
tailsCount = 0

flipTimes = int(input('How many times do you want to flip the coin: '))

while flipTimes > 0:
    coinFlip = random.choice(coinSides)
    print(coinFlip)
    if coinFlip == 'heads':
        headsCount += 1
    else:
        tailsCount += 1 
    print(headsCount, 'heads,', tailsCount, 'tails')
    flipTimes -=1
print('Coin was flipped', headsCount+tailsCount, 'times')

if headsCount > tailsCount:
    countDiff = headsCount-tailsCount
    print(countDiff, 'more heads')
    print(round(( 100 * countDiff )/headsCount), '% more heads')
else:
    countDiff = tailsCount-headsCount
    print(countDiff, 'more tails')
    print(round(( 100 * countDiff )/tailsCount), '% more tails')

