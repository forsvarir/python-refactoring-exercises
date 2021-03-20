import random
import time

PAUSE_PERIOD = 0
EVEN_BONUS = 10
ODD_PENALTY = 5
MINIMUM_SCORE = 0

def add_dice(score1, score2):
	return score1 + score2

def calculate_score(score1, score2):
	dice_total = add_dice(score1, score2)
	if (dice_total % 2 == 0):
		return dice_total + EVEN_BONUS
	if (dice_total < ODD_PENALTY):
		return MINIMUM_SCORE
	return dice_total - ODD_PENALTY

def pause():
	time.sleep(PAUSE_PERIOD)

def playRound(name = "default"):
	D1 = random.randint(1,6)
	D2 = random.randint(1,6)
	Total = add_dice(D1, D2)
	print(name, "has rolled", D1, "and", D2)
	pause()
	print(name, "has rolled a total of",Total)
	pause()
	if Total %2 == 0:
		print("You rolled an even total! You get an extra 10 points!")
		Total = Total + 10
		print("Your new total is",Total)

	else:
		print("You rolled an odd total, you lose 5 points")
		Total = Total - 5
		print("Your new total is", Total)
		
		if Total < 0:
			Total = 0
			print("You cannot go below 0, your new total is 0")

	if D1 == D2:
		D3 = random.randint(1,6)
		Total = Total + D3
		pause()
		print("Amazing, you rolled a double! Your new score is", Total)
	playRound.var = Total

def play_game():
	player1total = 0
	player2total = 0
	player1Score = 0
	player2Score = 0
	game = 1
	count = 0
	nameToCheck = "yes"

	p1name = input("Player 1, what is your name: ")
	p2name = input("Player 2, what is your name: ")
	fh = open("whitelist.txt", "r")

		
	while count < 3 and nameToCheck != "": 
		nameToCheck = fh.readline()[:-1]
		if nameToCheck == "":
			break
	#	print("DEBUG",nameToCheck)
	#	print("DEBUG",count)
		if nameToCheck == p1name or nameToCheck == p2name:
			count = count + 1
	fh.close()
		
	if count != 2:
		print("Incorrect names")
		exit()
		
	while game < 6:
		print("Round",game)
		pause()
		player = "1"
		player1total = playRound(p1name)
		player1Score = player1Score + int(playRound.var)
		pause()
		player = "2"
		player2total = playRound(p2name)
		player2Score = player2Score + int(playRound.var)
		pause()
		game = game + 1
		
	print(p1name, "has a score of", player1Score, "and", p2name, "has a score of", player2Score)
	if player1Score != player2Score and player1Score > player2Score:
		print(p1name, "has won!")

	elif player1Score != player2Score and player1Score < player2Score:
		print(p2name, "has won!")

	while player1Score == player2Score:
		print("It's a draw!")
		p1Roll = random.randint(1,6)
		p2Roll = random.randint(1,6)
		print(p1name, "rolled", p1Roll, "and", p2name, "rolled", p2Roll)
		
		if p1Roll > p2Roll:
			print(p1name, "has won!")
		
		elif p2Roll < p2Roll:
			print(p2name, "has won!")

	sf = open("scores.txt", "a")
	p1write = p1name + ", " + str(player1Score)
	p2write = p2name + ", " + str(player2Score)
	sf.write(p1write + "\n")
	sf.write(p2write + "\n")

	sf.close()

if __name__ == "__main__":
	play_game()

#highScore = open("scores.txt", "r")
#fileCount = 1
#added = False
#highScore.readline()












