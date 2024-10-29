#!/usr/bin/python3
#########################################################
# guess the card game      ##############################
# user will have three hints until the card is revealed #
#########################################################
import re, random #, sys
from termcolor import colored as c

# cards:
clubs   = chr(9827) 
diamonds = chr(9830) 
hearts  = chr(9829) 
spades= chr(9824) 

# init the cards deck
suits = ['C', 'D', 'H', 'S']
cardNumbers = ['A', '2', '3', '4', '5', '6', '7', 'J', 'Q', 'K']
suitColor = 'none yet'
hitSuit = hitColor = hitNumber = False

# User game vars
guessTries = 4

# pick a random card
cardNumber = random.choice(cardNumbers)
suit = random.choice(suits)

def displayCard():
    rows = ['', '', '', '','']
    rows[0] += '    ___ ' # top line of card
    rows[1] += '   |## |' 
    rows[2] += '   |###|   {}'.format(c('** GUESS THE CARD **', 'white'))
    rows[3] += '   |_##|      {} tries left'.format(c(guessTries, 'white'))
    rows[4] += ''
    for row in rows:
         print(c(row, 'green'))

def setCardColor():
    global suitColor
    if suit == 'H' or suit == 'D':
        suitColor = 'red'
    else:
        suitColor = 'cyan'

setCardColor()

def revealCard():
    mySuit = suit2Icon(suit)
    rows = ['', '', '', '','']
    rows[0] += '    ___  ' # top line of card
    rows[1] += '   |{} |'.format(c(cardNumber.ljust(2), suitColor))
    rows[2] += '   | {} |'.format(c(mySuit, suitColor))
    rows[3] += '   |_{}|'.format(c(cardNumber.rjust(2), suitColor))
    rows[4] += ''
    for row in rows:
         print(row)

displayCard()

# guess the card
def betCardNumber():
    global yourBetNumber  
    yourBetNumber = 'none yet' # must init every time
    myRegex = '^(A|J|Q|K|[2-7])$' # available inputs
    while not re.match(myRegex, yourBetNumber):
        yourBetNumber = input('guess the card number: (A, 2 to 7, J, Q or K)').upper()
def betCardSuit():
    global yourBetSuit  
    yourBetSuit = 'none yet' # must init every time
    myRegex = '^(H|D|S|C)$' # available inputs 
    while not re.match(myRegex, yourBetSuit):
        yourBetSuit = input('choose a suit: (H)earts, (D)iamonds, (S)pades or (C)lubs ').upper()

#####################################################################
#debug 
print(c('**************', 'red'), cardNumber, suit)
#####################################################################
#debug function
def pDebug():
    print(c('#DEBUG:', 'red'), 'yourBetNumber:', cardNum2Int(yourBetNumber), cardNumber,
          'yourBetSuit:', yourBetSuit,
          'suit:', suit, 'hitSuit:', hitSuit, 'hitNumber:', hitNumber )
#####################################################################

betCardNumber()
betCardSuit()

# convert card string to int
def cardNum2Int(i):
    if i == 'A':
        return 1
    elif i == 'J':
        return 10
    elif i == 'Q':
        return 11
    elif i == 'K':
        return 12
    else:
        return int(i)

# convert card string to word
def cardNum2Word(i):
    if i == 'A':
        return 'Ace'
    elif i == 'J':
        return 'Jack'
    elif i == 'Q':
        return 'Queen'
    elif i == 'K':
        return 'King'
    else:
        return i

# convert card suit to Icon
def suit2Icon(i):
    if i == 'C':
        return clubs
    elif i == 'D':
        return diamonds 
    elif i == 'H':
        return hearts
    elif i == 'S':
        return spades

# get card suit color
def suit2Color(i):
    if i == 'D' or i == 'H':
        return 'red'
    else:
        return 'cyan'

# convert card suit to full word
def suit2Word(i):
    if i == 'C':
        return 'Clubs'
    elif i == 'D':
        return 'Diamonds' 
    elif i == 'H':
        return 'Hearts'
    elif i == 'S':
        return 'Spades'

def yourBetWas():
    w = cardNum2Word(yourBetNumber)
    a = suit2Word(yourBetSuit)
    b = suit2Color(yourBetSuit)
    z = suit2Icon(yourBetSuit)
    print('your bet was', c(w, b), 'of', c(a, b), c(z, b))

def compareCardNumber(a, b):
    if a > b:
        return 'number should be bigger'
    elif a < b:
        return 'number should be smaller'
    else:
        return 'number is correct'

def compareColor(a, b):
    if (a == 'D' or a == 'H') and b == 'red':
        return 'color is right'
    elif (a == 'S' or a == 'C') and b == 'cyan':
        return 'color is right'
    else:
        return 'color is wrong'


def makeHints():
    global hitColor, hitNumber, hitSuit
    # check if color matches
    if (yourBetSuit == 'D' or yourBetSuit == 'H') and suitColor == 'red':
        hitColor = True
    elif (yourBetSuit == 'S' or yourBetSuit == 'C') and suitColor == 'cyan':
        hitColor = True
    # then check suit
    if yourBetSuit == suit:
        hitSuit = True
    # finally check the number
    x = cardNum2Int(cardNumber)
    y = cardNum2Int(yourBetNumber)
    if x == y:
        hitNumber = True

def calculateResult():
    global guessTries 
    global suitColor, yourBetSuit, hitColor, hitNumber, hitSuit, suit
    makeHints()
    guessTries -=1
    pDebug()
    y = cardNum2Int(cardNumber)
    z = cardNum2Int(yourBetNumber)
    if hitSuit == True and hitNumber == True:
        revealCard()
        yourBetWas()
        print(c('You hitted both suit and number. you totally WON!!! ', 
                'green', attrs=['blink', 'reverse']))
        guessTries =0
    elif hitSuit == True and hitNumber == False:
        displayCard()
        yourBetWas()
        print('Not bad. You hitted the suit but', 
              compareCardNumber(y,z)) 
        betCardNumber()
    elif hitSuit == False and hitNumber == True:
        displayCard()
        yourBetWas()
        print('Not bad. You hitted the number and missed the suit.')
        print('The card', compareColor(yourBetSuit, suitColor))
        betCardSuit()
    else: 
        displayCard()
        yourBetWas()
        print('Not even close. You missed both suit and number.')
        print('The card', compareColor(yourBetSuit, suitColor), 
              ', also', compareCardNumber(y, z)) 
        betCardNumber()
        betCardSuit()


while guessTries >= 1:
    calculateResult()

