#!/usr/bin/python3
#########################################################
# Lotto 6/49 simulator     ##  github.com/javieitez    ##
#
# Choose 6 numbers, then simulate a weekly lotto
# drawing that will run until the chosen combination wins 
#########################################################
import random

lottoWeek= [0, 0, 0, 0, 0, 0]
lottoCombi= [0, 0, 0, 0, 0, 0]
#lottoCombi= [7, 12, 26, 30, 41, 48] # hardcoded for debug
myRange= range(len(lottoCombi))
drawsPerWeek =3
totalDraws = drawsCount= weeks= years= 0
tM= [0, 0, 0, 0, 0, 0, 0] #counter for 0s, 1s, 2s, etc... must be one place longer

# force user input 1 to 49
print('Chooose six unique numbers, all between 1 and 49: ')
for i in myRange:
	a = False
	while a == False:
		myStr= str(i +1) + ' of ' + str(myRange[-1] + 1) + ': '
		x = input(myStr)
		if x.isdigit() and int(x) in lottoCombi: # already selected
			print('Already taken, go again...')
			x = '0'
		elif not x.isdigit(): # not a number
			print('Must be a number...') 
			x = '0'
		elif int(x)>49: # over range
			print('Too big, go again...') 
			x = '0'
		a = x.isdigit() and int(x)>0 and int(x)<=49 and int(x) not in lottoCombi
	lottoCombi[i]= int(x)

lottoCombi.sort()

def sorteo():
	global lottoWeek, weeks, years, drawsPerWeek, drawsCount, totalDraws
	for i in myRange:
		x = random.randint(1,49)
		while x in lottoWeek: #avoid dupes
			x = random.randint(1,49)
		lottoWeek[i]= x
	lottoWeek.sort()
	totalDraws +=1
	drawsCount +=1
	if drawsCount == drawsPerWeek: #reset the counter and increase weeks
		drawsCount = 0
		weeks +=1
	years = (weeks*7)//365 # weeks to years, not considering leap years (this is a fun prog)

def compareResults():
	global currentMatches, tM
	matches =0
	for i in myRange:
		if lottoCombi[i] in lottoWeek:
			matches +=1
		currentMatches = matches
		tM[currentMatches] +=1
			

print('Your combination:', lottoCombi)
print('------------------------------------------------\n\\n\\n\n\n\\n')
print(f'\033[?25l', end='')#hide cursor, POSIX only
def pStats():
	print(f'\033[F\033[F\033[FLotto:', lottoWeek, 
			'\nMatches:', currentMatches, 'Draws:', totalDraws,'Weeks:', weeks, 'Years:', years, 
			'\n0s:', tM[0], '1s:', tM[1], '2s:', tM[2], 
			'3s:', tM[3], '4s:', tM[4], '5s:', tM[5], ' -- ', end=' ')
	if isWin:
		print('You WON!!!            ')
	else:
		print('No 6s yet...')

isWin = False

while isWin == False:	
	sorteo()
	compareResults()
	isWin= lottoCombi == lottoWeek
	pStats()

print(f'\033[?25h', end='')#bring cursor back, POSIX only
