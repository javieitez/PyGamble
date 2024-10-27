#!/usr/bin/python3
#########################################################
# guess the card game      ##############################
# user will have three hints until the card is revealed #
#########################################################

import re, random, sys
from termcolor import colored as c

# cards:
hearts  = chr(9829) 
diamonds = chr(9830) 
spades= chr(9824) 
clubs   = chr(9827) 

# init the cards deck
suits = [hearts, diamonds, spades, clubs]
cardNumbers = ['A', '2', '3', '4', '5', '6', '7', 'J', 'Q', 'K']
suitColor = yourBetIcon = yourBetSuit = yourBetNumber = 'none yet'
hitSuit = hitColor = hitNumber = False

# pick a random card
cardNumber = random.choice(cardNumbers)
suit = random.choice(suits)

def displayCard():
    rows = ['', '', '', '','']
    rows[0] += '    ___ ' # top line of card
    rows[1] += '   |## |' 
    rows[2] += '   |###|   GUESS THE CARD'
    rows[3] += '   |_##|'
    rows[4] += ''
    for row in rows:
         print(c(row, 'green'))

def setCardColor():
    global suitColor
    if suit == hearts or suit == diamonds:
        suitColor = 'red'
    else:
        suitColor = 'cyan'

setCardColor()

def revealCard():
    rows = ['', '', '', '','']
    rows[0] += '    ___  ' # top line of card
    rows[1] += '   |{} |'.format(c(cardNumber.ljust(2), suitColor))
    rows[2] += '   | {} |'.format(c(suit, suitColor))
    rows[3] += '   |_{}|'.format(c(cardNumber.rjust(2), suitColor))
    rows[4] += ''
    for row in rows:
         print(row)

displayCard()

# guess the card
def betCardNumber():
    global yourBetNumber  
    myRegex = '^(A|J|Q|K|[2-7])$' # available inputs
    while not re.match(myRegex, yourBetNumber):
        yourBetNumber = input('guess the card number: (A, 2 to 7, J, Q or K)').upper()
def betCardSuit():
    global yourBetSuit  
    myRegex = '^(H|D|S|C)$' # available inputs 
    while not re.match(myRegex, yourBetSuit):
        yourBetSuit = input('choose a suit: (H)earts, (D)iamonds, (S)pades or (C)lubs ').upper()

#debug
print(cardNumber, suit)

betCardNumber()
betCardSuit()

# turn your keystrokes into readable words
def yourBetWas():
    global yourBetIcon, yourBetSuit 
    if yourBetNumber == 'A':
        w = "Ace"
    elif yourBetNumber == 'J':
        w = "Jack"
    elif yourBetNumber == 'Q':
        w = "Queen"
    elif yourBetNumber == 'K':
        w = "King"
    else:
        w = yourBetNumber
    if yourBetSuit == 'H':
        a, b, yourBetIcon = 'Hearts', 'red', hearts
        yourBetSuit = hearts
    elif yourBetSuit == 'D':
        a, b, yourBetIcon = 'Diamonds', 'red', diamonds
        yourBetSuit = diamonds
    elif yourBetSuit == 'S':
        a, b, yourBetIcon = 'Spades', 'cyan', spades
        yourBetSuit = spades
    elif yourBetSuit == 'C':
        a, b, yourBetIcon = 'Clubs', 'cyan', clubs
        yourBetSuit = clubs
    print('your bet was', c(w, b), 'of', 
          c(a, b), c(yourBetIcon, b))

# print hint function
def ph(a, b, c):
    myStr = a + ' ' + b + ' is ' + c
    print(myStr)

# convert card string to int
def convertCardNumber(i):
    if i == 'A':
        return 1
    elif i == '2':
        return 2
    elif i == '3':
        return 3
    elif i == '4':
        return 4
    elif i == '5':
        return 5
    elif i == '6':
        return 6
    elif i == '7':
        return 7
    elif i == 'J':
        return 10
    elif i == 'Q':
        return 11
    elif i == 'K':
        return 12

# give the user a hint about hits and misses
def giveHints():
    if (yourBetSuit == diamonds or yourBetSuit == hearts) and suitColor == 'red':
        ph('color', suitColor, 'right')
        hitColor = True
    elif (yourBetSuit == spades or yourBetSuit == clubs) and suitColor == 'cyan':
        ph('color', suitColor, 'right')
        hitColor = True
    else:
        if suitColor == 'cyan':
            z = 'red'
        else:
            z = 'cyan'
        ph('color', z, 'wrong')
        hitColor = False
    if yourBetSuit == suit:
        ph('suit', suit, 'right')
    else:
        ph('suit', suit, 'wrong')
    x = convertCardNumber(cardNumber)
    y = convertCardNumber(yourBetNumber)
    if x > y:
        print('number is bigger than', y)
    elif x < y:
        print('number is smaller than', y)
    else:
        print('number is exactly', y)

yourBetWas()

giveHints()
revealCard()
# calculate results
if yourBetNumber == cardNumber and yourBetIcon == suit:
    print(c('You hitted both suit and number. you totally WON!!! ', 
            'green', attrs=['blink', 'reverse']))
elif yourBetNumber == cardNumber: 
    print(c('Not bad. You hitted the number and missed the suit. ', 
            'green', attrs=['reverse']))
elif yourBetIcon == suit:
    print(c('Not bad. You hitted the suit and missed the number. ', 
            'green', attrs=['reverse']))
else:
    print("You missed both suit and number. Not even close")

