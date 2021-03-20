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

def is_valid_name(names, name):
	return name in names

def is_invalid_name(names, name):
	return not is_valid_name(names, name)

def read_all_lines_from_file(filename):
    with open(filename, 'r') as source_file:
        return source_file.readlines()

def strip_newlines(items):
    return list(map(lambda s: s.rstrip('\n'), items))

def update_scores_file(p1name, player1Score, p2name, player2Score):
	with open("scores.txt", "a") as source_file:
		source_file.write(p1name + ", " + str(player1Score) + "\n")
		source_file.write(p2name + ", " + str(player2Score) + "\n")

def evaluate_winner(p1name, player1Score, p2name, player2Score):
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


def play_game(whitelist):
	player1Score = 0
	player2Score = 0
	game = 1

	p1name = input("Player 1, what is your name: ")
	p2name = input("Player 2, what is your name: ")

	if is_invalid_name(whitelist, p1name) or is_invalid_name(whitelist, p2name):
		print("Incorrect names")
		exit()
		
	while game < 6:
		print("Round",game)
		pause()
		player1Score = player1Score + play_round(p1name)
		pause()
		player2Score = player2Score + play_round(p2name)
		pause()
		game = game + 1
		
	evaluate_winner(p1name, player1Score, p2name, player2Score)

	update_scores_file(p1name, player1Score, p2name, player2Score)

if __name__ == "__main__":
	play_game(strip_newlines(read_all_lines_from_file("whitelist.txt")))

