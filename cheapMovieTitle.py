#############################################################
# Cheap movie title generator  ##  github.com/javieitez   ##
#
#  Generate random introductory lines and B-movie titles
#  by combining sentence parts. 
#  Useless, but fun. It can be used as a template for other
#  random generators. 
#############################################################
import random
from termcolor import cprint

def c(x):
    cprint(x, 'red', 'on_white')
def r(z):
    return random.choice(z)

isSequel = bool(random.getrandbits(1)) # Sometimes movies will be sequels, others won't

numeral = ['II', 'III', 'IV' ]

people = ['assistant producer', 'catering team', 'cocaine addict', 'creators', 'director', 
			'insane minds', 'marketing assistant', 'minds', 'producers', 'writer']

didWhat = ['of', 'responsible for', 'that gave us', 'who brougth you', 'who gave life to', 
			'who made', 'who made possible', 'who perpetrated', 'who wrote']

adj = ['A Bloody', 'A Brave', 'A Very Fast', 'American', 'An Italian', 'Blind', 'Catastrophic', 
		'Dangerous', 'Deadly', 'Fatal', "Grandma's", 'Impossible', 'Lethal', 'Look At That', 'Mortal', 
		"My Sister's", 'Our forced', 'Romantic', 'Somebody Stole My', 'Subtle', 'Suspicious', 
		'The Amazing', 'The Biggest', 'The French', 'The Incredible', 'The Last', 'The Lost', 
		'The Naked', 'The Unstoppable', 'Tragic', 'Unexpected', 'Unfair', "Your Husband's"]

concept = ['Affair', 'Alliance', 'Battle', 'Captain', 'Christmas', 'City', 'Cop', 'Detective', 
			'Driver', 'Engagement', 'Executioner', 'Fury', 'Graduation', 'High School', 'Holiday', 
			'Jungle', 'Machine Gun', 'Mutiny', 'Ninja', 'Planet', 'Prom', 'Race', 'Rage', 
			'Rebellion', 'Revenge', 'Scandal', 'Soldier', 'Starship', 'War', 'Warrior', 'Wedding']

sentence = 'from the ' + r(people) + ' ' + r(didWhat) + ' ' + r(adj) + ' ' + r(concept)

movieTitle = r(adj) + ' ' + r(concept)

c(sentence)
print('')
if isSequel == True:
    movieTitle = movieTitle + ' ' +  r(numeral)
    c(movieTitle)
else:
    c(movieTitle)
