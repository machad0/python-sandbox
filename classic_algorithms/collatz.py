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
