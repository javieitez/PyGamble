#!/usr/bin/python3
#########################################################
# TicTacToe                ##############################
#########################################################
import random as r
from termcolor import cprint as p

yourSign = 'X'
compSign = 'O'
# build matrix data
t =	   [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' '] 
# keep move history
tHistory = []
tFree = [1, 2, 3, 4, 5, 6, 7, 8, 9]
movesCount = 0
myPrompt = 'Your move, [1-9] or [H]elp: '
myHelp ='''
Classic TicTacToe game. 

Place your move by using the 
following number keys

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

'''

def validateLine(a, b, c):
	if t[a]==t[b] and t[a]==t[c] and t[a]!=' ' :
		return True
		
def checkLine():
	global movesCount
	validCombis = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[6,4,2]]
	for a in validCombis:
		if validateLine(a[0],a[1],a[2]) == True:
			print('You win!!')
			movesCount = 9 
	
# build matrix representation, one cell per variable
def pMatrix(): 
	A1 = '| {} '.format(t[0])
	A2 = '| {} '.format(t[1])
	A3 = '| {} |'.format(t[2])
	B1 = '| {} '.format(t[3])
	B2 = '| {} '.format(t[4])
	B3 = '| {} |'.format(t[5])
	C1 = '| {} '.format(t[6])
	C2 = '| {} '.format(t[7])
	C3 = '| {} |'.format(t[8])
	print('\n'+A1+A2+A3+'\n'+B1+B2+B3+'\n'+C1+C2+C3+'\n')
	
def compMove():
	global t, tHistory, movesCount, tFree
	z = r.choice(tFree)
	t[z-1] = compSign
	tHistory.append(z)
	tFree.remove(z)
	movesCount += 1
	
def placeMove(z):
		global t, tHistory, movesCount, tFree
		tHistory.append(z)
		t[z-1] = yourSign
		tFree.remove(z)
		movesCount += 1

# force user input 1 to 9
def makeMove():
	global myPrompt
	a = False
	while a == False:
		b = input(myPrompt)
		if b.upper() == 'H':
			print(myHelp) 
			myPrompt = 'Your move [1-9]: '
		elif b.isdigit() and int(b) in tHistory:
			print('Already taken!')
		a = b.isdigit() and int(b)>0 and int(b)<=9 and int(b) not in tHistory
	placeMove(int(b))

# Let's go!
pMatrix()
while movesCount < 9:
	makeMove()
	pMatrix()
	checkLine()
	compMove()
	pMatrix()
	checkLine()
	print('Taken:', tHistory, 'Free:', tFree) #DEBUG
