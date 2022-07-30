# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <Joseph Schmidt>
# Creation Date: <7/30/2022>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

#Display text as each line with print 
def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = ''
#Watch for mixture of spaces and tabs these are causing a error
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()
#Spelling error caves should be cave
	return caves

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
#Time is not set for 2 seconds it is instead using a 3 not a 2
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
#Frogot the ( ) around the text
		print 'Gobbles you down in one bite!'

playAgain = 'yes'
#Both should be using an == sign
while playAgain = 'yes' or playAgain = 'y':
	displayIntro()
#Cave should have a capitol C as currently it is not linking
	caveNumber = choosecave()
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
#Playing is spelled wrong
		print("Thanks for planing")

#The ending could be done also by a if else 
#There is no code for a mistake if wrong input is done at the yes no phase the program ends with no notification