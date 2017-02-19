# -x- coding: utf-8 -x-
#############################################################################################################
# Fizz Buzz - Write a program that prints the numbers from 1 to 100.                                        #
# But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. #
# For numbers which are multiples of both three and five print “FizzBuzz”.                                  #
#############################################################################################################
for n in xrange(1, 101):
    output = ''
    if n % 3 == 0:
        output += "fizz"
    if n % 5 == 0:
        output += "buzz"
    print output or n
