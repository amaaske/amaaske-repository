import random # This is to import random to use the random function in the code.

# A sequence of assignments to generate a random problem:
minuend = random.randint(255, 259) # Used these bounds to avoid any borrowing during subtraction and to make sure that the difference is a positive, three-digit number.
subtrahend = random.randint(100, 105) # The hundreds place in the minuend is greater than the hundreds place in subtrahend, this guarantees that the difference will be a positive, three digit number. The tens of ones place of the minuend are both bigger than the respective places in the subtrahend and this guarantees that there will be no borrowing required.
answer = minuend - subtrahend # To find the difference between two random integers.

print ('Problem : {minuend} - {subtrahend} = ?'.format(minuend = minuend, subtrahend = subtrahend))
print ('Answer : {answer}'.format(answer = answer))

# Also did Comments assessment.