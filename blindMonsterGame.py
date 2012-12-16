import random
from sys import exit

def roof():
	print "\n--------------------------------------------------------------------"
	print "\nAs you take a deep breath you smell 2 succulent humans far below"
	print "It's been so long since you've fed...."
	print "It would just take a moment to drain them both..."
	print "But still you're on the mission now, you shouldn't get sidetracked!"
	
	print """Do you:
	1. Swoop down to feed, or
	2. Focus on the mission
	Enter 1 or 2 to indicate your choice."""
	
	range = [1]
	for i in range: 	
		choice = raw_input("> ")
		
		if choice == "1":
			fightOne()
		elif choice == "2":
			circle()
		else:
			range.append(1)
			print "That wasn't one of the choices...try again."
			
def dodge():
	dodge = False
	agility = random.randint(1,10)
	if agility >=5:
		dodge = True
	else:
		dodge = False
	return dodge
		
def fightOne():
	dodged = dodge()
	print "\nAs you swoop down you hear the scream of a human."
	print "At the same time you hear the pounding of four feet on the pavement and two distinct sounds of heavy breathing."
	print "One of pair of feet slows down, you hear shuffling, then a click, a gun!"
	print "Everything slows down, you hear the sound of the bullet flying through the air..."
	print """Do you:
	1. Try to dodge, or 
	2. Attack the gun wielding human
	Enter 1 or 2 to indicate your choice."""
	
	range = [1]
	for i in range: 	
		choice = raw_input("> ")
		
		if choice == "1" and dodged:
			dodgedGun()
		elif choice == "1":
			dead()
		elif choice == "2":
			dead()
		else:
			range.append(1)
			print "That wasn't one of the choices...try again."
			
def dodgedGun():
	print "Your lightning fast reflexes and heightened agility meant you dodged the bullet"
	print """Do you want to:
	1. Fly away, or,
	2. Kill the arrogant humans
	Enter 1 or 2 to indicate your choice."""
	range = [1]
	for i in range: 	
		choice = raw_input("> ")
		
		if choice == "1":
			circle()
		elif choice == "2":
			dead()
		else:
			range.append(1)
			print "That wasn't one of the choices...try again."
	
def circle():
	print "As you circle the city from the skies you smell the target far bellow."
	print "You fly a little lower, the target seems to be surrounded by many humans."
	print "Probably inside a building but your echolocation doesn't extend that far."
	print "You decide to sneak in, you move to the place where you sense the least humans"
	print "and manage to sneak in successfully. The moment you enter you smell a human to"
	print "your right, you decide to kill  it, it is swift, you drink it's blood."
	print "You feel strength seeping into every part of your body nothing can stand in your way now"
	print "You locate the target and kill it. Well done!"
	raw_input("Press any key to exit...")
	exit(0)

def dead():
	print "It seems you're dead. Of course you're not REALLY dead because you're immortal ",
	print "but you're injury is too grave for you to continue the mission"
	print "Press q to exit or r to start again."
	
	range = [1]
	for i in range: 	
		choice = raw_input("> ")
		
		if choice == "q" or choice == "Q":
			exit(0)
		elif choice == "r" or choice == "R":
			roof()
		else:
			range.append(1)
			print "That wasn't one of the choices...try again."
	
def start():
	print "Hello and welcome to the Blind Monster Game"
	raw_input("Press any key to continue...")
	roof()
	
start()