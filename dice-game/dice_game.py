from enum import Enum
import random
import time

PAUSE_PERIOD = 0
EVEN_BONUS = 10
ODD_PENALTY = 5
MINIMUM_SCORE = 0

class Player:
	def __init__(self, name, score = 0):
		self.name = name
		self.score = score

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

def evaluate_winner(player1, player2, roller = random.randint(1,6)):
	winner = ""
	print(player1.name, "has a score of", player1.score, "and", player2.name, "has a score of", player2.score)
	if player1.score > player2.score:
		return player1

	if player1.score < player2.score:
		return player2

	while True:
		print("It's a draw!")
		p1Roll = roller()
		p2Roll = roller()
		print(player1.name, "rolled", p1Roll, "and", player2.name, "rolled", p2Roll)
		
		if p1Roll > p2Roll:
			return player1
		
		if p1Roll < p2Roll:
			return player2

def ask_for_name(name):
	return input(name + ", what is your name?: ")

def play_game(whitelist):
	player1 = Player(ask_for_name("Player 1"))
	player2 = Player(ask_for_name("Player 2"))

	if is_invalid_name(whitelist, player1.name) or is_invalid_name(whitelist, player2.name):
		print("Incorrect names")
		exit()
		
	round_number = 1
	while round_number < 6:
		print("Round",round_number)
		pause()
		player1.score += play_round(player1.name)
		pause()
		player2.score += play_round(player2.name)
		pause()
		round_number += 1
		
	winner = evaluate_winner(player1, player2)
	print(winner.name + " has won!")

	update_scores_file(player1.name, player1.score, player2.name, player2.score)

if __name__ == "__main__":
	play_game(strip_newlines(read_all_lines_from_file("whitelist.txt")))

