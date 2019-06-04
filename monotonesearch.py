# monotonesearch.py
# this script runs a brute-force search of essential 0-1 matrices
# looking for violations of monotonicity from n = 2 to n = 3
# and stores any that it finds in a file called examples.txt

import numpy as np

examples = []  # this is where we'll store any violations we find

for alphaSize in range(2,9): # alphabet size

    for adjInt in range(0, (2**(alphaSize**2) - 1)): # matrices as wrapped binary integers

        # convert the integer for a matrix into the matrix itself, called adj
    
        strList = list((bin(adjInt)))
        tooShort = (alphaSize**2) - len(strList)
        strList = (['0'] * tooShort) + strList
    
        adj = np.array(strList)).reshape(alphaSize,alphaSize)

        # check if adj is essential and store the answer as a bool

        isEssential = True

        
    
 

# if adj is not essential, throw it away


# else (i.e. if adj is essential), store its square as adjSquared


# let b2 and b3 be the entry sums of adj and adjSquared respectively


# if b3 > (float(b2))^(1.5) then append shiftNumber to examples


# print each example as a new line
