#!/usr/bin/python3
#########################################################
# print colored cards      		# github.com/javieitez #
# functions to print a reversed and a revealed cards    
# using colored output.
# The cards function can be used in other programs  
#########################################################
from termcolor import colored as c
import random 
# cards:
clubs   = chr(9827) 
diamonds = chr(9830) 
hearts  = chr(9829) 
spades= chr(9824)
blackSuitColor = 'grey'
redSuitColor = 'red'
cardNumbers = ['A', '2', '3', '4', '5', '6', '7', 'J', 'Q', 'K']
cardSuits = [clubs, diamonds, hearts, spades]

def reverseCard():
	
    cardRev = c(' ', 'green', 'on_green')
    cardDeco = c('#', 'grey', 'on_green')
    print('''	
    {}{}{}{}{} 
    {}{}{}{}{}
    {}{}{}{}{}    
		'''.format(cardRev, cardDeco, cardDeco, cardDeco, cardRev, 
			cardRev, cardDeco, cardDeco, cardDeco,cardRev, 
			cardRev, cardDeco, cardDeco,cardDeco, cardRev ))
	

def displayCard(num, suit):
	if suit == hearts or suit == diamonds:
		suitColor = redSuitColor
	else:
		suitColor = blackSuitColor
	bgColor = 'on_white'
	cardSign = c(num, suitColor, bgColor)
	cardBlank = c(' ', 'white', bgColor)
	cardSuit = c(suit, suitColor, bgColor)
	print('''
    {}{}{}{}{} 
    {}{}{}{}{}
    {}{}{}{}{}    
	'''.format(cardBlank, cardSign, cardBlank, cardBlank, cardBlank,
			cardBlank, cardBlank, cardSuit, cardBlank, cardBlank,
			cardBlank, cardBlank, cardBlank, cardSign, cardBlank))

# DEMO: Display a random card
x = random.choice(cardNumbers)
y = random.choice(cardSuits)
print("Here's your card, hidden")
reverseCard()
print("Here's your card, revealed")
displayCard(x, y)
