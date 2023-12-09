
import re

# Read a list of games, parsing out the # of blue, green, and red cubes shown in any game
# Given a starting number of cubes of each color, identify which games are possible.
# Add the Game nums for the possible games.

reds = {}
greens = {}
blues = {}

game_num = 0
running_total = 0
rec_count = 0

def extract_cube_counts(a):
	ix =''
	match = re.search(r"Game (\d*):", a)
	if match:
		ix = int(match.group(1))
		#print("index {0}".format(ix))

		blues[ix] = [int(x) for x in re.findall(r"(\d*) blue", a)]
		greens[ix] = [int(x) for x in re.findall(r"(\d*) green", a)]
		reds[ix] = [int(x) for x in re.findall(r"(\d*) red", a)]
		#print("Blues: {0}".format(blues[ix]))
		#print("Greens: {0}".format(greens[ix]))
		#print("Reds: {0}".format(reds[ix]))
	return ix;

def game_power(game_number,red_list,blue_list,green_list):
	#max_red = 12
	#max_green = 13
	#max_blue = 14

	# in part 2, power is the sum of
	# the product of the min number of blue, min number of green, and min number of red cubes
	# NOTE: I bet there are few cases where 0 cubes are needed.  I wonder how that is handled?

	#print("Red {0}, Green {1}, Blue {2}".format(max(red_list),max(green_list),max(blue_list)))
	return max(red_list) * max(green_list) * max(blue_list);

with open('input.txt') as f:
	line = f.readline()

	while line:
		print('**********')
		print(line)
		rec_count += 1
		game_num = extract_cube_counts(line)
		running_total += game_power(game_num, reds[game_num], blues[game_num],greens[game_num])
		line = f.readline()

print("Running total is {0}".format(running_total))
print("Total records is {0}".format(rec_count))
