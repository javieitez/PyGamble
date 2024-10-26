#!/usr/bin/python3

#######################################################
# game of blackjack
# User vs Computer: Deal cards up to a value of 21
#######################################################

import random, sys

# cards:
hearts  = chr(9829) 
diamonds = chr(9830) 
spades= chr(9824) 
clubs   = chr(9827) 
backSide = 'backside'
card = backSide

def displayCards(cards):
    global card
    rows = ['', '', '', '',]
    for i, card in enumerate(cards):
        rows[0] += ' ___  ' # top line of card
        #if card == backSide:
        rows[1] += '|## |'
        rows[2] += '|###|'
        rows[3] += '|_##|'
        for row in rows:
            print(row)

displayCards(card)
