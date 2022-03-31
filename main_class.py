#Authors: Rachel Yong (01382292); Benjamin Yong, Cao Wanyue, Tian Mingze, Wei Hao

class TicTacToe:
	def __init__(self, player1, player2):
		self.players = {1:{"name":player1,"choice":None,"pos":[],"score":0},
						2:{"name":player2,"choice":None,"pos":[],"score":0}} 
		self.start_player = 1
		self.cur_player = self.start_player
		self.values = [' ' for x in range(9)]
		
# #player dictionary
# players = {1:{"name":"Bob","choice":"X","pos":[],"score":0},2:{"name":"Tom","choice":"O","pos":[],"score":0}} 
# 	#convert the "pos" list to set when checking winning
# start_player=1 #or 2
# cur_player=start_player #or 2

	def change_start_player(self): #explain before teaching the full algo
		if self.start_player==1:
			self.start_player=2
		else:
			self.start_player=1
		self.cur_player = self.start_player

	def change_cur_player(self):
		if self.cur_player==1: ### assginment in func will define a local var, not global var
			self.cur_player=2
		else:
			self.cur_player=1

	# Function to print Tic Tac Toe

	def print_tic_tac_toe(self):
		values = self.values   ###save time to change all values to self.values below
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
	def print_scoreboard(self):
		print("\t--------------------------------")
		print("\t       	   SCOREBOARD       ")
		print("\t--------------------------------")

		# players = list(score_board.keys())
		#use a loop to iterate players, can teach for statement here
		for k in self.players:
			print("\t   ", self.players[k]["name"], "\t    ", self.players[k]["score"])
		# print("\t   ", players[1]["name"], "\t    ", players[1]["score"])
		# print("\t   ", players[2]["name"], "\t    ", players[2]["score"])

		# print("\t   ", players[1], "\t    ", score_board[players[0]])
		# print("\t   ", players[2], "\t    ", score_board[players[1]])

		print("\t--------------------------------\n")

	# Function to check if any player has won
	def check_win(self):

		# All possible winning combinations
		soln = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, 
				{2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}] ##change ele to set to compare

		# Loop to check if any winning combination is satisfied
		for x in soln:
			if x <= set(self.players[self.cur_player]["pos"]): #change to set, use subset to check winning combo
				# Return True if any winning combination satisfies
				return True
		# Return False if no combination is satisfied		
		return False		

	# Function to check if the game is drawn
	def check_draw(self):
		if len(self.players[1]["pos"]) + len(self.players[2]["pos"]) == 9:
			return True
		return False		

	# Function for a single game of Tic Tac Toe
	def single_game(self):

		# Stores the positions occupied by X and O
		# player_pos = {'X':[], 'O':[]}
		
		# Game Loop for a single game of Tic Tac Toe
		while True:
			self.print_tic_tac_toe()
			
			# Try exception block for MOVE input
			try:
				print("Player ", self.players[self.cur_player]["name"], 
					"("+ self.players[self.cur_player]["choice"] + ") turn. Which box? : ")
				move = int(input())	
			except ValueError:
				print("Wrong Input!!! Try Again")
				continue

			# Sanity check for MOVE inout
			if move < 1 or move > 9:
				print("Wrong Input!!! Try Again")
				continue

			# Check if the box is not occupied already
			if self.values[move-1] != ' ':
				print("Place already filled. Try again!!")
				continue

			# Update game information

			# Updating grid status 
			self.values[move-1] = self.players[self.cur_player]["choice"]

			# Updating player positions
			self.players[self.cur_player]["pos"].append(move)

			# Function call for checking win
			if self.check_win():
				self.print_tic_tac_toe()
				print("Player ", self.players[self.cur_player]["name"], " has won the game!!")		
				print("\n")
				return self.cur_player

			# Function call for checking draw game
			if self.check_draw():
				self.print_tic_tac_toe()
				print("Game Drawn")
				print("\n")
				return 'D'

			self.change_cur_player()
	
	def play(self):
		self.print_scoreboard()

		# Game Loop for a series of Tic Tac Toe
		# The loop runs until the players quit 
		while True:  #GUI is event driven, so don't need while loop

			# Player choice Menu
			print("Turn to choose for", self.players[self.start_player]["name"])
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
				self.players[self.start_player]["choice"] = "X"
				if self.start_player == 1:
					self.players[2]["choice"] = "O"
				else:
					self.players[1]["choice"] = "O"

			elif choice == 2:
				self.players[self.start_player]["choice"] = "O"
				if self.start_player == 1:
					self.players[2]["choice"] = "X"
				else:
					self.players[1]["choice"] = "X"
			
			elif choice == 3:
				print("Final Scores")
				self.print_scoreboard()
				break	

			else:
				print("Wrong Choice!!!! Try Again\n")

			# Stores the winner in a single game of Tic Tac Toe
			# Represents the Tic Tac Toe
			self.values = [' ' for x in range(9)]
			winner = self.single_game() #return either cur_player or D
			
			# Edits the scoreboard according to the winner
			if winner != 'D' :
				# player_won = player_choice[winner]
				self.players[winner]["score"] += 1 ##teach += here

			self.print_scoreboard()
			# Switch player who chooses X or O
			self.change_start_player()
			self.players[1]["pos"] = []
			self.players[2]["pos"] = []

if __name__ == "__main__":

	player1 = input("Player 1. Enter the name : ")  
	print("\n")

	player2 = input("Player 2. Enter the name : ") 
	print("\n")
	
	game = TicTacToe(player1, player2)

	game.play()