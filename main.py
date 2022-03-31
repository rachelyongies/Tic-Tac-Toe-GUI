#Authors: Rachel Yong (01382292); Benjamin Yong, Cao Wanyue, Tian Mingze, Wei Hao

#player dictionary
players = {1:{"name":"Bob","choice":"X","pos":[],"score":0},2:{"name":"Tom","choice":"O","pos":[],"score":0}} 
	#convert the "pos" list to set when checking winning
start_player=1 #or 2
cur_player=start_player #or 2

def change_start_player(): #explain before teaching the full algo
	global cur_player, start_player
	if start_player==1:
		start_player=2
	else:
		start_player=1
	cur_player = start_player

def change_cur_player():
	global cur_player
	if cur_player==1: ### assginment in func will define a local var, not global var
		cur_player=2
	else:
		cur_player=1

# Function to print Tic Tac Toe

def print_tic_tac_toe():
	print("\n")
	print("\t     |     |")
	print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
	print('\t_____|_____|_____')

	print("\t     |     |")
	print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
	print('\t_____|_____|_____')

	print("\t     |     |")

	print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
	print("\t     |     |")
	print("\n")


# Function to print the score-board
def print_scoreboard():
	print("\t--------------------------------")
	print("\t       	   SCOREBOARD       ")
	print("\t--------------------------------")

	# players = list(score_board.keys())
	#use a loop to iterate players, can teach for statement here
	for k in players:
		print("\t   ", players[k]["name"], "\t    ", players[k]["score"])
	# print("\t   ", players[1]["name"], "\t    ", players[1]["score"])
	# print("\t   ", players[2]["name"], "\t    ", players[2]["score"])

	# print("\t   ", players[1], "\t    ", score_board[players[0]])
	# print("\t   ", players[2], "\t    ", score_board[players[1]])

	print("\t--------------------------------\n")

# Function to check if any player has won
def check_win():

	# All possible winning combinations
	soln = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, 
			{2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}] ##change ele to set to compare

	# Loop to check if any winning combination is satisfied
	for x in soln:
		if x <= set(players[cur_player]["pos"]): #change to set, use subset to check winning combo
			# Return True if any winning combination satisfies
			return True
	# Return False if no combination is satisfied		
	return False		

# Function to check if the game is drawn
def check_draw():
	if len(players[1]["pos"]) + len(players[2]["pos"]) == 9:
		return True
	return False		

# Function for a single game of Tic Tac Toe
def single_game():

	# Stores the positions occupied by X and O
	# player_pos = {'X':[], 'O':[]}
	
	# Game Loop for a single game of Tic Tac Toe
	while True:
		print_tic_tac_toe()
		
		# Try exception block for MOVE input
		try:
			print("Player ", players[cur_player]["name"], 
				"("+ players[cur_player]["choice"] + ") turn. Which box? : ")
			move = int(input())	
		except ValueError:
			print("Wrong Input!!! Try Again")
			continue

		# Sanity check for MOVE inout
		if move < 1 or move > 9:
			print("Wrong Input!!! Try Again")
			continue

		# Check if the box is not occupied already
		if values[move-1] != ' ':
			print("Place already filled. Try again!!")
			continue

		# Update game information

		# Updating grid status 
		values[move-1] = players[cur_player]["choice"]

		# Updating player positions
		players[cur_player]["pos"].append(move)

		# Function call for checking win
		if check_win():
			print_tic_tac_toe()
			print("Player ", players[cur_player]["name"], " has won the game!!")		
			print("\n")
			return cur_player

		# Function call for checking draw game
		if check_draw():
			print_tic_tac_toe()
			print("Game Drawn")
			print("\n")
			return 'D'

		# Switch player moves
		# if cur_player == 'X':
		# 	cur_player = 'O'
		# else:
		# 	cur_player = 'X'
		change_cur_player()

if __name__ == "__main__":

	players[1]["name"] = input("Player 1. Enter the name : ")  #player1
	print("\n")

	players[2]["name"] = input("Player 2. Enter the name : ")  #player2
	print("\n")
	
	# Stores the player who chooses X and O
	# player_name = players[1]["name"]   #player1

	# Stores the choice of players
	# player_choice = {'X' : "", 'O' : ""}

	# Stores the options
	# options = ['X', 'O']

	# Stores the scoreboard
	# score_board = {players[1]["name"]: players[1]["score"], players[2]["name"]: players[2]["score"]}  #{player1: 0, player2: 0}
	print_scoreboard()

	# Game Loop for a series of Tic Tac Toe
	# The loop runs until the players quit 
	while True:  #GUI is event driven, so don't need while loop

		# Player choice Menu
		print("Turn to choose for", players[start_player]["name"])
		print("Enter 1 for X")
		print("Enter 2 for O")
		print("Enter 3 to Quit")

		# Try exception for CHOICE input
		try:
			choice = int(input())	
		except ValueError:
			print("Wrong Input!!! Try Again\n")
			continue

		# Conditions for player choice	
		if choice == 1:
			players[start_player]["choice"] = "X"
			if start_player == 1:
				players[2]["choice"] = "O"
			else:
				players[1]["choice"] = "O"

		elif choice == 2:
			players[start_player]["choice"] = "O"
			if start_player == 1:
				players[2]["choice"] = "X"
			else:
				players[1]["choice"] = "X"
		
		elif choice == 3:
			print("Final Scores")
			print_scoreboard()
			break	

		else:
			print("Wrong Choice!!!! Try Again\n")

		# Stores the winner in a single game of Tic Tac Toe
		# Represents the Tic Tac Toe
		values = [' ' for x in range(9)]
		winner = single_game() #return either cur_player or D
		
		# Edits the scoreboard according to the winner
		if winner != 'D' :
			# player_won = player_choice[winner]
			players[winner]["score"] += 1 ##teach += here

		print_scoreboard()
		# Switch player who chooses X or O
		change_start_player()
		players[1]["pos"] = []
		players[2]["pos"] = []