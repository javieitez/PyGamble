#!/usr/bin/python3
#########################################################
# TicTacToe                ##  github.com/javieitez    ##
#
# Unlike other python based TicTacToe games, this one
# plays real Human vs Computer. The computer checks for
# potential 3s instead of just placing random movements 
#########################################################
import random as r

player1 = 'Human'
player2 = 'Computer'
p1Sign = 'X'
p2Sign = 'O'
currentPlayer = ''
# build matrix data
t =	   [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' '] 
# keep move history
tHistory = []
# keep track of unused cells
tFree = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# all possible wins
validCombis = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[6,4,2]]
movesCount = 0
p1Prompt = 'Your move, [1-9]: '
p2Prompt = "Computer's move"
myIntro = '''
Classic TicTacToe game. 
Try to place 3 on the same line.

Press [H] for Help
'''
myHelp ='''
Place your move by using the  
following number keys

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

'''
print(myIntro)

def potential3(z, y):
	if z.count(y) == 2 and z.count(' ') == 1: # 2 equals + blank  
		return True

def validateLine(a, b, c):
	if t[a]==t[b] and t[a]==t[c] and t[a]!=' ' :
		return True
		
def checkLine():
	global movesCount
	for a in validCombis:
		if validateLine(a[0],a[1],a[2]) == True:
			print(currentPlayer, 'wins')
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

def calcMove(mySign):	
	global t
	for i in validCombis:
		z = []
		for y in i:
			z.extend(t[y])
			if len(z) == 3 and potential3(z, mySign) == True:
				myCell = i[z.index(' ')] +1 # -1 later
				return myCell
	myCell = 10
	return myCell

def calcMovePriority():
	myCell = calcMove(p2Sign) # p2 potential row first
	if myCell == 10:
		myCell = calcMove(p1Sign) # then check for p1
		if myCell == 10:
			myCell = r.choice(tFree) # if nothing found, go random
	return myCell

def placeMove(z):
		global currentPlayer, t, tHistory, movesCount, tFree
		if z == player2:
			currentPlayer = player2
			x = p2Sign
			z = calcMovePriority()  #r.choice(tFree)
		else:
			x = p1Sign
			currentPlayer = player1
		tHistory.append(z)
		t[z-1] = x
		if z in tFree:
			tFree.remove(z)
		movesCount += 1

# force user input 1 to 9
def makeMove():
	global p1Prompt
	a = False
	while a == False:
		b = input(p1Prompt)
		if b.upper() == 'H':
			print(myHelp) 
		elif b.isdigit() and int(b) in tHistory: # check if move has already been made
			print('Already taken!')
		a = b.isdigit() and int(b)>0 and int(b)<=9 and int(b) not in tHistory
	placeMove(int(b))

# Let's go!
pMatrix()
while movesCount < 9:
	makeMove()
	pMatrix()
	checkLine()
	if movesCount < 9: # unless p1 has won
		print(p2Prompt)
		placeMove(player2)
		pMatrix()
		checkLine()
print('Game Over!')
