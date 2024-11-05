#!/usr/bin/python3
#########################################################
# TicTacToe                ##############################
#########################################################
import random as r
from termcolor import cprint as p

yourSign = 'X'
compSign = 'O'

# build matrix data
t =	   [[' ', ' ', ' '],
        [' ', ' ', ' '],
	    [' ', ' ', ' ']] 
# build matrix representation, one cell per variable
A1 = '| {} '.format(t[0][0])
A2 = '| {} '.format(t[0][1])
A3 = '| {} |'.format(t[0][2])
B1 = '| {} '.format(t[1][0])
B2 = '| {} '.format(t[1][1])
B3 = '| {} |'.format(t[1][2])
C1 = '| {} '.format(t[2][0])
C2 = '| {} '.format(t[2][1])
C3 = '| {} |'.format(t[2][2])

def pMatrix():
	print(A1+A2+A3+'\n'+B1+B2+B3+'\n'+C1+C2+C3)

def placeMove(z):
		global t
		if z =='1' or z =='2' or z =='3':
			t[0][z] = 'x' #yourSign
		
# force user input 1 to 9
def makeMove():
	a = False
	while a == False:
		b = input('Your move (1-9): ')
		a = b.isdigit() and int(b)>0 and int(b)<9
	placeMove(int(b))

pMatrix()
makeMove()
pMatrix()
