#read each line in file
#strip non-numeric characters
   # case where string = nineight -> value shoudl be nine.
   # find first single digit integer.
   # for each character
   	   # is character a single digit?
   	   #    if yes, add it to cleaned string
   	   # else, does new string start with a number in words
   	   #    if yes, add the digit to the cleaned string
   	   # else, add nothing to cleaned string.  
   	   # always chop off the one character from current string.

#take first value * 10 + take last value  -- these may be the same number, that's ok.
#store value
#sum all values
#print it out

import re
import inflect

# build dictionary of single digit integer and the english word for the integer.
def set_number_replacement_dict():
	p = inflect.engine()
	return {ix: p.number_to_words(ix) for ix in range(1,10)}


translation_dict = {}

def process_first_char(a):
	# return what, if anything to add to new string &
	#   remaining string that needs processing.

	#print("original string: " + a)
	#print("a[0]: " + a[0])
	for key in translation_dict:
		if (a[0] == str(key)):
			integer_found = a[0]
			remaining_string = a[1:]
			break		 
		elif (re.sub('^' + translation_dict[key],'', a) != a):
			integer_found = str(key)
			# stupid.  eighthree calibration should be 83, not 88.
			# so still only pop off the first char.
			remaining_string = a[1:]
			break
		else:
			integer_found = ''
			remaining_string = a[1:]
	#print("integer found: " + str(integer_found))
	#print("remaining string: " + remaining_string)
	return [integer_found, remaining_string]

def process_line(a):
	cleaned_string = a
	new_string = ''
	# iterate through the cleaned_string
	while ( len(cleaned_string) > 0 ):
		results = process_first_char(cleaned_string)
		new_string += results[0]
		cleaned_string = results[1]
	#print("original string: " + a)
	#print("new_string: " + new_string)
	return new_string

# coords are the first and last integers in a string
def find_coords(a):
	#result = process_line(a)
	return( int(a[0]) * 10 + int(a[-1]))

ix = 0
coord_list = []
translation_dict = set_number_replacement_dict()
print(translation_dict)

# test cases for process_first_char
#print(process_first_char("12345abd"))
#print(process_first_char("seven3a3"))
#print(process_first_char("anine8"))
#print(process_first_char("nineight"))
#

# test cases for process_line
#print(process_line("12345abd"))
#print(process_line("seven3a3"))
#print(process_line("anine8"))
#calibration for this is 98, not just 9
#print(process_line("nineight"))
#

with open('inputs.txt') as f:
	line = f.readline()
	while line:
		cleaned_string =  process_line(line)
		coord_list.append(find_coords(cleaned_string))		
		print(line + "," + cleaned_string + ","+str(find_coords(cleaned_string)))
		#print("Coord list: " + str(coord_list[ix]))
		ix += 1
		line = f.readline()

	print("Sum of coordinates:")
	print(sum(coord_list))
	print("length of coordinates:")
	print(len(coord_list))
