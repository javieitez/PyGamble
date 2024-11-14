#!/usr/bin/python3
############################################################
# Quiniela 1X2 simulator      ##  github.com/javieitez    ##
#
# Quiniela is a Sports betting game popular in Spain
# The bets are based on 15 football matches from the 
# national league. 
#
# Each row places a bet with 1, X or 2 
# (1) Local team wins
# (X) Ties
# (2) Visitor team wins
# 
# The program makes 15 bets and runs indefinitely until 
# the chosen combination wins
############################################################
import random

#quiniela = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
quiniela = ['2', '1', '2', '1', '1', 'X', 'X', '2', 'X', '1', '2', 'X', '1', 'X', '2'] #hardcoded for debug
currentWeek = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
bets = ['1', 'X', '2']
myRange= range(len(quiniela))
tM= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #counter for 0s, 1s, 2s, etc... must be one place longer
weeks = years = currentMatches = 0

def sorteo():
	global currentWeek
	for i in myRange:
		currentWeek[i] = random.choice(bets)

def compareResults():
	global tM, weeks, years, currentMatches
	matches =0
	for i in myRange:
		if currentWeek[i] == quiniela[i]:
			matches +=1
		currentMatches = matches
		tM[currentMatches] +=1
	weeks +=1
	years = (weeks*7)//365 # weeks to years, not considering leap years (this is a fun prog)
'''
# force user input 1, X or 2
print('Chooose 15 bets: 1, X or 2. ')
for i in myRange:
	a = False
	while a == False:
		myStr= str(i +1) + ' of ' + str(myRange[-1] + 1) + ': '
		x = input(myStr)
		if x != '1' and x.upper() != 'X' and x != '2': 
			print('must be 1, X or 2. Not', x.upper())
			x = '0'
		a = x == '1' or x.upper() == 'X' or x == '2'
	currentWeek[i]= x.upper()
'''
print('Your bet:\n', quiniela)
print('------------------------------------------------\n\n\n\n\n')
print(f'\033[?25l', end='')#hide cursor, POSIX only

def pStats():
	print(f'\033[F\033[F\033[F\033[F\033[FThis week:\n', currentWeek,
			'\ncurrent:', currentMatches, 'Weeks:', weeks, 'Years:', years, 
			'\nMatches: (0)', tM[0],'(1)', tM[1],'(2)', tM[2], '(3)', tM[3],'(4)', tM[4],'(5)', tM[5],
			'(6)', tM[6],'\n(7)', tM[7],'(8)', tM[8],'(9)', tM[9],'(10)', tM[10],'(11)', tM[11],'(12)', 
			tM[12],'(13)', tM[13], '(14)', tM[14], end=' ')
	if isWin:
		print('You WON!!!            ')
	else:
		print('No 15s yet...')

isWin = False

while isWin == False:	
	sorteo()
	compareResults()
	isWin= quiniela == currentWeek
	pStats()

print(f'\033[?25h', end='')#bring cursor back, POSIX only
