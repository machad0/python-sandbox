# -x- coding: utf-8 -x-

## Check if Palindrome - Checks if the string entered by the user is a palindrome.
## That is that it reads the same forwards as backwards like “racecar”
palindrome = ''
while palindrome.upper() != 'Q':
    palindrome = raw_input("check if the string is a palindrome or type 'q' to quit:  ")
    length = len(palindrome)
    for i in range(length/2):
        if (palindrome[length - i - 1] != palindrome[i]):
            break
    if (i == (length/2) - 1):
        print "True"
    else:
        print "False"
