import math
import random

 ######################################## 
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
#% 					%#
#% Version 1.4				%#
#% By Kell Larson	    (24 hr)	%#
#% Last Edit: 2017, Oct 30, 01:35 	%#
#%					%#
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
 ########################################

def public_static_void_main(): #Memories of main methods past
	# Get game choice
	choice = getGameType()
	# if player vs player
	if(choice == 1):
		# play a game without an AI
		playGame(None, 0)
	elif(choice == 2):
		# Play a game with an untrained AI
		AI1 = generateAI()
		playGame(AI1, 1)
	else:
		print("Training AI, please wait...\n")
		# Amt of games for the AI to play against another AI to teach itself
		gameAmt = 5000
		# Play the (gameAmt) amount of games
		AI1 = doAIvsAIgame(gameAmt)
		# Start the player Vs AI game
		playGame(AI1, 1)

# Allows the user to pick one of three game types.
def getGameType():
	print("Would you like to play a game against another person,")
	print("Options:")
	print("Play against a friend (1)")
	print("Play against a computer (2)")
	print("Play against a trained computer (3)")
	print("Which option do you want (1-3)? ")
	# Get user input
	choice = int(input(''))
	# If user input is valid, return it
	if(choice > 0 and choice < 4):
		return choice
	# Otherwise tell them to try again, and the functon recurses.
	else:
		print("\n\nSelection error, Please try again.\n")
		return getGameType()

# Main game loop, allows games to be played one after another.
def playGame(AI1, vers):
	keepGoing = True
	# Loops until user tells program to quit at end of match
	while(keepGoing):
		# Gets the amount of nuts at the start
		totalNuts = gameSetup()
		# Allows passing of player numbers to the move function
		player1 = 1
		player2 = 2
		# Player 1 gets the first move
		currentTurn = 1
		# Keeps looping until win condition has been reached (No nuts left)
		while(True):
			# if the game has only 1 nut on board, do not print plural "nuts"
			if(totalNuts > 1):
				plural = "are {} nuts".format(totalNuts)
			else:
				plural = "is 1 nut"
			# print amt of nuts, with correct plurality
			print("There {} on the board".format(plural))
			# If player 1's turn
			if(currentTurn == 1):
				# get player 1's move
				totalNuts = totalNuts - playerMove(player1)
				# Check if they lost
				if(hasLost(totalNuts, currentTurn, True)):
					# end the loop if they have
					break
				# otherwise, hand over turn to player 2 (or AI)
				currentTurn = 2
			# If player 2's turn
			else:
				# if player vs AI
				if(vers == 1):
					# get AI to calculate its turn
					AI1, takenNuts = doAIturn(AI1, totalNuts)
					# print what the AI's turn selection is
					print("AI selects ", takenNuts, "\n")
					# update nut count
					totalNuts = totalNuts - takenNuts
					# check if has lost
					if(hasLost(totalNuts, currentTurn, True)):
						# break out of game loop if has lost
						break
					# otherwise, hand over turn to player 1
					currentTurn = 1
				# if player vs player
				else:
					# get player 2's move
					totalNuts = totalNuts - playerMove(player2)
					# check if has lost
					if(hasLost(totalNuts, currentTurn, False)):
						# break out of game loop if player has lost
						break
					# otherwise, hand over turn to player 1
					currentTurn = 1
		# LOOK HERE LOOK HERE
		# uncomment to print AI tables
		#print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n",AI1,"\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

		# check if user wants to continue, or quit
		keepGoing = checkIfContinue()

# Returns a boolean describing if the user would like to play another game.
def checkIfContinue():
	print('Play again (1 = yes, 0 = no)? ')
	# get user input
	choice = int(input(''))
	# If they picked no
	if(choice == 0):
		# close program
		return False
	# if they picked yes
	elif(choice == 1):
		# keep program going
		return True
	# otherwise...
	else:
		# Tell them to enter a proper input number
		print("\n\nSelection error, Please try again.\n")
		# And then recurse to allow them to try again entering in a proper number
		return checkIfContinue()

# Does a given amount of game sequentially between 2 distinct AI, "teaching" them the game.
# Returns one of the two AI to play against the human player.
def doAIvsAIgame(times):
	# Allows passing of player numbers to the move function
	player1 = 1
	player2 = 2
	# Player 1 gets the first move
	currentTurn = 1
	# Generate both AI players
	AI1 = generateAI()
	AI2 = generateAI()

	# Keeps looping until win condition has been reached (No nuts left)
	for i in range(times):
		# Randomized in order to acclimate AI to multiple game settings
		totalNuts = int(random.uniform(10,101))
		# Keep looping forever until broken out of by the out-of-nuts if
		while(True):
			if(currentTurn == 1):
				# Do a turn
				AI1, takenNuts = doAIturn(AI1, totalNuts)
				# update current amount of nuts on the board
				totalNuts = totalNuts - takenNuts
				# checks if the player has taken too many
				if(totalNuts < 1):
					# AI 1 Loses
					AI1 = AIlearn(AI1, False)
					# AI 2 Wins
					AI2 = AIlearn(AI2, True)
					# quit game loop, to allow another game to start
					break
				# If game is still going, AI 2 has the next turn
				currentTurn = 2
			else:
				AI2, takenNuts = doAIturn(AI2, totalNuts)
				totalNuts = totalNuts - takenNuts
				if(totalNuts < 1):
					# AI 1 Wins
					AI1 = AIlearn(AI1, True)
					# AI 2 Loses
					AI2 = AIlearn(AI2, False)
					# quit game loop, to allow another game to start
					break
				# If game is still going, AI 1 has the next turn
				currentTurn = 1
	# Return AI 2, could be either AI 1 or 2, but I've decided AI 2 to be returned
	return(AI2)	
	
# Called to allow a Human player to make a move, via console input of an integer.
def playerMove(player):
	# ask player for amt of nuts to take
	print("Player {}: How many nuts do you take (1-3)? ".format(player))
	nuts = input("")
	
	#checks of valid input
	if (int(nuts) > 0 and int(nuts) < 4):
		# if valid input, return it
		return int(nuts)
	else:
		#Recurses if improper input
		print("Please enter a number between 1 and 3.")
		return playerMove(player)

# Sets up the game, with player chosen amount of nuts.
def gameSetup():
	print("Welcome to the game of nuts!")
	print("How many nuts are there on the table initially (10-100)? ")
	# loops until proper value entered
	while(True):
		# get value entered
		totalNuts = int(input(""))
		# parses value
		if(totalNuts > 9 and totalNuts < 101):
			# returns value if valid
			return totalNuts
		else:
			# otherwise get user to try again
			print("Please enter a number between 10 and 100.")

# Returns True if no more nuts on the board, false if there are still nuts of the board.
# Has special print dialouges for whoever loses the game.
def hasLost(totalNuts, currentPlayer, isAI):
	# Game ends if there are no nuts left on the board
	if(totalNuts < 1):
		# Special dialouge if AI loses
		if(isAI):
			# Doesn't trigger AI dialouge if player loses
			if(currentPlayer == 1):
				# formats the print to player 1
				print("Player 1, you lose.")
			else:
				# User wins
				print('AI loses.')
		else:
			# Formats the print to accept lose from either player
			print("Player {}, you lose.".format(currentPlayer))
		# Lets the main loop know the game has ended
		return True
	else:
		# Lets the main loop keep going
		return False

# Generates the baseline AI
def generateAI():
	AI = []
	beside = -1
	# Generates 100 hats for the AI, 1 for each amount of nuts.
	# First entry in the tuple is the hat #.
	# Second entry is the content of the hat (the "balls").
	# THird entry is the beside, the used "balls".
	for i in range(101):
		# Creates a "hat", with default balls.
		AI.append([i,[1,1,1],beside])
	return AI

# Allows the AI to determine how many nuts to take.
def doAIturn(AI, nuts):
	# Randomly select one of the "balls" in the "hat"
	totalChoiceAmt = -1
	#print("Current hat vals: ",AI[nuts][1])
	for i in range(3):
		totalChoiceAmt += AI[nuts][1][i]
	choiceAmt = int(random.uniform(0, totalChoiceAmt + 1))
	#print("Chose reference ", choiceAmt)
	if(choiceAmt < AI[nuts][1][0]):
		#print('settings aside as 1')
		AI[nuts][2] = 1
		return AI, 1
	else:
		choiceAmt -= AI[nuts][1][0]
	if(choiceAmt < AI[nuts][1][1]):
		#print('setting aside as 2')
		AI[nuts][2] = 2
		return AI, 2
	else:
		choiceAmt -= AI[nuts][1][1]
	if(choiceAmt < AI[nuts][1][2]):
		#print('setting aside as 3')
		AI[nuts][2] = 3
		return AI, 3
	else:
		#print("ERR CHOICE EVERFLOW")
		chosenNumber = -1
	

def AIlearn(AI, hasWon):
	for i in range(len(AI)):
		#print('Aside val of hat ', i, ':  ', AI[i][2])
		if(AI[i][2] > 0):
			#print('detecting aside...')
			if(AI[i][2] == 1):
				if(hasWon):
					AI[i][1][0] += 1
					#print("1 given further priority")
				else:
					AI[i][1][0] -= 1
					#print("1 given less priority")
					if(AI[i][1][0] == 0):
						#print("1 reset to min priority")
						AI[i][1][0] = 1
			elif(AI[i][2] == 2):
				if(hasWon):
					AI[i][1][1] += 1
					#print("2 given further priority")
				else:
					AI[i][1][1] -= 1
					#print("2 given less priority")
					if(AI[i][1][1] == 0):
						#print("2 reset to min priority")
						AI[i][1][1] = 1
			elif(AI[i][2] == 3):
				if(hasWon):
					AI[i][1][2] += 1
					#print("3 given further priority")
				else:
					AI[i][1][2] -= 1
					#print("3 given less priority")
					if(AI[i][1][2] == 0):
						#print("3 reset to min priority")
						AI[i][1][2] = 1
	return AI

public_static_void_main() # Java!
