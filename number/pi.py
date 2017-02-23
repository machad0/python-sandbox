#Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places. 
#Keep a limit to how far the program will go.

from decimal import Decimal, getcontext
int_input = ""
int_input = int(raw_input("type an int: "))
getcontext().prec = int_input
if int_input == 1:
    print 3
else:
    print sum(1/Decimal(16)**k * 
             (Decimal(4)/(8 * k + 1) - 
             Decimal(2)/(8 * k + 4) - 
             Decimal(1)/(8 * k + 5) -
             Decimal(1)/(8 * k + 6)) for k in xrange(0, 101))
