from enum import Enum
import random
import time

PAUSE_PERIOD = 0
EVEN_BONUS = 10
ODD_PENALTY = 5
MINIMUM_SCORE = 0

def add_dice(score1, score2):
	return score1 + score2

def rolled_double(total, roller):
	even_score = rolled_even(total)
	double_score = even_score + roller()
	print("Amazing, you rolled a double! Your new score is", double_score)
	return double_score

def rolled_even(total):
	print("You rolled an even total! You get an extra 10 points!")
	new_total = total + EVEN_BONUS
	print("Your new total is",new_total)
	return new_total

def rolled_low_odd(total):
	rolled_odd(total)
	print("You cannot go below 0, your new total is 0")
	return MINIMUM_SCORE

def rolled_odd(total):
	print("You rolled an odd total, you lose 5 points")
	new_total = total - ODD_PENALTY
	print("Your new total is", new_total)
	return new_total

def calculate_score(score1, score2, roller = lambda : random.randint(1,6), printer = lambda x: ()):
	dice_total = add_dice(score1, score2)
	if(score1 == score2):
		return rolled_double(dice_total, roller)
	if (dice_total % 2 == 0):
		return rolled_even(dice_total)
	if (dice_total < ODD_PENALTY):
		return rolled_low_odd(dice_total)
	return rolled_odd(dice_total)

def pause():
	time.sleep(PAUSE_PERIOD)

def random_roller():
	return random.randint(1,6)

def play_round(name, roller = lambda : random.randint(1,6), printer = lambda x: print(x)):
	dice_1 = roller()
	dice_2 = roller()
	printer(name + " has rolled " + str(dice_1) + " and " + str(dice_2))
	pause()
	printer(name + " has rolled a total of " + str(add_dice(dice_1, dice_2)))
	return calculate_score(dice_1, dice_2, roller, printer)

def play_game():
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
		player1Score = player1Score + play_round(p1name)
		pause()
		player = "2"
		player2Score = player2Score + play_round(p2name)
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

