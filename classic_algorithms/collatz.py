############################################################################################################
# Collatz Conjecture - Start with a number n > 1. Find the number of steps it takes to reach one using the #
# following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.                #
############################################################################################################

inputNumber = int(raw_input("Type a number: "))
i = 0
print inputNumber
while inputNumber > 1:

 if inputNumber % 2 == 0:
     inputNumber = inputNumber/2
     print inputNumber
 else:
     inputNumber = 3 * inputNumber + 1
     print inputNumber
     i += 1;
