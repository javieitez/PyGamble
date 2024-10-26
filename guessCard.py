#!/usr/bin/python3
#######################################################
# guess the card game
#######################################################

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

# pick a random card
cardNumber = random.choice(cardNumbers)
suit = random.choice(suits)
yourBetIcon = yourBetSuit = yourBetNumber = 'none yet'

def displayCard():
    rows = ['', '', '', '','']
    rows[0] += ' ___ ' # top line of card
    rows[1] += '|## |' 
    rows[2] += '|###|'
    rows[3] += '|_##|'
    rows[4] += ''
    for row in rows:
         print(c(row, 'green'))

def revealCard():
    if suit == hearts or suit == diamonds:
        suitColor = 'red'
    else:
        suitColor = 'cyan'
    rows = ['', '', '', '','']
    rows[0] += ' ___  ' # top line of card
    rows[1] += '|{} |'.format(c(cardNumber.ljust(2), suitColor))
    rows[2] += '| {} |'.format(c(suit, suitColor))
    rows[3] += '|_{}|'.format(c(cardNumber.rjust(2), suitColor))
    rows[4] += ''
    for row in rows:
         print(row)

displayCard()

# guess the card
def makeYourBet():
    global yourBetSuit, yourBetNumber  
    myRegex = '(A|J|Q|K|[2-7])'
    while not re.match(myRegex, yourBetNumber):
        yourBetNumber = input('guess the card number: (A, 2 to 7, J, Q or K)')
        yourBetNumber = yourBetNumber.upper() # go upppercase
    myRegex = '(H|D|S|C)'
    while not re.match(myRegex, yourBetSuit):
        yourBetSuit = input('choose a suit: (H)earts, (D)iamonds, (S)pades or (C)lubs ')
        yourBetSuit = yourBetSuit.upper() # go upppercase

makeYourBet()

# turn your keystrokes into readable words
def yourBetWas():
    global yourBetIcon
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
    elif yourBetSuit == 'D':
        a, b, yourBetIcon = 'Diamonds', 'red', diamonds
    elif yourBetSuit == 'S':
        a, b, yourBetIcon = 'Spades', 'cyan', spades
    elif yourBetSuit == 'C':
        a, b, yourBetIcon = 'Clubs', 'cyan', clubs
    print('your bet was', c(w, b), 'of', c(a, b), c(yourBetIcon, b))

yourBetWas()
revealCard()
# calculate results
if yourBetNumber == cardNumber and yourBetIcon == suit:
    print(c('You hitted both suit and number. you totally WON!!!', 'red', attrs=['blink']))
elif yourBetNumber == cardNumber: 
    print(c('Not bad. You hitted the number and missed the suit', 'green', attrs=['blink']))
elif yourBetIcon == suit:
    print(c('Not bad. You hitted the suit and missed the number', 'green', attrs=['blink']))
else:
    print("You missed both suit and number. Not even close")

