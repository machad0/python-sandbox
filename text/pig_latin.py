################################################################################################################################################################################
# Pig Latin - Pig Latin is a game of alterations played on the English language game.                                                                                          #
# To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay). #
# Read Wikipedia for more information on rules.                                                                                                                                #
################################################################################################################################################################################
input_string = ""
while input_string.upper() != 'Q':
	input_string = raw_input("kinda racist for a excercice, but anyway, press 'q' to quit: ")
	if input_string.upper() != 'Q':
		piggify = input_string[1:] + '-' + input_string[0] + 'ay'
		print piggify
