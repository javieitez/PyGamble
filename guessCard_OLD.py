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
    global suit, suitColor
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
    yourBetNumber = 'none yet'
    myRegex = '^(A|J|Q|K|[2-7])$' # available inputs
    while not re.match(myRegex, yourBetNumber):
        yourBetNumber = input('guess the card number: (A, 2 to 7, J, Q or K)').upper()
def betCardSuit():
    global yourBetSuit  
    myRegex = '^(H|D|S|C)$' # available inputs 
    while not re.match(myRegex, yourBetSuit):
        yourBetSuit = input('choose a suit: (H)earts, (D)iamonds, (S)pades or (C)lubs ').upper()

#####################################################################
#debug
print(c('**************', 'red'), cardNumber, suit)
#####################################################################

betCardNumber()
betCardSuit()

# turn your keystrokes into readable words
def yourBetWas():
    global yourBetNumber, yourBetIcon, yourBetSuit 
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
    #print('your bet was', c(w, b), 'of', 
    #      c(a, b), c(yourBetIcon, b))

# convert card string to int
def convertCardNumber(i):
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

def compareCardNumber(a, b):
    if a > b:
        return 'number should be bigger'
    elif a < b:
        return 'number should be smaller'
    else:
        return 'number is correct'

def compareColor(a, b):
    if (a == diamonds or a == hearts) and b == 'red':
        return 'color is right'
    elif (a == spades or a == clubs) and b == 'cyan':
        return 'color is right'
    else:
        return 'color is wrong'


def makeHints():
    global suitColor, yourBetSuit, hitColor, hitNumber, hitSuit, suit
    # check if color matches
    if (yourBetSuit == diamonds or yourBetSuit == hearts) and suitColor == 'red':
        hitColor = True
    elif (yourBetSuit == spades or yourBetSuit == clubs) and suitColor == 'cyan':
        hitColor = True
    # then check suit
    if yourBetSuit == suit:
        hitSuit = True
    # finally check the number
    x = convertCardNumber(cardNumber)
    y = convertCardNumber(yourBetNumber)
    if x == y:
        hitNumber = True

def calculateResult():
    global guessTries 
    global suitColor, yourBetSuit, hitColor, hitNumber, hitSuit, suit
    yourBetWas()
    makeHints()
    ## # # # # # # # # # # # #  dbug
    print(c('DEBUG:', 'red'), hitSuit, hitNumber, hitColor, suit, yourBetSuit)
    ## # # # # # # # # # # # # #  
    guessTries -=1
    if hitSuit == True and hitNumber == True:
        revealCard()
        print(c('You hitted both suit and number. you totally WON!!! ', 
                'green', attrs=['blink', 'reverse']))
        guessTries =0
    elif hitSuit == True and hitNumber == False:
        #displayCard()
        print('Not bad. You hitted the suit but', compareCardNumber(cardNumber, yourBetNumber)) 
        betCardNumber()
    elif hitSuit == False and hitNumber == True:
        #displayCard()
        print('Not bad. You hitted the number and missed the suit.')
        print('The card', compareColor(yourBetSuit, suitColor))
        betCardSuit()
    else: 
        #displayCard()
        print('Not even close. You missed both suit and number.')
        print('The card', compareColor(yourBetSuit, suitColor), 
              ', also', compareCardNumber(cardNumber, yourBetNumber), cardNumber, yourBetNumber) 
        betCardNumber()
        betCardSuit()


while guessTries >= 1:
    calculateResult()

'''
# give the user a hint about hits and misses
# and calculate next round
def giveHints():
    global suitColor, yourBetSuit, hitColor, hitNumber, hitSuit, suit
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
    if yourBetSuit == suit:
        ph('suit', suit, 'right')
        hitSuit = True
    else:
        ph('suit', yourBetSuit, 'wrong')
    x = convertCardNumber(cardNumber)
    y = convertCardNumber(yourBetNumber)
    if x > y:
        print('number is bigger than', y)
    elif x < y:
        print('number is smaller than', y)
    else:
        print('number is exactly', y)
        hitNumber = True

# print hint function
def ph(a, b, c):
    myStr = a + ' ' + b + ' is ' + c
    print(myStr)

'''
