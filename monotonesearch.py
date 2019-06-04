# monotonesearch.py
# this script runs a brute-force search of essential 0-1 matrices
# looking for violations of monotonicity from n = 2 to n = 3
# and stores any that it finds in a file called examples.txt

import numpy as np

examples = []  # this is where we'll store any violations we find

for alphaSize in range(2,6): # alphabet size

    for adjInt in range(0, (2**(alphaSize**2) - 1)): # matrices as wrapped binary integers

        # convert the integer for a matrix into the matrix itself, called adj
    
        strList = list((bin(adjInt)[2:]))
        intList = [int(i) for i in strList]
        tooShort = (alphaSize**2) - len(intList)
        intList = ([0] * tooShort) + intList
    
        adj = np.array(intList).reshape(alphaSize,alphaSize)

        # check if adj is essential and store the answer as a bool isEssential
        myZeros = np.zeros(alphaSize, dtype=int)

        rowsGood = True
        colsGood = True

        for i in range(0,alphaSize):
            rowsGood = rowsGood and not(np.array_equal(adj[i,:], myZeros))
            colsGood = colsGood and not(np.array_equal(adj[:,i], myZeros))

        isEssential = rowsGood and colsGood

        # if adj is essential, check if it's an example of nonmonotonicity

        if isEssential:

            adjSquared = adj.dot(adj)

            if np.sum(adjSquared) > (float(np.sum(adj)))**1.5:

                examples.append(adj) 


for ex in examples:
    print(ex)
