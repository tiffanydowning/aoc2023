#read each line in file
#strip non-numeric characters
#take first value * 10 + take last value  -- these may be the same number, that's ok.
#store value
#sum all values
#print it out

import re
import inflect

number_list = []

def set_number_replacement_list():
	vals = []
	p = inflect.engine()
	for ix in range(0,10):
		vals.append(p.number_to_words(ix))
	return vals

def find_coords (a,b):
	cleaned_a = a
	for ix in range(0,10):
		cleaned_a = cleaned_a.replace(b[ix], str(ix))
	cleaned_a = re.sub('\D', '',cleaned_a)

	if len(cleaned_a) == 0:
	   	coord_as_num = 0
	else:
		coord_as_num = int(cleaned_a[0]) * 10 + int(cleaned_a[-1])
	return coord_as_num

ix = 0
coord_list = []
number_list = set_number_replacement_list()
print(number_list)

with open('test_inputs.txt') as f:
	line = f.readline()
	coord_list.append(find_coords(line,number_list))
	while line:
		print(line)
		print(coord_list[ix])
		ix += 1
		line = f.readline()
		coord_list.append(find_coords(line,number_list))

	print("Sum of coordinates:")
	print(sum(coord_list))
