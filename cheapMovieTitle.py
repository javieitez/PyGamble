#########################################################
#    Generate random B-movie titles
#########################################################

import random
from termcolor import cprint

def c(x):
    cprint(x, 'red', 'on_white')
def r(z):
    return random.choice(z)

isSequel = bool(random.getrandbits(1))

numeral = ['II', 'III', 'IV' ]
people = ['minds', 'creators', 'director', 'producers', 'catering team', 'writer', 
          'marketing assistant', 'assistant producer', 'cocaine addict', 'insane minds']
didWhat = ['responsible for', 'who brougth you', 'who perpetrated', 'that gave us', 'of',
           'who made', 'who made possible', 'who gave life to', 'who wrote']

adj = ['Lethal', 'Fatal', 'Tragic', 'Mortal', 'Deadly', 'Subtle', 'Dangerous', 'Unexpected', 
       'Suspicious', 'Catastrophic', 'A Very Fast', "My Sister's", 'The Biggest', "Grandma's", 
       'The last', 'Blind', 'Look At That', 'Somebody Stole My', 'The Unstoppable',
       "Your Husband's", 'Our forced', 'A Brave', 'A Bloody', 'The Naked', 'American', 
       'An Italian', 'The French', 'The Incredible', 'The Lost', 'Unfair', 'Impossible']

concept = ['Revenge', 'Affair', 'Christmas', 'Alliance', 'Engagement', 'Holiday', 
           'Jungle', 'Mutiny', 'Rebellion', 'Graduation', 'Prom', 'City', 'Starship',
           'Wedding', 'Machine Gun', 'Ninja', 'Warrior', 'Executioner', 'Cop', 'Fury',
           'Battle', 'High School', 'Scandal', 'War', 'Planet', 'Race', 'Rage', 'Soldier',
           'Detective', 'Driver', 'Captain']

sentence = 'from the ' + r(people) + ' ' + r(didWhat) + ' ' + r(adj) + ' ' + r(concept)

movieTitle = r(adj) + ' ' + r(concept)

c(sentence)
print('')
if isSequel == True:
    movieTitle = movieTitle + ' ' +  r(numeral)
    c(movieTitle)
else:
    c(movieTitle)
