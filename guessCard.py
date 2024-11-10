#!/usr/bin/python3
#########################################################
# guess the card game      ##############################
# user will have three hints until the card is revealed #
#########################################################
import re, random 
from termcolor import colored as c

# cards:
clubs   = chr(9827) 
diamonds = chr(9830) 
hearts  = chr(9829) 
spades= chr(9824)
blackSuitColor = 'grey'
redSuitColor = 'red'


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

print('''      
        ** GUESS THE CARD **''')

def displayCard():
    cardRev = c(' ', 'green', 'on_green')
    cardDeco = c('#', 'grey', 'on_green')
    print('''	
    {}{}{}{}{} 
    {}{}{}{}{}
    {}{}{}{}{}    {} tries left'
		'''.format(cardRev, cardDeco, cardDeco, cardDeco, cardRev, 
			cardRev, cardDeco, cardDeco, cardDeco,cardRev, 
			cardRev, cardDeco, cardDeco,cardDeco, cardRev, c(guessTries, 'white')))

def setCardColor():
    global suitColor
    if suit == 'H' or suit == 'D':
        suitColor = redSuitColor
    else:
        suitColor = blackSuitColor

setCardColor()

def revealCard(num, suit):
	mySuit = suit2Icon(suit)
	if mySuit == hearts or mySuit == diamonds:
		suitColor = redSuitColor
	else:
		suitColor = blackSuitColor
	bgColor = 'on_white'
	cardSign = c(num, suitColor, bgColor)
	cardBlank = c(' ', 'white', bgColor)
	cardSuit = c(mySuit, suitColor, bgColor)
	print('''
    {}{}{}{}{} 
    {}{}{}{}{}
    {}{}{}{}{}    
	'''.format(cardBlank, cardSign, cardBlank, cardBlank, cardBlank,
			cardBlank, cardBlank, cardSuit, cardBlank, cardBlank,
			cardBlank, cardBlank, cardBlank, cardSign, cardBlank))

displayCard()
# colored background card characters
def cc(txt, color):
    return c(txt, color, 'on_white')

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
        print('(H)', cc(hearts, redSuitColor), '(S)', cc(spades, blackSuitColor), 
              '(D)', cc(diamonds, redSuitColor), '(C)', cc(clubs, blackSuitColor)) 
        yourBetSuit = input('choose a suit:').upper()

#####################################################################
#debug 
#print(c('**************', redSuitColor), cardNumber, suit)
#####################################################################
#debug function
#def pDebug():
#    print(c('#DEBUG:', redSuitColor), 'Number:', cardNum2Int(yourBetNumber), 'vs', cardNumber,
#          'Suit:', yourBetSuit,
#          'vs', suit, 'hitSuit:', hitSuit, 'hitNumber:', hitNumber )
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
        return redSuitColor
    else:
        return blackSuitColor

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
    print('your bet was', cc(w, b), 'of', cc(a, b), cc(z, b))

def compareCardNumber(a, b):
    if a > b:
        return 'number should be bigger'
    elif a < b:
        return 'number should be smaller'
    else:
        return 'number is correct'

def compareColor(a, b):
    if (a == 'D' or a == 'H') and b == redSuitColor:
        return 'color is right'
    elif (a == 'S' or a == 'C') and b == blackSuitColor:
        return 'color is right'
    else:
        return 'color is wrong'


def makeHints():
    global hitColor, hitNumber, hitSuit
    # check if color matches
    if (yourBetSuit == 'D' or yourBetSuit == 'H') and suitColor == redSuitColor:
        hitColor = True
    elif (yourBetSuit == 'S' or yourBetSuit == 'C') and suitColor == blackSuitColor:
        hitColor = True
    # then check suit
    if yourBetSuit == suit:
        hitSuit = True
    # finally check the number
    x = cardNum2Int(cardNumber)
    y = cardNum2Int(yourBetNumber)
    if x == y:
        hitNumber = True

winLine = c('Right suit and number. You win.', 
                'green', attrs=['reverse'])
loseLine = c('No more tries left. You lose... :(',
             redSuitColor, attrs=['reverse'])

while guessTries >=1:
    bottomLine = loseLine
    makeHints()
    y = cardNum2Int(cardNumber)
    z = cardNum2Int(yourBetNumber)
    if hitSuit == True and hitNumber == True:
        bottomLine = winLine
        guessTries = 0
        break
    if hitSuit == True and hitNumber == False:
        guessTries -=1
        displayCard()
        yourBetWas()
        print('The suit is right but', 
              compareCardNumber(y,z)) 
        betCardNumber()
    elif hitSuit == False and hitNumber == True:
        guessTries -=1
        displayCard()
        yourBetWas()
        print('Right number. The suit is incorrect.')
        print('The suit', compareColor(yourBetSuit, suitColor))
        betCardSuit()
    else: 
        guessTries -=1
        displayCard()
        yourBetWas()
        b = suit2Color(yourBetSuit)
        print('You missed both suit and number.')
        print('The suit', compareColor(yourBetSuit, suitColor), 
              ',also', compareCardNumber(y, z)) 
        betCardNumber()
        betCardSuit()


# needs one final calculation 
makeHints()
if hitSuit == True and hitNumber == True:
    bottomLine = winLine

yourBetWas()
revealCard(cardNumber, suit)
print(bottomLine)
