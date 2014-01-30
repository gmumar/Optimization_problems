#!/usr/bin/python
# -*- coding: utf-8 -*-

def call(w,j):
    try:
        if(array[w][j]==-1):
            x = knap(w, j)
            insert(w, j, x)
            return int(x)
        else:
            return int(array[w][j])
    except IndexError:
        x = knap(w, j)
        insert(w, j, x)
        return int(x)
        

def insert(w, j, val):
    array[w][j] = (val)
    
def knap(w, j):

    if(j<0):
        return 0

    if(weights[j] > w):
        return call(w,j-1)
    else:
        return max(call(w,j-1) , values[j] + call(w - weights[j],j-1 )) 
        

def solveIt(inputData):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    items = int(firstLine[0])
    capacity = int(firstLine[1])

    global values
    global weights

    values = []
    weights = []

    for i in range(1, items+1):
        line = lines[i]
        parts = line.split()

        values.append(int(parts[0]))
        weights.append(int(parts[1]))

    items = len(values)

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = []

    item = 0
    bits = items
    item = 0
    out = ''
    j = 1

    print("Init")

    global array
    array = [[-1]*(items+1) for x in xrange(capacity+1)]

    print("Running")
    
    bestVal = knap(capacity,items-1)

##    for i in range(capacity):
##        for j in range(items):
##            print('{0},'.format(array[i][j])),
##        print('\n'),
##            
                

    # prepare the solution in the specified output format
    #outputData = str(value) + ' ' + str(0) + '\n'
    #outputData += ' '.join(map(str, taken))
    outputData = bestVal
    return outputData


import sys
import cmath

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

