#!/usr/bin/python3
#########################################################
# Lotto 6/49 simulator     ##  github.com/javieitez    ##
#
# Choose 6 numbers, then simulate a weekly lotto
# drawing that will run until the chosen combination wins 
#########################################################
import random

lottoWeek= [0, 0, 0, 0, 0, 0]
#lottoCombi= [0, 0, 0, 0, 0, 0]
lottoCombi= [7, 12, 26, 30, 41, 48] # hardcoded for debug
myRange= range(len(lottoCombi))
drawsPerWeek =3
totalDraws = drawsCount= weeks= years= 0
totalMatches= [0, 0, 0, 0, 0, 0] # counter for zeros, ones, twos, etc...

'''
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
		elif not x.isdigit():
			print('Must be a number...') # not a number
			x = '0'
		elif int(x)>49:
			print('Too big, go again...') # over range
			x = '0'
		a = x.isdigit() and int(x)>0 and int(x)<=49 and int(x) not in lottoCombi
	lottoCombi[i]= int(x)
'''
lottoCombi.sort()

def weeklyRun():
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
	years = (weeks*7)//365 # weeks to years, not considering leap years

def compareResults():
	global currentMatches, totalMatches
	matches =0
	for i in myRange:
		if lottoCombi[i] in lottoWeek:
			matches +=1
		currentMatches = matches
		totalMatches[currentMatches] +=1
			

print('Your combination:', lottoCombi)
print('------------------------------------------------\n\\n\\n\n\n\\n')
		
def pStats():
	print(f'\033[F\033[F\033[FLotto:', lottoWeek, 
			'\nMatches:', currentMatches, 'Draws:', totalDraws,'Weeks:', weeks, 'Years:', years, 
			'\n0s:', totalMatches[0], '1s:', totalMatches[1], '2s:', totalMatches[2], 
			'3s:', totalMatches[3], '4s:', totalMatches[4], '5s:', totalMatches[5], ' -- ', end=' ')
	if isWin:
		print('You WON!!!            ')
	else:
		print('No 6s yet...')

isWin = False

while isWin == False:
	weeklyRun()
	compareResults()
	isWin= lottoCombi == lottoWeek
	pStats()
