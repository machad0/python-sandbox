##########################################################################################
# Count Vowels - Enter a string and the program counts the number of vowels in the text. #
# For added complexity have it report a sum of each vowel found.                         #
##########################################################################################

input_string = ""
while input_string.upper() != 'Q':
	input_string = raw_input("Type a string to count the number of vowels or 'q' to exit: ")
	if input_string.upper() != 'Q':
		vowels = ['a', 'e', 'i', 'o', 'u']
		count_vowels = 0
		for vowel in vowels:
			print "the letter {0} has appeared {1} time(s).".format(vowel, input_string.lower().count(vowel))
			count_vowels += input_string.lower().count(vowel)

		print "total: {0}".format(count_vowels)
